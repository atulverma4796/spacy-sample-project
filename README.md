## Training the Spacy Model


## Generate config.cfg file in the same folder
python3 -m spacy init fill-config base_config.cfg config.cfg

## In order to train existing Spacy model with new parameters, we will execute below command from cmd or terminal
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy