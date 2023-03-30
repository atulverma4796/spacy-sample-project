from PyPDF2 import PdfReader
import spacy

<<<<<<< HEAD
# reader = PdfReader("src/samples/scheduled_texts_three.pdf")
reader = PdfReader("src/samples/Hudson.pdf")
=======
reader = PdfReader("src/samples/schedule_text2.pdf")
>>>>>>> ef3aa94aa42de77b81bc54e65c48883e8f7ec26e
number_of_pages = len(reader.pages)
nlp = spacy.load("en_core_web_sm")

for i in range(number_of_pages):
    if i == 51:
        page = reader.pages[i]
        text = page.extract_text()
        text = text.replace('\n', "")
        print('text: ', text)
       
        