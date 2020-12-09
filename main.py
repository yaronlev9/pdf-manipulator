import PyPDF2
import os
from PIL import Image


def relpath(filename):
    """
    this function finds the file in the directory
    :return: the relative path to the file
    """
    return os.path.join(os.path.dirname(__file__), filename)


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
    return number_of_pages


def remove_pages(path, pages_to_delete, output):
    output = 'removed_' + output
    pdf_reader = PyPDF2.PdfFileReader(path)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(pdf_reader.getNumPages()):
        if page in pages_to_delete:
            continue
        else:
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def merge_pdfs(paths, output):
    output = 'merged_' + output
    pdf_writer = PyPDF2.PdfFileWriter()
    for path in paths:
        pdf_reader = PyPDF2.PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def create_pdf_from_images(images, output):
    ims = []
    for image in images:
        im = Image.open(image)
        ims.append(im)
    ims[0].save(output, "PDF", resolution=100.0, save_all=True, append_images=ims[1:])

if __name__ == '__main__':
    # extract_information("combinedfile.pdf")
    # remove_pages('merged_combinedfile.pdf', [4, 5, 6, 7], 'combinedfile.pdf')
    # merge_pdfs(['removed_combinedfile.pdf', '2020.pdf'], 'grades sheet.pdf')
    # create_pdf_from_images(['2020.png'], '2020.pdf')
