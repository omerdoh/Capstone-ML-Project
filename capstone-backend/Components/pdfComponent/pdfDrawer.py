import fitz
from io import BytesIO
import io
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

def pdfDrawer(pdf_bytes, jsons):
    # pdf = fitz.open("pdf", BytesIO(pdf_bytes))

    pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(pdf_bytes))

    # Get the image data from the JSON
    image_path = jsons.get("image_path", "")
    image_x = jsons.get("x", 0)
    image_y = jsons.get("y", 0)
    image_width = jsons.get("width", 100)
    image_height = jsons.get("height", 100)

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # Iterate through each page of the PDF
    for page_num in range(pdf_reader.getNumPages()):
        # Get the current page from the reader
        page = pdf_reader.getPage(page_num)

        # Create a new page with the same dimensions and draw the image on it
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        img = ImageReader(image_path)
        can.drawImage(img, image_x, image_y, width=image_width, height=image_height)
        can.save()

        # Move the pointer to the beginning of the packet
        packet.seek(0)

        # Merge the new page (with the image) with the original page
        overlay_pdf = PyPDF2.PdfFileReader(packet)
        page.mergePage(overlay_pdf.getPage(0))

        # Add the modified page to the writer
        pdf_writer.addPage(page)

    # Save the modified PDF to a bytes buffer
    output_pdf_bytes = io.BytesIO()
    pdf_writer.write(output_pdf_bytes)

    return output_pdf_bytes.getvalue()

    # return pdf_bytes