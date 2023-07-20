from Components.pdfComponent.pdfProccesor import pdfProccesor
from Components.pdfComponent.pdfDrawer import pdfDrawer
from Components.aicomponents import returnImageWeight

def pdfModule(bytes):

    pdf_bytes = bytes
     
    jsons = pdfProccesor(pdf_bytes)# this returns a json of all the images

    jsons["imageJson"] = returnImageWeight(jsons["imageJson"])

    # step 4: calcuate average acc per image - computer
    # what images need to be drawn on

    # step 5: reconstruct the pdf based on the json file -shivam

    # step 6: send neat package back to the route to be sent to the frontend for proccesing - whoever

    return pdf_bytes