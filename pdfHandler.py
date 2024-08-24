import PyPDF2
from pathlib import Path


# with open("pdf-files/dummy.pdf", "rb") as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     print(len(reader.pages))
#     text = reader.pages[0].extract_text()
#     print(text)


def pdf_merger():
    merger = PyPDF2.PdfMerger(strict=False)
    pdf_files = [file for file in Path("pdf-files").iterdir() if
                 file.suffix == ".pdf" and
                 (file.name != "super.pdf" and file.name != "watermarked.pdf")]
    for file in pdf_files:
        merger.append(file)
    with open("pdf-files/super.pdf", "wb") as combined:
        merger.write(combined)


def water_mark():
    template = PyPDF2.PdfReader(open("pdf-files/super.pdf", "rb"))
    watermark = PyPDF2.PdfReader(open("pdf-files/wtr.pdf", "rb"))
    output = PyPDF2.PdfWriter()
    for page in template.pages:
        page.merge_page(watermark.pages[0])
        output.add_page(page)
    with open("pdf-files/watermarked.pdf", "wb") as watermarked:
        output.write(watermarked)