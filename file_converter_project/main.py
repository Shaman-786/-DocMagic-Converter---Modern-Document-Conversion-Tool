import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
import os
import sys
from pathlib import Path
import time

# Add current directory to path
sys.path.append(str(Path(__file__).parent))
from converter import (
    pdf_to_word, word_to_pdf, pdf_to_jpg, excel_to_pdf
)

class DocumentConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Converter App")
        self.root.geometry("700x500")
        self.root.configure(bg="#f5f7fa")
        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.root, text="File Converter", font=("Arial", 20, "bold"), bg="#f5f7fa")
        title.pack(pady=10)

        # Conversion types
        self.conversion_var = tk.StringVar()
        ttk.Label(self.root, text="Select conversion type:").pack(pady=5)
        self.combo = ttk.Combobox(self.root, textvariable=self.conversion_var, state="readonly", width=40)
        self.combo['values'] = [
            "PDF to Word",
            "Word to PDF",
            "PDF to JPG",
            "Excel to PDF"
        ]
        self.combo.current(0)
        self.combo.pack(pady=5)

        # File chooser
        ttk.Label(self.root, text="Select input file:").pack(pady=5)
        self.file_path = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.file_path, width=60).pack(pady=5)
        ttk.Button(self.root, text="Browse", command=self.browse_file).pack(pady=5)

        # Output folder
        ttk.Label(self.root, text="Select output folder:").pack(pady=5)
        self.output_path = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        ttk.Entry(self.root, textvariable=self.output_path, width=60).pack(pady=5)
        ttk.Button(self.root, text="Change", command=self.browse_output).pack(pady=5)

        # Convert button
        ttk.Button(self.root, text="Convert", command=self.convert_file).pack(pady=20)

        self.status = tk.Label(self.root, text="", fg="green", bg="#f5f7fa")
        self.status.pack()

    def browse_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.file_path.set(file)

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path.set(folder)

    def convert_file(self):
        input_file = self.file_path.get()
        output_folder = self.output_path.get()
        conversion_type = self.conversion_var.get()

        if not os.path.exists(input_file) or not os.path.exists(output_folder):
            messagebox.showerror("Error", "Invalid input file or output folder.")
            return

        try:
            if conversion_type == "PDF to Word":
                pdf_to_word(input_file, output_folder)
            elif conversion_type == "Word to PDF":
                word_to_pdf(input_file, output_folder)
            elif conversion_type == "PDF to JPG":
                pdf_to_jpg(input_file, output_folder)
            elif conversion_type == "Excel to PDF":
                excel_to_pdf(input_file, output_folder)
            else:
                raise Exception("Unsupported conversion type.")

            self.status.config(text="Conversion successful!", fg="green")
        except Exception as e:
            self.status.config(text=f"Error: {e}", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = DocumentConverterApp(root)
    root.mainloop()
