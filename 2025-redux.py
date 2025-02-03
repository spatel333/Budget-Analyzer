import os, sys
import pandas as pd
import pdfplumber, csv

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

def extract_text_from_csv(path_to_csv=None):
    """
    Extract data from CSV
    """

    # print(path_to_csv)
    with open(path_to_csv, "r") as csv_file:
        # print(csv_file)

        # creating a csvreader object
        csvreader = csv.reader(csv_file)

        # extract field names (from first row)
        fields = next(csvreader)

        print(fields)

if __name__ == "__main__":

    all_raw_filenames = os.listdir("./extract/raw_files/")

    absolute_filepaths_prefix =\
        os.path.abspath('.') + "/extract/raw_files/"
    
    for file in all_raw_filenames:
        extract_text_from_csv(absolute_filepaths_prefix + file)
        break
