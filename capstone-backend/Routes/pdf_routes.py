from flask import Flask, request, jsonify, send_file
#from Components.PdfScrape import *

def pdf_routes(app):

    @app.route('/pdf-upload', methods=['POST'])
    def pdf_upload():

        file = request.files['files']

        if 'files' not in request.files:
            return 'No file uploaded', 400
        if file.filename == '':
            return 'No file selected', 400
        if file:
            content = file.read() # reads the file as bytes
            newFile = open(".\capstone-backend\savedpdfs\\"+file.filename, "wb")# creates a new binary file
            newFile.write(content) # writes the content of the file to the new file
            newFile.close() # closes the file0
            #fianlProduct = test(content)
            return content , 200    
        
            '''
                {
                    filename:name,
                    content:bytes,
                    comments:{
                        aiRepsonse: 100%
                        aiComments[]
                    }
                }
            '''
        else:
            return 'File upload failed', 400
        
    @app.route('/', methods=['GET'])
    def index():
        return 'work'

