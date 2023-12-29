from PyPDF2 import PdfReader
import re

reader = PdfReader("bank-statements\April-2023-Bank-Statement.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]


text = page.extract_text()

#words = text.split()
lines = text.splitlines()

for line in lines:
    words = line.split()
    pattern = re.compile("^([A-Z][0-9]+)+$")
    print(line)
    print("---")
    #pattern.match(string)

#print(text)
