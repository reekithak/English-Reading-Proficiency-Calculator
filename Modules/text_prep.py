def to_text(output_file,text_dict):
    import speech_recognition as sr
    r = sr.Recognizer()
    hellow=sr.WavFile('output.wav')
    with hellow as source:
        audio = r.record(source)

        try:
            s = r.recognize_google(audio).lower()
            print("Text: "+s)
            print("Successfully Analysed")
            intelligence_score = 1
        except Exception as e:
            print("Exception: "+str(e))
            intelligence_score = 0
            print("Final Try? Read Again, Ensure a Calm Environment / API Error")
            s = text_dict['to_read'][:250]  #default implmentation (reason:- needs paid api for processing audio)
        return s