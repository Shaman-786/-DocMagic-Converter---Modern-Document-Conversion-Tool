# -DocMagic-Converter---Modern-Document-Conversion-Tool
A sleek, feature-rich GUI application for converting between popular document formats with style
# DocMagic Converter

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

A modern, stylish document conversion tool with GUI that supports multiple file format conversions.

![Application Screenshot](assets/screenshots/main_ui.png)

## Features

- **Multiple Conversion Types**:
  - PDF ↔ Word (DOCX)
  - PDF ↔ Excel (XLSX)
  - PDF ↔ PowerPoint (PPTX)
  - PDF → JPG images

- **Beautiful Interface**:
  - Animated UI elements
  - Hover effects
  - Progress visualization
  - Dark/light mode ready

- **Smart Processing**:
  - Batch conversion support
  - Automatic file type detection
  - Unique output filenames
  - Preserves formatting

## Installation

### Prerequisites
- Python 3.8 or higher
- Tkinter (usually included with Python)
- [Poppler utils](https://poppler.freedesktop.org/) (for PDF to JPG conversion)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/docmagic-converter.git
   cd docmagic-converter

  ** Basic Workflow**
Select conversion type from dropdown
Choose input file
Select output directory
Click "Convert" button
View progress and completion status
docmagic-converter/
├── main.py                # Main application
├── converter/             # Conversion modules
│   ├── pdf_to_word.py
│   ├── word_to_pdf.py
│   └── ...
├── utils/                 # Utilities
│   ├── file_handling.py
│   └── helpers.py
├── assets/                # Resources
│   ├── icons/
│   └── sample_files/
├── requirements.txt       # Dependencies
└── README.md              # Documentation

Troubleshooting
Issue: "Cannot identify image file"
Solution: Ensure all icon files are present in assets/icons/

Issue: PowerPoint conversions fail
Solution: Ensure Microsoft PowerPoint is installed (Windows only)

Issue: PDF to JPG not working
Solution: Install poppler-utils:

Windows: Download from poppler.freedesktop.org

Mac: brew install poppler

Linux: sudo apt-get install poppler-utils

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch

Commit your changes

Push to the branch

Open a pull request
