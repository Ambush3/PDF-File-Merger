import sys
from PyPDF2 import PdfFileMerger as pdfM

def mergePDF(files):
    filename = str(input("Enter the name of the new file: "))
    merger = pdfM()
    for i in files:
        merger.append(i)
    merger.write(filename)

files = sys.argv[1:]
mergePDF(files)
