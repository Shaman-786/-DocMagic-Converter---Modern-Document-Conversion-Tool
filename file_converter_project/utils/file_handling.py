import os
import uuid

def get_output_path(input_path, output_folder, new_extension):
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_name = f"{base_name}_{str(uuid.uuid4())[:4]}{new_extension}"
    return os.path.join(output_folder, output_name)