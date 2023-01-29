import PyPDF2

pdfFile1 = open('meetingminutes1.pdf', 'rb')
pdfFile2 = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfReader(pdfFile1)
reader2 = PyPDF2.PdfReader(pdfFile2)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

output = open('combinedminutes.pdf', 'wb')
writer.write(output)
output.close()
pdfFile1.close()
pdfFile2.close()
