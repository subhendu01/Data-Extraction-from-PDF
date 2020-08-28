import PyPDF2
import pikepdf
import textract

# Read text from decrypted file
def read_text(file_name, password, encrypted_status):
    #calling the decrypt_file function for accessing the decrypted pdf
    # If file is encrypted than it will fetch the file name as new file name or it will take the old file name
    if encrypted_status == True:
        decrypt_file(file_name, password)
        filename = 'decrypt_'+file_name
    else:
        filename = file_name

    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(filename, method='tesseract', language='eng').decode("utf-8")
    print(text)
    # Writing all the data into one text file
    with open('data.txt', 'a+') as f:
        f.write(text)

# decrypt the encrypted pdf file and generating a new pdf
def decrypt_file(file_name, password):
    pdf = pikepdf.open(file_name,password = password)
    pdf.save('decrypt_'+file_name)

# call the read_text function
if __name__=="__main__":
    file_name = 'SWP.pdf'
    # If your pdf is encrypted than use your password here and make 'encrypted_status = True' else put it as 'False'
    password = 'csm2020'
    encrypted_status = True
    # Calling the read_text function
    read_text(file_name, password, encrypted_status)
