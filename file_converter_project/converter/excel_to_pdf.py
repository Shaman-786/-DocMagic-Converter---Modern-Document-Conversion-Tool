import os
from fpdf import FPDF
import pandas as pd
from utils.file_handling import get_output_path


def convert(input_path, output_folder):
    output_path = get_output_path(input_path, output_folder, ".pdf")

    # Read Excel file
    xls = pd.ExcelFile(input_path)

    # Create PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=sheet_name, ln=1, align='C')

        # Add table
        col_width = pdf.w / (len(df.columns) + 1)
        row_height = pdf.font_size * 2

        # Header
        pdf.set_font("Arial", 'B', size=10)
        for col in df.columns:
            pdf.cell(col_width, row_height, str(col), border=1)
        pdf.ln(row_height)

        # Data
        pdf.set_font("Arial", size=8)
        for _, row in df.iterrows():
            for item in row:
                pdf.cell(col_width, row_height, str(item), border=1)
            pdf.ln(row_height)

    pdf.output(output_path)
    return output_path