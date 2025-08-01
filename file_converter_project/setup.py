import os
from setuptools import setup

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('assets')

setup(
    name='document_converter',
    version='1.0',
    packages=['converter', 'utils'],
    package_data={'': extra_files},
    include_package_data=True,
    install_requires=[
        'pillow',
        'pdf2docx',
        'docx2pdf',
        'pdf2image',
        'tabula-py',
        'pandas',
        'fpdf2',
        'python-pptx',
        'comtypes'
    ],
)