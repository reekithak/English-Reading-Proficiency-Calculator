class DocSim:
    import numpy as np

    def __init__(self, w2v_model, stopwords=None):
        self.w2v_model = w2v_model
        self.stopwords = stopwords if stopwords is not None else []

    def vectorize(self, doc: str) -> np.ndarray:
        import numpy as np
        """
        Identify the vector values for each word in the given document
        :param doc:
        :return:
        """
        doc = doc.lower()
        words = [w for w in doc.split(" ") if w not in self.stopwords]
        word_vecs = []
        for word in words:
            try:
                vec = self.w2v_model[word]
                word_vecs.append(vec)
            except KeyError:
                # Ignore, if the word doesn't exist in the vocabulary
                pass

        # Assuming that document vector is the mean of all the word vectors
        # PS: There are other & better ways to do it.
        vector = np.mean(word_vecs, axis=0)
        return vector

    def _cosine_sim(self, vecA, vecB):
        import numpy as np
        """Find the cosine similarity distance between two vectors."""
        csim = np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB))
        if np.isnan(np.sum(csim)):
            return 0
        return csim

    def calculate_similarity(self, source_doc, target_docs=None, threshold=0):
        """Calculates & returns similarity scores between given source document & all
        the target documents."""
        if not target_docs:
            return []

        if isinstance(target_docs, str):
            target_docs = [target_docs]

        source_vec = self.vectorize(source_doc)
        results = []
        for doc in target_docs:
            target_vec = self.vectorize(doc)
            sim_score = self._cosine_sim(source_vec, target_vec)
            if sim_score > threshold:
                results.append({"score": sim_score, "doc": doc})
            # Sort results by score in desc order
            results.sort(key=lambda k: k["score"], reverse=True)

        return results



def process_tfidf_similarity(source_doc,target_docs):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    vectorizer = TfidfVectorizer()

    # To make uniformed vectors, both documents need to be combined first.
    target_docs.insert(0, source_doc)
    embeddings = vectorizer.fit_transform(target_docs)

    cosine_similarities = cosine_similarity(embeddings[0:1], embeddings[1:]).flatten()

    highest_score = 0
    highest_score_index = 0
    for i, score in enumerate(cosine_similarities):
        if highest_score < score:
            highest_score = score
            highest_score_index = i

    return highest_score
 # The text that we get from the converted voice note

def predict(source_doc,target_docs,model_path):
    from gensim.models.keyedvectors import KeyedVectors
    
    print("Started Execution")
    w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
    ds = DocSim(w2v_model)
    print("Model Loaded, Basic Evaluaiton Complete")
    sim_scores = ds.calculate_similarity(source_doc, target_docs)
    tf_score = process_tfidf_similarity(source_doc,target_docs)

    sim_score = 0
    print("Calculating Approximate score")
    if((sim_scores[0]['score']>=0.4) and (tf_score>=0.4)):
        document_similar = True
        sim_score = (sim_scores[0]['score']+tf_score)/2
    else:
        document_similar = False
        sim_score = (sim_scores[0]['score']+tf_score)/2
    
    

    

    return ({"Score ":sim_score,
    "document_similar":document_similar,
    "score_1":sim_scores[0]['score'],
    "score_2":tf_score})


