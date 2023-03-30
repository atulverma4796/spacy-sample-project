# Load a spacy model and chekc if it has ner
import spacy
nlp=spacy.load('en_core_web_sm')

# Getting the pipeline component
ner = nlp.get_pipe("ner")