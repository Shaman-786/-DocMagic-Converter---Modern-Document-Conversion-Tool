import os
from pdf2docx import Converter
from docx2pdf import convert as docx2pdf
from pdf2image import convert_from_path
import openpyxl
import win32com.client


def pdf_to_word(input_path, output_folder):
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".docx")
    cv = Converter(input_path)
    cv.convert(output_file, start=0, end=None)
    cv.close()


def word_to_pdf(input_path, output_folder):
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".pdf")
    docx2pdf(input_path, output_file)


def pdf_to_jpg(input_path, output_folder):
    images = convert_from_path(input_path)
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"page_{i+1}.jpg"), 'JPEG')


def excel_to_pdf(input_path, output_folder):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False
    wb = excel.Workbooks.Open(input_path)
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".pdf")
    wb.ExportAsFixedFormat(0, output_file)
    wb.Close()
    excel.Quit()
