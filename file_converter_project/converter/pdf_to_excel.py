import os
import tabula
import pandas as pd
from utils.file_handling import get_output_path


def convert(input_path, output_folder):
    output_path = get_output_path(input_path, output_folder, ".xlsx")

    # Read PDF and extract tables
    tables = tabula.read_pdf(input_path, pages="all", multiple_tables=True)

    # Save each table to a separate sheet
    with pd.ExcelWriter(output_path) as writer:
        for i, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f"Table_{i + 1}", index=False)

    return output_path