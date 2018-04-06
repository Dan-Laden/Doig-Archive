import nltk, PyPDF2

print("Test File")

f = open("source/This-House-of-Sky-1-5.pdf", 'rb')

pdfReader = PyPDF2.PdfFileReader(f)

page = pdfReader.getPage(0)

for i in range(0, pdfReader.getNumPages()):
    print("==========================\n=\tPage "+(str)(i+1)+"\n==========================")
    page = pdfReader.getPage(i)
    print(page.extractText())
