from flask import Flask, request, render_template_string
from flask_cors import CORS
from pdfreader import PDFDocument
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import os
from io import BufferedReader
import numpy as pynum
from scipy import stats
import io

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config['MAX_CONTENT_LENGTH'] = 30 * 1000 * 1000

@app.route('/pdf-upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    print(request.files)
    file = request.files['file']
 
    if file:
        images = convert_from_bytes(file.read())
        for image in images:
            print(image.size)
            print(type(image))
            image = image.rotate(180)
            image.save("img1.jpg")
            
            width, height = image.size
            for x in range(0, width):
                for y in range(0, height):
                    coordinate = x,y
                    pixels = pynum.array(image.getpixel(coordinate))
                    print(image.getpixel(coordinate))

            print(stats.mode(pixels))
        # for page in images: 
        #     in_mem_file = io.BytesIO()
        #     page.save(in_mem_file , format = "png")
        #     in_mem_file.seek(0)
        #     break

        # img = Image.open(filestr)
        # print(img.size)
        # img = Image.open(request.files['file'])
        # img = np.array(img)
        # img = cv2.resize(img, (224,224))
        # img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        # fact_resp= model.predict(img)                         
        # print(fact_resp)

        # print(file.filename)   

        # npimg = numpy.frombuffer(filestr, numpy.uint8)
        # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
        # img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        # print(img)

        return 'PDF file uploaded successfully', 200
    else:
        return 'File upload failed', 400

def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

@app.route('/', methods=['GET'])
def index():
    return 'work'

if __name__ == '__main__':
    app.run(port=5000, debug=True)