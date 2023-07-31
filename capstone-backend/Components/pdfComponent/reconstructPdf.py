import os
from PIL import Image
from fpdf import FPDF
import base64
import tempfile
from io import BytesIO

def create_pdf(jsonData):

    pdf = FPDF()
    pdf.set_auto_page_break(True, margin=15)

    for block in jsonData:

        image_bytes = base64.b64decode(block["image"])

        if block["ai-response"][1] == False:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                    temp_file.write(image_bytes)
                    image_path = temp_file.name

            im = Image.open(image_path)
           
            pdf.add_page()
            pdf.set_draw_color(255,0,0)
            pdf.set_fill_color(255,0,0)
            pdf.rect(24.75, 24.75, im.width/10 +.5, im.height/10 +.5, "DF")
            pdf.image(image_path, 25, 25, im.width/10, im.height/10)
            im.close()
            os.remove(image_path)

    pdf_data = pdf.output(dest='S').encode('latin1')

    return pdf_data