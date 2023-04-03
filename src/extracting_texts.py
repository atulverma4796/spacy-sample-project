from PyPDF2 import PdfReader
import spacy
from helper_functions import normalize_text
from training_data_generation import generateTrainingDataText, phraseMatcher

reader = PdfReader("src/samples/schedule_text1.pdf")
number_of_pages = len(reader.pages)
nlp = spacy.load("en_core_web_sm")

texts = []
training_data_set = []

for i in range(number_of_pages):
    if (i == 4):
        page = reader.pages[i]
        text = page.extract_text()    
        startText = 'name of additional insured'
        endText = '“suit.”'
        text = normalize_text(text)
        texts.append(text)
        training_data = phraseMatcher(text)
        if training_data:
            training_data_set.append(training_data)
            
print('training_data_set: ', training_data_set)      
            
       