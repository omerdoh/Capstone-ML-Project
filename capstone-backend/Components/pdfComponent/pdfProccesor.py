from io import BytesIO
import os
import json
import fitz
import base64

def pdfProccesor(pdf_bytes):

    pdf = fitz.open("pdf", BytesIO(pdf_bytes)) #this converts the bytes to a temp file that can then edited by the library

    imageJson = getImgData(pdf)
    textJson = checkTextAllowed(pdf)
    return {"imageJson":imageJson, "textJson": textJson}
    
def getImgData(pdf): #this gets the transform of the image the actual image as well as the page number and index of the image

    pageImgBlock = []
    jsonArray = []
    indexCounter = 0

    for page in pdf:
        d = page.get_text("dict")
        blocks = d["blocks"]
        imgblocks = [b for b in blocks if b["type"] == 1]
        pageImgBlock.append(imgblocks)

    for counter, img_blocks in enumerate(pageImgBlock, start=1):

        for images_in_blocks in img_blocks:

            jsonArray.append({
                "index":indexCounter,
                "page":counter,
                "transform":images_in_blocks["transform"],
                "image":base64.b64encode(images_in_blocks["image"]).decode('utf-8') # to use this you have to decode it utf-8
            })
            indexCounter = indexCounter + 1

    return json.dumps(jsonArray)

def checkTextAllowed(pdf):

    print("check pdf text")
    pageTextBlocks = []
    jsonArray = []
    
    for page in pdf:
        d = page.get_text("dict")
        blocks = d["blocks"]
        textblocks = [b for b in blocks if b["type"] == 0]
        pageTextBlocks.append(textblocks)

    for counter, text_blocks in enumerate(pageTextBlocks, start=1):

        for text_in_blocks in text_blocks:

            jsonArray.append(text_in_blocks)
    
    return jsonArray