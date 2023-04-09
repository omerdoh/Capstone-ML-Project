from flask import Flask, request, jsonify
from pdf2image import convert_from_path
from pathlib import Path
from pdfreader import PDFDocument

app = Flask(__name__)

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    pdf_file = request.files['pdfFile']
    print("File uploaded Successfully") 

    if Path(pdf_file).suffix != ".pdf":
        return ("The file is not a pdf file!")
    
    myFile = open(pdf_file, "rb")
    fileDoc = PDFDocument(myFile)

    page1 = next(fileDoc.pages())
    for font in sorted(page1.Resources.Font.keys()):
          print (font.BaseFont)

    for pageIndex in range(len(pdf_file)):
        page = pdf_file[pageIndex]
        imageList = page.getImageList()

        for image_index, img in enumerate(page.getImageList(), start=1):
                xref = img[0]
                base = pdf_file.extractImage(xref)
                imgBytes = base["image"] 

if __name__ == '__main__':
    app.run(port=5000)