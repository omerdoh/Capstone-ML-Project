from flask import Flask, request, jsonify
from flask_cors import CORS
# from flask_restful import Resource, Api, reqparse
# import pandas as pd
# import ast

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config['MAX_CONTENT_LENGTH'] = 30 * 1000 * 1000

@app.route('/pdf-upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    if file and allowed_file(file.filename):
        # Handle PDF file here
        return 'PDF file uploaded successfully'
    else:
        return 'File upload failed', 400

def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'
# check it is pdf or not
#

@app.route('/', methods=['GET'])
def index():
    return 'work'

if __name__ == '__main__':
    app.run(port=5000, debug=True)