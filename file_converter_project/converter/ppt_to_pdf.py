import os
import comtypes.client
import pythoncom
from utils.file_handling import get_output_path


def convert(input_path, output_folder):
    output_path = get_output_path(input_path, output_folder, ".pdf")

    try:
        # Initialize COM
        pythoncom.CoInitialize()
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1

        # Open presentation
        deck = powerpoint.Presentations.Open(os.path.abspath(input_path))

        # Save as PDF
        deck.SaveAs(os.path.abspath(output_path), 32)  # 32 is PDF format

        # Close and quit
        deck.Close()
        powerpoint.Quit()

        return output_path
    except Exception as e:
        raise Exception(f"PowerPoint conversion failed: {str(e)}")
    finally:
        pythoncom.CoUninitialize()