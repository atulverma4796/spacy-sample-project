from PyPDF2 import PdfReader
import spacy

reader = PdfReader("src/samples/scheduled_texts.pdf")
number_of_pages = len(reader.pages)
nlp = spacy.load("en_core_web_sm")

for i in range(number_of_pages):
    if i == 0:
        page = reader.pages[i]
        text = page.extract_text()
        text = text.replace('\n', "")
        # print('text: ', text)
        doc = nlp(text)
        print('doc: ', doc)
        
        