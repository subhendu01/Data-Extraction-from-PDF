import PyPDF2
import textract

filename = 'decrypt_pdf-sample.pdf'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
print("page count : ",num_pages)
count = 0
text = ""

# Extracting text
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count += 1
    text += pageObj.extractText()

if text != "":
    text = text
else:
    text = textract.process(filename, method="tesseract", language='eng').decode("utf-8")

# print(text)

#writing data into a .txt file
with open('do_re_mi.txt', 'a+') as f:
    f.write(text)