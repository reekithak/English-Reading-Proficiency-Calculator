
def preprocess_image(image,target_size=(224, 224)):
    import tensorflow.keras
    import numpy as np
    from tensorflow.keras.preprocessing.image import load_img
    import tensorflow.keras
    from PIL import Image, ImageOps
    print("Image Preprocessing...")
    np.set_printoptions(suppress=True)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = ImageOps.fit(image, (224,224), Image.ANTIALIAS)
    image_array = np.asarray(image)
    image = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = image 
    
    return data


def predict_2(image):
    import tensorflow.keras
    processed_image = preprocess_image(image,target_size=(224,224))
    print("keras Model Loading")
    
    model = tensorflow.keras.models.load_model(".\Modules\Models\model.h5")
    print("Model Loading Complete")
    prediction = model.predict(processed_image).tolist()
    print("Prediction Complete")
    return prediction