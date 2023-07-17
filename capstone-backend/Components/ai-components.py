#install version 2.8 of tensorflow
#pip install tensorflow==2.8 tensorflow==2.8 opencv-python matplotlib protobuf==3.19.1
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model
import base64
import json

#load the model
#model = load_model("capstone-backend\ai-model\models\algonquinModel_1.h5")
detectionModel = load_model("capstone-backend/ai-model/models/detectImagePeopleModel_V1.h5")
logoModel = load_model("capstone-backend/ai-model/models/logoModel_V1.h5")
peopleModel = load_model("capstone-backend/ai-model/models/peopleModel_V1.h5")

#function that loads the model and calculates the weight from the model
#jsonDoc is a json object
#img is an encoded base64 string
#returns an array with the weight and boolean 
#in current model, less than 0.5 means off brand, greater than 0.5 means on brand
def returnImageWeight(jsonDoc):
    response = []
    if(jsonDoc is None):
        raise ValueError("No jsonDoc was passed")
    img = None
    parseJson = json.loads(jsonDoc)
    for index in parseJson:

        img = index["image"]
        if (img is None):
            raise ValueError("No or empty image was passed")
        
        resize = _decodeResize(img)
        type = _detectImageType(resize)

        if (type is True):
            weightArray = logoModel.predict(np.expand_dims(img/255,0))
        else:
            weightArray = peopleModel.predict(np.expand_dims(img/255,0))
        

    weight=weightArray[0][0]
    #return array with weight and response
    if(weight > 0.5):
        response = [weight,True]
    else:
        response = [weight,False]
    return response

#detect if image is of logos or people
def _detectImageType(img):
    weightArray = detectionModel.predict(np.expand_dims(img/255,0))
    type = weightArray[0][0]

    #Logo is < 0.5, people is > 0.5
    if(type < 0.5): 
        #it is a logo
        return True
    else:
        #it is a person
        return False

def _decodeResize(img):
    img = cv2.imdecode(np.frombuffer(base64.b64decode(img),dtype=np.uint8),cv2.IMREAD_COLOR)
    resize = tf.image.resize(img,(256,256))
    return resize

"""
f = open('capstone-backend/Components/pdfComponent/testjson.json')
myJson = json.load(f)
for brand in myJson:
    img = brand["image"]
    resize = _decodeResize(img)
    type = _detectImageType(resize)
    #type is logo or people
    #send to which model
    #response[weight,true/false]
    #add to myJson
"""
