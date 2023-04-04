import re
from PyPDF2 import PdfReader
import spacy
from spacy.matcher import PhraseMatcher

from helper_functions import normalize_text


def generateTrainingDataText(text, startText, endText):  
    text = normalize_text(text)

    startindex = text.index(startText)
    endindex = text.index(endText)
    lengthOfEndText = len(endText)
    endindex = endindex + lengthOfEndText
    
    trainingDataText = text[startindex: endindex]
    print('trainingDataText: ', trainingDataText)
    return trainingDataText
 


def generateTrainingData():  
    text = 'POLICY NUMBER: 1TPM NY1701234898 COMMERCIAL GENERAL LIABILITY CG 20 37 04 13 THIS ENDORSEMENT CHANGES THE POLICY. PLEASE READ IT CAREFULLY. CG 20 37 04 13 © Insurance Services Office, In c., 2012 Page 1 of 1 ADDITIONAL INSURED  OWNERS, LESSEES OR CONTRACTORS  COMPLETED OPERATIONS This endorsement modifies insurance provided under the following: COMMERCIAL GENERAL LIABILITY COVERAGE PART PRODUCTS/COMPLETED OPERATIONS LIABILITY COVERAGE PART SCHEDULE Name Of Additional Insured Person(s) Or Organiz ation(s) Location And Description Of Completed Oper ations As Required by Written Contract executed prior to any claim or “suit.” As Required by Written Contract executed prior to any claim or “suit.” Information required to complete this Schedule, if not shown above, will be shown in the Declarations. A. Section II  Who Is An Insured is amended to include as an additional insured the person(s) or organization(s) shown in the Schedule, but only with respect to liability for "bodily injury" or "property damage" caused, in whole or in part, by "your work" at the location designated and described in the Schedule of this endorsement performed for that additional insured and included in the "productscompleted operations hazard". However: 1. The insurance afforded to such additional insured only applies to the extent permitted by law; and 2. If coverage provided to the additional insured is required by a contract or agreement, the insurance afforded to such additional insured will not be broader than that which you are required by the contract or agreement to provide for such additional insured. B. With respect to the insurance afforded to these additional insureds, the following is added to Section III  Limits Of Insurance: If coverage provided to the additional insured is required by a contract or agreement, the most we will pay on behalf of the additional insured is the amount of insurance: 1. Required by the contract or agreement; or 2. Available under the applicable Limits of Insurance shown in the Declarations; whichever is less. This endorsement shall not increase the applicable Limits of Insurance shown in the Declarations. CG 20 37 04 13 © Insurance Services Office, Inc., 2012 Page 1 of 1'
    startText = 'Name Of Additional Insured Person(s)'
    endText = '“suit.”'

    trainingDataText = generateTrainingDataText(text, startText, endText)
    return trainingDataText


def phraseMatcher(text):
    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    
    # List of Patterns To Match For
    # phrases = [
    #     'Name Of Additional Insured Person(s) Or Organization(s): As Required by Written Contract executed prior to any claim or “suit.”',
    #     'Name Of Additional Insured Person(s) Or Organiz ation(s) Location And Description Of Completed Oper ations As Required by Written Contract executed prior to any claim or “suit.” As Required by Written Contract executed prior to any claim or “suit.',
    #     'Name Of Additional Insured Person(s) Or Organization(s): The City of New York, including its officials and employees ; New York City Transit Authority ( "NYCT"), the Manhattan and Bronx Surface Transit Operating Authority ("MaBSTOA"), the Staten Island Rapid Transit Operating Authority ("SIRTOA"), the Metropolitan Transportation Authority ("MTA") including its subsidiaries and affiliates, MTA Capital Construction ("MTACC"), MTA Bus Company ("MTA Bus"), and the City of New York ("City" as Owner) and the representative affiliates and subsidiaries existing currently or in the future of and successors to each Indemnified Partie s listed herein.',
    #     'Name Of Additional Insured Person(s) Or Organization(s) Location(s) Of Covered Operations As required by written contract executed prior to the As required by writte n contract executed prior to date of an occurrence. the date of an occurrence.',
    #     'Name Of Additional Insured Person(s) Or Organization(s) As required by written contract executed prior to the date of an occurrence. If required by your written contract with the Additional Insured, this insurance shall be on a primary/noncontributory basis. The inclusion of one or more Additional Insured under the terms of this endorsement does not increase our limits of liability. All other terms and conditions remain unchanged.',
    #     'Name Of Additional Insured Person(s) Or Organization(s) Location And Description Of Completed Ooerations As required by written contract executed prior to the date of an occurrence. As required by written contract executed prior to the date of an occurrence.',
    #     'Name Of Additional Insured Person(s)Or Organization(s)Location And Description Of Completed Operations Any person or organization where the Named Insured has agreed in a written contract or agreement to name as an additional insured provided that the contract or agreement was executed prior to the loss or occurrence. All Locations at which the Named Insured completed operations.',
    #     'Name Of Additional Insured Person(s)Or Organization(s)Location(s) Of Covered OperationsAny person or organization where the Named Insured has agreed in a written contract or agreement to name as an additional insured provided that the contract or agreement was executed prior to the loss or occurrence. All Locations at which the Named Insured is performing ongoing operations.',    
    # ]
    
    phrases = [
        'name of additional insured person(s) or organization(s): as required by written contract executed prior to any claim or “suit.”',
        'name of additional insured person(s) or organiz ation(s) location and description of completed oper ations as required by written contract executed prior to any claim or “suit.” as required by written contract executed prior to any claim or “suit.',
        'name of additional insured person(s) or organization(s): the city of new york, including its officials and employees ; new york city transit authority ( "nyct"), the manhattan and bronx surface transit operating authority ("mabstoa"), the staten island rapid transit operating authority ("sirtoa"), the metropolitan transportation authority ("mta") including its subsidiaries and affiliates, mta capital construction ("mtacc"), mta bus company ("mta bus"), and the city of new york ("city" as owner) and the representative affiliates and subsidiaries existing currently or in the future of and successors to each indemnified partie s listed herein.',
        'name of additional insured person(s) or organization(s) location(s) of covered operations as required by written contract executed prior to the as required by writte n contract executed prior to date of an occurrence. the date of an occurrence.',
        'name of additional insured person(s) or organization(s) as required by written contract executed prior to the date of an occurrence. if required by your written contract with the additional insured, this insurance shall be on a primary/noncontributory basis. the inclusion of one or more additional insured under the terms of this endorsement does not increase our limits of liability. all other terms and conditions remain unchanged.',
        'name of additional insured person(s) or organization(s) location and description of completed ooerations as required by written contract executed prior to the date of an occurrence. as required by written contract executed prior to the date of an occurrence.',
        'name of additional insured person(s)or organization(s)location and description of completed operations any person or organization where the named insured has agreed in a written contract or agreement to name as an additional insured provided that the contract or agreement was executed prior to the loss or occurrence. all locations at which the named insured completed operations.',
        'name of additional insured person(s)or organization(s)location(s) of covered operationsany person or organization where the named insured has agreed in a written contract or agreement to name as an additional insured provided that the contract or agreement was executed prior to the loss or occurrence. all locations at which the named insured is performing ongoing operations.',    
        'name of additional insured person(s) or organization(s): the city of new york c/o nycdot office of permit management 55 water street new york, ny 10041 the city of new york, including its officials and employees',
        'name of additional insured person(s) or organization(s): location and description of completed operations any person or organization for whom you are performing operations during the policy period when you and such person or organization have agreed in writing in a contract or agreement that such person or organization be added as an additional insured on your policy. 520 e 137th street, bronx, ny 10457',
    ]
    
    # Create Doc Objects For The Phrases
    # Only run nlp.make_doc to speed things up
    patterns = [nlp.make_doc(phrase) for phrase in phrases]
    matcher.add("AdditionalInsuredsPattern", patterns)

    doc = nlp(text)

    matches = matcher(doc)
    
    training_data = None
    
    if (len(matches) > 0):
        for match_id, start, end in matches:
            string_id = nlp.vocab.strings[match_id]  
            span = doc[start:end]    
            spanText = span.text
            start_index = text.find(spanText)
            end_index = start_index + len(spanText)
            return (
                text,
                {"entities": [(start_index, end_index, "SCHEDULED_TEXT:ADDITIONAL_INSURED")]}
                )
    return training_data


