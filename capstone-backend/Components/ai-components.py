#install version 2.8 of tensorflow
#pip install tensorflow==2.8 tensorflow==2.8 opencv-python matplotlib protobuf==3.19.1
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model
import base64

#load the model
model = load_model("capstone-backend\ai-model\models\algonquinModel_1.h5")

#function that loads the model and calculates the weight from the model
#img is an encoded base64 string
#returns an array with the weight and boolean 
#In current model, less than 0.5 means off brand, greater than 0.5 means on brand
def returnImageWeight(img):
    response = []
    if (img is None):
        raise ValueError("No or empty image was passed")

    image = cv2.imdecode(np.frombuffer(base64.b64decode(img),dtype=np.uint8),cv2.IMREAD_COLOR)
    resize = tf.image.resize(image,(256,256))
    weightArray = model.predict(np.expand_dims(resize/255,0))
    weight=weightArray[0][0]
    #return array with weight and response
    if(weight > 0.5):
        response = [weight,True]
    else:
        response =[weight,False]
    return response



