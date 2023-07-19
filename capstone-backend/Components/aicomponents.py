'''
aicomponents.py 
Description: AI components used for reading json images and returning the ai image score
Variables: 
    detectionModel: detects if the image provided is of logos or people
    logoModel: detects if the logo provided is on brand for algonquin college
    peopleModel: detects if the people shown are on brand for algonquin college
Author: Kelsey Phillips
'''
import tensorflow as tf
import numpy as np
import cv2
from tensorflow.python.keras.models import load_model
import base64
import json

#load the models
#detectionModel - detects if the image provided is of logos or people
detectionModel = load_model("capstone-backend/ai-model/models/detectImagePeopleModel_V1.h5")
#logoModel - detects if the logo provided is on brand for algonquin college
logoModel = load_model("capstone-backend/ai-model/models/logoModel_V1.h5")
#peopleModel - detects if the people shown are on brand for algonquin college
peopleModel = load_model("capstone-backend/ai-model/models/peopleModel_V1.h5")

"""
returnImageWeight
Description: jsonDoc is a json object converted into a python dictionary
    Returns a parseJson dictionary containing the ai-response
Inputs:
    jsonDoc: A json object, interpreted as a python dictionary, 
    which accesses the jsonDoc['image'] as an encoded base64 string
Outputs:
    parseJson: Json object has ai-response appended to each indices of the jsonDoc
Variables: 
    response: ai-response[modelScore,good or bad value, corresponds to logo or person]
    weight: Less than 0.5 means off brand, greater than 0.5 means on brand
"""
def returnImageWeight(jsonDoc):

    response = []
    if(jsonDoc is None):
        raise ValueError("No jsonDoc was passed")
    img = None

    parseJson = json.loads(jsonDoc)

    for block in parseJson:
        
        img = block["image"]

        if (img is None):
            raise ValueError("No or empty image was passed")
        
        img = _decodeResize(img)
        imageType = _detectImageType(img)

        if (imageType == 'logo'):
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
        block['ai-response'] = response

    return parseJson


'''
_detectImageType(img):
Description: Detects if the image being processed is of people or logos and returns that result
Inputs:
    img: base64 encoded string
Outputs:
    string: returns a string as 'logo' or 'people'
Variables: 
    weightArray: returned value from detectionModel
    type: float of 0-1, determines if image is of people or logos
'''
def _detectImageType(img):
    weightArray = detectionModel.predict(np.expand_dims(img/255,0))
    type = weightArray[0][0]

    #Logo is < 0.5, People is > 0.5
    if(type < 0.5): 
        return 'logo'
    else:
        return 'people'

'''
_decodeResize(img): 
Description: Converts the base64 string into a cv2 object and resizes the image for processing
Inputs:
    img: base64 encoded string decoded to cv2 object
Outputs:
    resize: cv2 image resized to 256 by 256
'''
def _decodeResize(img):
    img = cv2.imdecode(np.frombuffer(base64.b64decode(img),dtype=np.uint8),cv2.IMREAD_COLOR)
    resize = tf.image.resize(img,(256,256))
    return resize


