import spacy

nlp = spacy.blank("en")

doc = nlp('This is a sentence')

print(doc.text)