from flask import Flask, request, jsonify, send_file

def image_routes(app):

    @app.route('/img-upload', methods=['POST'])
    def img_upload():

        files = request.files['images']

        print(files)

        return "hello", 200