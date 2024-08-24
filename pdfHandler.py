import PyPDF2
from pathlib import Path


with open("pdf-files/dummy.pdf", "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    print(len(reader.pages))
    text = reader.pages[0].extract_text()
    print(text)


def pdf_merger():
    merger = PyPDF2.PdfMerger()
    for file in Path("pdf-files").iterdir():
        if file.suffix == ".pdf":
            merger.append(file)
    merger.write("pdf-files/super.pdf")