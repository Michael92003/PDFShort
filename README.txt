PDFShort
A python program designed to remove redundant pages from pdfs, redundant pages being ones that are comprised entirely of text found in the next page. Shortened pdfs are written to the ShortPDFs folder. Any files in ShortPDFs with the same name as a file in LongPDFs will be overwritten, so be careful.

Contents:
 - PDFShort.py: the program that shortens the pdfs
 - LongPDFs: a directory containing the pdfs to be shortened
 - ShortPDFs: a directory that the shortened pdfs are written to
 - README.txt - this file

Additional requirements:
Requires that you have Python and PyPDF2 installed.
PyPDF2: https://pypi.org/project/PyPDF2/

Running instructions:
Place your pdf files in the LongPDFs folder, then run from the command line with python3 PDFShort.py. Remove the shortened files from ShortPDFs.
