from flask import Flask
from Routes.pdf_routes import pdf_routes
from Routes.image_routes import image_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config['MAX_CONTENT_LENGTH'] = 30 * 1000 * 1000

pdf_routes(app)
image_routes(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)