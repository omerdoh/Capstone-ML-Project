#install version 2.8 of tensorflow
#pip install tensorflow==2.8 tensorflow==2.8 opencv-python matplotlib protobuf==3.19.1
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model

#load the model
model = load_model("capstone-backend/ai-model/imageclassifier.h5")

#function that loads the model and calculates the weight from the model
#img is a cv2.imread('myimage.png') object
#returns a 0 to 1 float
#In current model, less than 0.5 means happy, greater than 0.5 means sad
def returnImageWeight(img):
    resize = tf.image.resize(img,(256,256))
    weightArray = model.predict(np.expand_dims(resize/255,0))
    weight=weightArray[0][0]
    return weight

#From original training set
#img1 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/happyimage1.jpg"))
#img2 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/happyimage2.jpg"))
#img3 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/sadimage1.jpg"))
#img4 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/sadimage2.jpg"))

#print(img1) #returns 0.35
#print(img2) #returns 0.029
#print(img3) #returns 0.99
#print(img4) #returns 0.99

#Pulled off the internet 2023/06/15
#img5 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/sadimage3.jpg"))
#img6 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/happyimage3.png"))
#img7 = returnImageWeight(cv2.imread("capstone-backend/ai-model/testImages/happyimage4.jpg"))

#print(img5) # returns 0.99 
#print(img6) # returns 1.0 this is wrong
#print(img7) # returns 0.99 this is also wrong