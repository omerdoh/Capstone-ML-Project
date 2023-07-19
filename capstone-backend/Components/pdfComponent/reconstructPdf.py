import os
from PIL import Image
from fpdf import FPDF
import base64

def pdf_to_bytes(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()
    return pdf_bytes

def reconstructPdf(json_data):
    # Sort the JSON data based on the "index" key
    sorted_json_data = sorted(json_data, key=lambda x: x['index'])
    # Create a new PDF object
    pdf = FPDF()

    # Set up the PDF document
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set the font and font size
    pdf.set_font("Arial", size=12)
   
    # Initial position for the first image
    x = 10
    y_txt = 10
    y_img = 10

    # Check is there more data or not
    has_next_data = True

    # Iterate over the JSON data
    for index, data in enumerate(json_data):
        if index < len(json_data) - 1:
            has_next_data = True
        else:
            has_next_data = False
        
        # Iterate over the items in each dictionary
        pdf.set_y(y_txt)
        pdf.set_x(120)
        pdf.set_font("Arial", style="B")
        pdf.cell(0, 10, "Location", ln=True)
        y_txt += 10

        for key, value in data.items():
            if key == "image":
                # Convert the base64 encoded image to bytes
                image_data = base64.b64decode(value)

                # Save the image to a file
                # image_file = f"temp_image_{data['index']}.png"

                # Save the image to a file with the appropriate format
                image_format = value.split(';')[0].split('/')[1]
                image_file = f"temp_image_{data['index']}.{image_format}"

                with open(image_file, 'wb') as file:
                    file.write(image_data)
                
                if is_image_format_supported(image_file) == False:
                    img = Image.open(image_file)
                    img = img.convert("RGBA")
                    png_image_file = f"temp_image_{data['index']}.png"
                    img.save(png_image_file, "PNG")
                    image_file = png_image_file
                    img.close()

                # Embed the image into the PDF
                pdf.image(image_file, x=x, y=y_img, w=100, h=100)

                # Update the position for the next image
                remaining_height = pdf.h - y_img - 100  # Calculate the remaining height after embedding the image
                if has_next_data == True and remaining_height < 100:
                    pdf.add_page()
                    y_img = 10  # Reset the y-coordinate for the new
                    y_txt = 10
                else:
                    y_img += 120
                    y_txt += y_img - y_txt
                
                # Remove the temporary image files
                os.remove(png_image_file)
                os.remove(f"temp_image_{data['index']}.{image_format}")
            else:
                pdf.set_y(y_txt)
                pdf.set_x(125)  # Set the x position to 125 units
                pdf.set_font("Arial", style="")
                pdf.cell(10, 10, f"{key}: {value}", ln=True)
            y_txt += 10

    pdf_path = "../../savepdfs/AIResponse.pdf"
    pdf.output(pdf_path)
    pdf_bytes = pdf_to_bytes(pdf_path)
    os.remove(pdf_path)
    return pdf_bytes


def is_image_format_supported(image_format):
    supported_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.wbmp']
    if image_format.lower() in supported_formats:
        return True
    else:
        return False
