#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: alepalroj
@file: tablesOnPdfToCsv.py
@time: 10/03/22 4:30 PM
"""

import argparse

PDF_ARGUMENT_NAME = 'pdf'
CONVERT_ARGUMENT_NAME = '--convert'
CONVERT_ARGUMENT_ACTION = 'store_true'
PDF_READER_MODE = 'rb'
CSV_EXTENSION = '.csv'
OUTPUT_FORMAT = "csv"
PROCESS_DESCRIPTION = 'Process of converting data tables in pdf file to csv files.'
PDF_ARGUMENT_HELP_DESCRIPTION = 'an pdf file name with data tables'
CONVERT_ARGUMENT_HELP_DESCRIPTION = 'convert data tables in pdf file to csv files'

def convert_pdf_to_csv(pdf_filename_with_extension):
        import tabula
        from pathlib import Path
        from PyPDF2 import PdfFileReader
        pdf_filename_without_extension = Path(pdf_filename_with_extension).stem
        reader = PdfFileReader(open(pdf_filename_with_extension, mode=PDF_READER_MODE))
        n = reader.getNumPages()
        df = []
        for page in [str(i+1) for i in range(n)]:
                tabula.convert_into(pdf_filename_with_extension, pdf_filename_without_extension+page+CSV_EXTENSION , output_format=OUTPUT_FORMAT,pages=page, stream=True)

parser = argparse.ArgumentParser(description=PROCESS_DESCRIPTION)
parser.add_argument(PDF_ARGUMENT_NAME, type=str, help=PDF_ARGUMENT_HELP_DESCRIPTION)
parser.add_argument(CONVERT_ARGUMENT_NAME, action=CONVERT_ARGUMENT_ACTION , help=CONVERT_ARGUMENT_HELP_DESCRIPTION)

args = parser.parse_args()

if args.convert:        
        convert_pdf_to_csv(args.pdf)

