import spacy
from spacy.matcher import PhraseMatcher
import re

# text = 'policy number: 1tpm ny1701234898 commercial general liability cg 20 37 04 13 this endorsement changes the policy. please read it carefully. cg 20 37 04 13 © insurance services office, in c., 2012 page 1 of 1 additional insured  owners, lessees or contractors  completed operations this endorsement modifies insurance provided under the following: commercial general liability coverage part products/completed operations liability coverage part schedule name of additional insured person(s) or organiz ation(s) location and description of completed oper ations as required by written contract executed prior to any claim or “suit.” as required by written contract executed prior to any claim or “suit.” information required to complete this schedule, if not shown above, will be shown in the declarations.'

text = 'policy number: 1tpm ny1701234898 commercial general liability cg 20 10 04 13 this endorsement changes the policy. please read it carefully. cg 20 10 04 13 © insurance services office, inc., 2012 page 1 of 2 additional insured  owners, lessees or contractors  scheduled person or organization this endorsement modifies insurance provided under the following: commercial general liability coverage part schedule name of additional insured pe rson(s) or or ganiz ation(s) location(s) of covered oper ations as required by written contract executed prior to any claim or “suit.” as required by written contract executed prior to any claim or “suit.” information required to complete this schedule, if not shown above, will be shown in the declarations.'

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
    'name of additional insured pe rson(s) or or ganiz ation(s) location(s) of covered oper ations as required by written contract executed prior to any claim or “suit.” as required by written contract executed prior to any claim or “suit.”',
]   
 
# Create Doc Objects For The Phrases
# Only run nlp.make_doc to speed things up
# patterns = [nlp(phrase) for phrase in phrases ]
patterns = [nlp.make_doc(phrase) for phrase in phrases]
# print('patterns: ', patterns)
matcher.add("AdditionalInsuredsPattern", patterns)

doc = nlp(text)

matches = matcher(doc)
for match_id, start, end in matches:
    string_id = nlp.vocab.strings[match_id]  
    span = doc[start:end]    
    spanText = span.text
    print('spanText: ', spanText)
    start_index = text.find(spanText)
    end_index = start_index + len(spanText)
    print('text: ', text)
    print('res: ', text[start_index:end_index])
        
        