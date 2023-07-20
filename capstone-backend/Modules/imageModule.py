from Components.ImageComponents.imageProccesor import imageProccesor
from Components.aicomponents import returnImageWeight
from Components.pdfComponent.reconstructPdf import reconstructPdf
'''
natdyl <3 forever 
step 1: veify size = size matching

step 2: send an array of images to the ai model
    2.1: returning api response after completion
    {
    apiResponse:{
            response: x%
            comment:"
    }    
    }
step 3: add images to a created pdf

step 4: return the pdf neatly to the route 

'''

def imageModule(images):

    json = imageProccesor(images)#get the image json

    json = returnImageWeight(json)#get the weights

    #pdf = reconstructPdf(json)

    #json = createJsonFromImage(images)
