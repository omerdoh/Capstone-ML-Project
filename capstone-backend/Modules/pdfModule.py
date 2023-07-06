from Components.pdfComponent.pdfProccesor import pdfProccesor
import json
<<<<<<< HEAD
from pdfrw import PdfWriter
=======
>>>>>>> 35618eac59c158deb586ebfc1b57d71e1884dc86

def pdfModule(bytes):

    pdf_bytes = bytes
     
    # step 0: check locked pdf - Moses front and shivam back

    # step 1: temp save pdf no - salah (this does not need to happen)

    # step 2: breaking pdfs apart and saving imgs and logos - Moses

    jsons = pdfProccesor(pdf_bytes)# this returns a json of all the images

    with open("C:\\Users\\asdfg\\Desktop\\Capstone-ML-Project\\capstone-backend\\Components\\pdfComponent\\test.json", "w") as file:
         file.write(json.dumps(jsons["textJson"]))


    

    print(jsons["imageJson"][0])

    print(jsons["textJson"][0])


    #Example json testjson.json

        # step 2.1: make an array of images
        # step 2.2: algo to check all font in pdf (size,color,type)
        # step 2.3: create json for the pdf
    '''
        {
            img:{
                pageNumber:1
                index:1
                aiResponse:{
                    reponse: 85%
                    //comment:""
                }
                x:5,
                y:y
            }
            img2:{
                pageNumber:2
            }
        }
    '''
    # step 3: call the model to verify images and logos write to json - kelsey
    # step 4: calcuate average acc per image - computer
    # what images need to be drawn on
    # step 5: reconstruct the pdf based on the json file -shivam
    reconstructPdf(pdf_bytes, imageJson)
    # step 6: send neat package back to the route to be sent to the frontend for proccesing - whoever
    return pdf_bytes

def reconstructPdf(bytes, jsonData):
    try:
        data = json.loads(jsonData)
        image = data['image']
        aiResponse = data['aiResponse']
        page = data['page']
        index = data['index']
    except Exception as e:
        print("Invalidation inside JSON data")

    try:
        with PdfWriter("AIResponse.pdf") as pdf:
            # Need to design proper PDF below
            for img in image:
                pdf.save(img)
    except Exception as e:
        print("PDF generation FAILED")
