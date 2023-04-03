import re

def normalize_text(text):
    text = text.replace('\n', "")
    text = re.sub(' +', ' ', text)
    text = text.replace("-", "")
    text = text.replace("–", "")
    text = text.lower()
    return text