import PyPDF2

pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)

print(len(reader.pages), end='\n\n')

page = reader.pages[0]
print(page.extract_text(), end='\n\n')

for pageNum in range(len(reader.pages)):
    page = reader.pages[pageNum]
    print(page.extract_text())