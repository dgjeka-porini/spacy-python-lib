'''
Named entities are "real world objects" that are assigned a name – for example, a person, an organization or a country.

The doc.ents property lets you access the named entities predicted by the named entity recognition model.

It returns an iterator of Span objects, so we can print the entity text and the entity label using the .label_ attribute.

In this case, the model is correctly predicting "Apple" as an organization, 
"U.K." as a geopolitical entity and "$1 billion" as money.
'''

import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

'''
TIP: the spacy.explain method

A quick tip: To get definitions for the most common tags and labels, you can use the spacy.explain helper function.

For example, "GPE" for geopolitical entity isn't exactly intuitive – but spacy.explain can tell you that it refers to countries, cities and states.

The same works for part-of-speech tags and dependency labels.
'''

