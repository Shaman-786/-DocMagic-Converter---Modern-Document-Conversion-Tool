import os
from pdf2image import convert_from_path
from utils.file_handling import get_output_path


def convert(input_path, output_folder):
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_folder = os.path.join(output_folder, base_name)
    os.makedirs(output_folder, exist_ok=True)

    images = convert_from_path(input_path)
    output_paths = []

    for i, image in enumerate(images):
        output_path = os.path.join(output_folder, f"{base_name}_page_{i + 1}.jpg")
        image.save(output_path, "JPEG")
        output_paths.append(output_path)

    return output_folder