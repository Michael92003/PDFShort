import PyPDF2
import os

def findUseful(filename):
    """
    Finds pages that aren't redundant

    Arguments:
        filename (string): the name of the original pdf
        reader (PDFFileReader): a PDFFileReader for the pdf to be modified

    Return:
        Returns a list of pages containing the pages that aren't redundant
    """
    fin = open("LongPDFs/" + filename,"rb")
    reader = PyPDF2.PdfFileReader(fin)
    pages = []
    
    for i in range(reader.numPages-1):
        page = reader.getPage(i)
        nextPage = reader.getPage(i+1)
        if page.extractText() not in nextPage.extractText():
            pages.append(page)

    createNewPdf(filename,pages)
    fin.close()

def createNewPdf(filename,pages):
    """
    Creates a new pdf without any redundant pages in ShortPDFs

    Arguments:
        filename (string): the name of the original pdf
        pages (list of pages): a list of non-redundant pages

    Return:
        None
    """
    fout = open("ShortPDFs/" + filename,"wb")
    writer = PyPDF2.PdfFileWriter()
    
    for i in pages:
        writer.addPage(i)
    writer.write(fout)
    fout.close()
    

def removeRedundant(filename):
    """
    Finds redundant pages, then creates a new pdf without those pages in
    ShortPDFs

    Arguments:
        filename (string): the name of the original pdf

    Return:
        None
    """
    findUseful(filename)

def main():
    if not os.path.isdir("ShortPDFs"):
        os.mkdir("ShortPDFs")
    files = os.listdir("LongPDFs")
    for i in files:
        if i[-4:] == ".pdf":
            removeRedundant(i)
    

if __name__ == "__main__":
    main()
