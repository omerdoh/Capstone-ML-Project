import os
from PIL import Image
from fpdf import FPDF
import base64

def reconstructPdf(bytes, json_data):
    # try:
    #     data = jsonData
    #     image = data['image']
    #     aiResponse = data['aiResponse']
    #     page = data['page']
    #     index = data['index']
    # except Exception as e:
    #     print("Invalidation inside JSON data")

    # try:
    #     with PdfWriter("AIResponse.pdf") as pdf:
    #         # Need to design proper PDF below
    #         for img in image:
    #             pdf.save(img)
    # except Exception as e:
    #     print("PDF generation FAILED")

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
    # Specify the maximum height of the image on a page
    max_image_height = 100
    
    # Iterate over the JSON data
    for data in json_data:
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
                image_file = f"temp_image_{data['index']}.png"
                with open(image_file, 'wb') as file:
                    file.write(image_data)
                
                # Get the remaining space on the current page
                remaining_height = pdf.h - pdf.get_y()

                # Get the height of the image
                img = Image.open(image_file)
                image_height = img.height
                img.close()

                # Check if the image fits on the current page
                if image_height > remaining_height:
                    pdf.add_page()
                    y_img = 10  # Reset the y-coordinate for the new
                    y_txt = 10
                    
                # Embed the image into the PDF
                pdf.image(image_file, x=x, y=y_img, w=100, h=100)

                # Update the position for the next image
                y_img += 120
                # y_txt += y_img - y_txt

                # Remove the temporary image file
                os.remove(image_file)
            else:
                pdf.set_y(y_txt)
                pdf.set_x(125)  # Set the x position to 125 units
                pdf.set_font("Arial", style="")
                pdf.cell(10, 10, f"{key}: {value}", ln=True)
            y_txt += 10

