import json
import base64

def imageProccesor(images):

    jsonArray = []

    for image in images:
        #create json
        jsonArray.append({
            "image":base64.b64encode(image).decode('utf-8') # to use this you have to decode it utf-8"
        })

    return json.dumps(jsonArray)