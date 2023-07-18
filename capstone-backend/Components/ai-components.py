import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model
import base64
import json

#load the models
detectionModel = load_model("capstone-backend/ai-model/models/detectImagePeopleModel_V1.h5")
logoModel = load_model("capstone-backend/ai-model/models/logoModel_V1.h5")
peopleModel = load_model("capstone-backend/ai-model/models/peopleModel_V1.h5")
"""
Function that loads the model and calculates the weight from the model
jsonDoc is a json object converted into a python dictionary
jsonDoc['image'] is an encoded base64 string
Returns a parseJson dictionary containing the ai-response
ai-response[modelScore,good or bad value, corresponds to logo or person]
In current model, less than 0.5 means off brand, greater than 0.5 means on brand
"""
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
        
        img = _decodeResize(img)
        imageType = _detectImageType(img)

        if (imageType is True):
            weightArray = logoModel.predict(np.expand_dims(img/255,0))
        else:
            weightArray = peopleModel.predict(np.expand_dims(img/255,0))     

        weight=weightArray[0][0]

        #return array with weight and response response[AI score, good/bad score, logo/person]
        if(weight > 0.5):
            response = [weight,True,imageType]
        else:
            response = [weight,False,imageType]
        
        #_appendtoJson()
        index['ai-response'] = response
    return parseJson


#Detects if image is of logos or people
def _detectImageType(img):
    weightArray = detectionModel.predict(np.expand_dims(img/255,0))
    type = weightArray[0][0]

    #Logo is < 0.5, People is > 0.5
    if(type < 0.5): 
        return 'logo'
    else:
        return 'people'

#Converts the base64 image into cv2 format and resizes the image for the AI
def _decodeResize(img):
    img = cv2.imdecode(np.frombuffer(base64.b64decode(img),dtype=np.uint8),cv2.IMREAD_COLOR)
    resize = tf.image.resize(img,(256,256))
    return resize


