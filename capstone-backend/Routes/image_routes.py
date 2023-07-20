from Modules.imageModule import imageModule
from flask import Flask, request, jsonify, send_file

def image_routes(app):

    @app.route('/img-upload', methods=['POST'])

    def img_upload():

        imageList = request.files.getlist("images")
        imageArray = []

        for image in imageList:
            imageArray.append(image.read())

        imageModule(imageArray)

        return "hello", 200