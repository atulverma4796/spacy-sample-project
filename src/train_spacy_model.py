import random
import spacy
from pathlib import Path
from tqdm import tqdm 
from spacy.tokens import DocBin
from spacy.util import minibatch, compounding
from pathlib import Path
from spacy.training import Example 
from training_data import TRAIN_DATA

model = None
num_of_iterations = 10

#load the model
if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")

for text, annot in tqdm(TRAIN_DATA): 
    db = DocBin()
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    print('doc.ents: ', doc.ents)
    db.add(doc)

db.to_disk("./train.spacy") 



# TODO

# def train_spacy(model=None, output_dir=None, n_iter=1):
#     """Load the model, set up the pipeline and train the entity recognizer."""
#     if model is not None:
#         nlp = spacy.load(model)  # load existing spaCy model
#         print("Loaded model '%s'" % model)
#     else:
#         nlp = spacy.blank("en")  # create blank Language class
#         print("Created blank 'en' model")

#     # create the built-in pipeline components and add them to the pipeline
#     # nlp.create_pipe works for built-ins that are registered with spaCy
#     if "ner" not in nlp.pipe_names:
#         # ner = nlp.create_pipe("ner")
#         # nlp.add_pipe(ner, last=True)
#         ner = nlp.add_pipe("ner")
#     # otherwise, get it so we can add labels
#     else:
#         ner = nlp.get_pipe("ner")

#     # add labels
#     for _, annotations in TRAIN_DATA:
#         for ent in annotations.get("entities"):
#             # print(f"ent {ent}")
#             ner.add_label(ent[2])

#     # print('ner labels: ', nlp.get_pipe('ner').labels)
#     # get names of other pipes to disable them during training
#     pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
#     other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
#     # only train NER
#     with nlp.disable_pipes(*other_pipes):  # only train parser
#         optimizer = nlp.begin_training()
#         for itn in range(n_iter):
#             random.shuffle(TRAIN_DATA)
#             losses = {}
#             # batch up the examples using spaCy's minibatch
#             batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
#             for batch in batches:
#                 texts, annotations = zip(*batch)
                
#                 example = []
#                 # Update the model with iterating each text
#                 for i in range(len(texts)):
#                     doc = nlp.make_doc(texts[i])
#                     example.append(Example.from_dict(doc, annotations[i]))
#                 # Update the model
#                 nlp.update(example, drop=0.5, losses=losses)
                
#     print('ner labels: ', nlp.get_pipe('ner').labels)
#     # test the trained model
#     for text, _ in TRAIN_DATA:
#         doc = nlp(text)
#         # print('doc: ', doc)
#         print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
#         # print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

#     # save model to output directory
#     if output_dir is not None:
#         output_dir = Path(output_dir)
#         if not output_dir.exists():
#             print("output_dir NOT EXISTS")
#             output_dir.mkdir()
#         nlp.to_disk(output_dir)
#         print("Saved model to", output_dir)

#         # test the saved model
#         print("Loading from", output_dir)
#         nlp2 = spacy.load(output_dir)
# #        for text, _ in TRAIN_DATA:
# #            doc = nlp2(text)
# #            print("Entities", [(ent.text, ent.label_) for ent in doc.ents])
# #            print("Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

# train_spacy()

# TODO


## Issue with data set

 # (
    #      'POLICY NUMBER:  1-TPM -NY-17-01234898  COMMERCIAL GENERAL LIABILITY   CG 24 17 10 01   THIS ENDORSEMENT CHANGES THE POLICY.  PLEASE READ IT CAREFULLY.  CG 24 17 10 01  © ISO Properties, Inc.,  2000   Page 1 of 1   CONTRACTUAL LIABILITY – RAILROADS  This endorsement modifies insurance provided under the following:   COMMERCIAL GENERAL LIABILITY COVERAGE PART   SCHEDULE   Scheduled Railroad:   Designated Job Site:  All Railroads  All Jobsites           (If no entry appears above, information required to complete this endorsement will be shown in the Declarations as applicable to this endorsement.)',
    #     {"entities": [(374, 431, "SCHEDULED_TEXT:RAILROAD"), (396, 445, "SCHEDULED_TEXT:PROJECT_COVERAGE")]}
    # ),
# (
    #     'POLICY NUMBER: COMMERCIAL GENERAL LIABILITY CG 241710 01 THIS ENDORSEMENT CHANGES THE POLICY. PLEASE READ IT CAREFULLY. CONTRACTUAL LIABILITY -RAILROADS This endorsement modifies insurance provided under the following : COMMERCIAL GENERAL LIABILITY COVERAGE PART SCHEDULE Scheduled Railroad: IAS REQUIRED BY WRITTEN CONTRACT Designated Job Site: (If no entry appears above, information required to complete this endorsement will be shown in the Declarations as applicable to this endorsement.)',
    #     {"entities": [(272, 324, "SCHEDULED_TEXT:RAILROAD"), (325, 345, "SCHEDULED_TEXT:Designated Job Site")]}
    # ),