import fitz
from io import BytesIO

def pdfDrawer(pdf_bytes, json):

    pdf = fitz.open(stream = pdf_bytes, filetype = "pdf")

    for blocks in json:

        page = pdf[blocks["page"]]

        if blocks["ai-response"][1] == False:

            x = blocks["transform"][4] # X-coordinate of the top-left corner
            y = blocks["transform"][5] # Y-coordinate of the top-left corner
            w = blocks["transform"][0]  # Width of the rectangle
            h = blocks["transform"][3]  # Height of the rectangle

            page.draw_rect(fitz.Rect(x, y, x + w, y + h), color=(1, 0, 0), width=2)

    pdf_bytes = pdf.write()
    pdf.close()

    return pdf_bytes



