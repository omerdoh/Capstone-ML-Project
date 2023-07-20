import fitz
from io import BytesIO

def pdfDrawer(pdf_bytes, json):

    pdf = fitz.open("pdf", BytesIO(pdf_bytes))

    for blocks in json:

        if blocks["ai-response"][1] == False:
            print(pdf[blocks["page"]])
            pdf[blocks["page"]].draw_rect([500,500,500,500], color = (0, 0, 0), width = 100)

    return pdf.write()



