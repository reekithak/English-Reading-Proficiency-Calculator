from Modules.generate import gpt2_generator
from Modules.Counter import countdown
import time
from Modules.record import read_out
from Modules.text_prep import to_text
from Modules.data_prepare import outside_fn
from Modules.ml_module1 import predict
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from Modules.ml_im_1 import predict_2
from Modules.i_score import inter_score
from Modules.f_score import final_score


# Work Flow Begins

text_dict = gpt2_generator()


print("Read The Below Sentence after the timer goes off,ignore the complex/unwanted Characters(75 Seconds, For Now).")
print("                         ")
print(countdown(10))
print(text_dict['to_read'])
read_out() # changes to make - add reocord start stop button
s = to_text("output.wav",text_dict)
outside_fn()
print("Machine Learning Model Analysing Begins")
model_path = r'Modules\Models\GoogleNews-vectors-negative300.bin'
prediction = predict(text_dict['to_check'],[s],model_path)
score_1 = prediction['Score ']
image = Image.open("output.jpg")
prediction_2 = predict_2(image)
score_2 = inter_score(prediction_2)
Final_Score  = final_score(score_1,score_2)
print("The final Predicted Score of Your Test is {}%, on an average".format(Final_Score))
print("Lots of Room for Improvements: ")
print("    a.) Vector-Model")
print("    b.) Spectrogram-Model")
print("    c.) Varied Implementation for Audio Input / Better Algorithm ")