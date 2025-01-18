import os
import pandas as pd
import pdfplumber

# Define standard headers
STANDARD_HEADERS = ["Name", "Date", "Amount"]

def extract_text_from_pdf(path_to_pdf):
    """
    Extract text from PDF using pdfplumber
    """

    extracted_data = []

    with pdfplumber.open(path_to_pdf) as pdf:
        for page in pdf.pages:
            # Extract tables if possible
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    extracted_data.extend(table)
            
            # if no tables are present
            else:
                # extract raw text
                extracted_data.append(page.extract_text())

    return extracted_data

if __name__ == "__main__":
    print("Hello World")