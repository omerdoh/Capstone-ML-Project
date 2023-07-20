import os
from PIL import Image
from fpdf import FPDF
import base64

def is_image_format_supported(image_format):
    supported_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.wbmp']
    if image_format.lower() in supported_formats:
        return True
    else:
        return False

def add_border_to_image(image_path, color, border_width):
    img = Image.open(image_path)
    # Calculate the new width and height to accommodate the border
    new_width = int(img.width + 2 * border_width)
    new_height = int(img.height + 2 * border_width)

    # Create a new image with the specified border color and size
    bordered_img = Image.new('RGBA', (new_width, new_height), color=color)
    bordered_img.paste(img, (int(border_width), int(border_width)))

    return bordered_img

def create_pdf(jsonData):
    # Sort the JSON data based on the "index" key
    sorted_json_data = sorted(jsonData, key=lambda x: x['index'])
    # Create a new PDF object
    pdf = FPDF()

    # Set up the PDF document
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_page()

    # Initial position for the first image
    x = 10
    y = 10

    # Check is there more data or not
    has_next_data = True
    
    # Iterate over the JSON data
    for index, data in enumerate(jsonData):
        # Check there is next dictonary in JSON data
        if index < len(jsonData) - 1:
            has_next_data = True
        else:
            has_next_data = False
        
        # Encode the bytes to base64
        image_data = base64.b64decode(data["image"])

        # Save the image to a file with the appropriate format
        image_format = data["image"].split(';')[0].split('/')[1]
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
        image_path = f"temp_image_{data['index']}.{image_format}"
        if data["ai-response"][1] == True:
            bordered_image = add_border_to_image(image_path, (0, 255, 0), 1)
        else:
            bordered_image = add_border_to_image(image_path, (255, 0, 0), 1)
        bordered_image_file = f"bordered_temp_image_{data['index']}.png"
        bordered_image.save(bordered_image_file)
        image_file = bordered_image_file

        # Get the actual width and height of the bordered image
        img_width, img_height = bordered_image.size

        # Embed the image into the PDF
        pdf.image(image_file, x=x, y=y, w=img_width, h=img_height)

        # Update the position for the next image
        remaining_height = pdf.h - y - 100  # Calculate the remaining height after embedding the image
        if has_next_data == True and remaining_height < 100:
            pdf.add_page()
            y = 10  # Reset the y-coordinate for the new
        else:
            y += img_height + 10
        
        # Remove the temporary image files
        os.remove(png_image_file)
        os.remove(f"temp_image_{data['index']}.{image_format}")

    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return pdf_bytes