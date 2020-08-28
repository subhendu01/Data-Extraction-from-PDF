# You should firstly install tesseract-ocr using this: on Linux: sudo apt-get install tesseract-ocr
import PyPDF2
import textract
import glob

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# Step 2:
# filename = 'Covid_Article_45.pdf'

pdf_dir = "Covid_medicine"  # folder name
pdf_files = glob.glob("%s/*.pdf" % pdf_dir)
for filename in pdf_files:
    # open allows you to read the file.
    pdfFileObj = open(filename, 'rb')
    # The pdfReader variable is a readable object that will be parsed.
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Discerning the number of pages will allow us to parse through all the pages.
    num_pages = pdfReader.numPages
    count = 0
    text = ""

    # The while loop will read each page.
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    # This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
    if text != "":
        text = text
    # If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
    # Convert bytes to a Python String
    else:
        text = textract.process(filename, method='tesseract', language='eng').decode("utf-8")
    # print(text)

    # Now we have a text variable that contains all the text derived from our PDF file. Type print(text) to see what it contains. It likely contains a lot of spaces, possibly junk such as '\n,' etc.#Now, we will clean our text variable and return it as a list of keywords.

    # Step 3: Convert text into keywords
    # The word_tokenize() function will break our text phrases into individual words.
    tokens = word_tokenize(text)
    # We'll create a new list that contains punctuation we wish to clean.
    punctuations = ['(', ')', ';', ':', '[', ']', ',', '.']

    # We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.
    stop_words = stopwords.words('english')

    # We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
    keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    print(keywords)