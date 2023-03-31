from PyPDF2 import PdfReader
import spacy
from training_data_generation import generateTrainingDataText

reader = PdfReader("src/samples/Hudson.pdf")
number_of_pages = len(reader.pages)
nlp = spacy.load("en_core_web_sm")

  
for i in range(number_of_pages):
    if i == 55:
        page = reader.pages[i]
        # text = page.extract_text()    
        text = 'POLICY NUMBER: 5050-0419-16 COMMERCIAL GENERAL LIABILITY CG 24 04 05 09 WAIV ER OF TRANSFER OF RIGHTS OF RECOVERY AGAINST OTHERS TO US This endorsement modifies insurance provided under the following : COMMERCIAL GENERAL LIABILITY COVERAGE PART PRODUCTS/COMPLETED OPERATIONS LIABILITY COVERAGE PART SCHEDULE Name Of Person Or Organization: AS PER WRITTEN CONTRACT Inform ation required to comp lete this Schedule , if not shown above , will be shown in the Declarations .'
        startText = 'Name Of Person'
        endText = 'WRITTEN CONTRACT'
        trainingDataText = generateTrainingDataText(text, startText, endText)
        print('trainingDataText: ', trainingDataText)
             