def generateTrainingDataSetFromPDF(pdfFile):  
    reader = PdfReader(pdfFile)
    number_of_pages = len(reader.pages)
                
    texts = []
    training_data_set = []

    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()    
        text = normalize_text(text)

        texts.append(text)
        training_data = phraseMatcher(text)
        if training_data:
            training_data_set.append(training_data)
            
    return training_data_set


def generateTextsDataSetFromPDF(pdfFile):  
    reader = PdfReader(pdfFile)
    number_of_pages = len(reader.pages)
    texts = []
    for i in range(number_of_pages):
        if (i == 14):
            page = reader.pages[i]
            text = page.extract_text()    
            text = normalize_text(text)
            if text:
                texts.append(text)    
    return texts


def generateTestingDataTextFromPDF(pdfFile):  
    texts = generateTextsDataSetFromPDF (pdfFile) 
    return texts


def phraseMatcherInSentences(text):
    nlp = spacy.load("en_core_web_sm")
    phrase_matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    
    # List of Patterns To Match For
    phrases = [
        'name of additional insured person(s) or organization(s)', 
        'name of additional insured person(s) or orga nization(s)', 
        'location(s) of covered operations',
        'agreed in writing in a contract or agreement',
        'an additional insured on your policy',
        'the city of new york',
        'scheduled basis only',
        'any person or organization for whom you are performing operations during the policy period',
        'as required by written contract executed prior to the date of an occurrence',
        'any person or organization where the named insured has agreed',
        'all locations at which the named insured'
    ]
    
    patterns = [nlp(text) for text in phrases]
    phrase_matcher.add('AdditionlInsuredsScheduledText', None, *patterns)
    
    training_data = None
    
    scheduledTextsList = []
    scheduledText = ''
    
    doc = nlp(text)
    
    for sent in doc.sents:
        for match_id, start, end in phrase_matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in ["AdditionlInsuredsScheduledText"]:
                scheduledTextsList.append(sent.text)
    if (len(scheduledTextsList) > 0):
        entities = []
        scheduledTextsList = list(set(scheduledTextsList))
        for scheduledText in scheduledTextsList:
            start_index = text.find(scheduledText)
            end_index = start_index + len(scheduledText)
            entity = (start_index, end_index, "SCHEDULED_TEXT:ADDITIONAL_INSURED")
            entities.append(entity)
            
        training_data = (
            text,
            {"entities": entities}
        )
    
    return training_data


def sentenceExtraction():
    pdfFile = "src/samples/Additional-Insureds-Training.pdf"

    reader = PdfReader(pdfFile)
    number_of_pages = len(reader.pages)
                
    texts = []
    training_data_set = []

    for i in range(number_of_pages):
        if (i == 1):
            page = reader.pages[i]
            text = page.extract_text()    
            text = normalize_text(text)

            texts.append(text)
            training_data = phraseMatcherInSentences(text)
            if training_data:
                training_data_set.append(training_data)
            
    return training_data_set


pdfFile = "src/samples/Additional_Insureds_Training_Two.pdf"

if __name__ == "__main__":
    generateTrainingDataSetFromPDF(pdfFile)