import os
from docx2pdf import convert as docx2pdf
from utils.file_handling import get_output_path

def convert(input_path, output_folder):
    output_path = get_output_path(input_path, output_folder, ".pdf")
    docx2pdf(input_path, output_path)
    return output_path