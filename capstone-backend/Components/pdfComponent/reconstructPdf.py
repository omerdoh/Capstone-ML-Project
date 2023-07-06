import json
from pdfrw import PdfWriter

def reconstructPdf(bytes, jsonData):
    try:
        data = jsonData
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