import os
from pdf2docx import Converter
from utils.file_handling import get_output_path

def convert(input_path, output_folder):
    output_path = get_output_path(input_path, output_folder, ".docx")
    cv = Converter(input_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()
    return output_path