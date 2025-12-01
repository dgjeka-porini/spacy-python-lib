'''
Let's take a look at the model's predictions. In this example, we're using spaCy to predict part-of-speech tags, 
the word types in context.

First, we load the small English pipeline and receive an nlp object.

Next, we're processing the text "She ate the pizza".

For each token in the doc, we can print the text and the .pos_ attribute, the predicted part-of-speech tag.

In spaCy, attributes that return strings usually end with an underscore – attributes without the underscore return 
an integer ID value.

Here, the model correctly predicted "ate" as a verb and "pizza" as a noun.
'''

import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)


'''
In addition to the part-of-speech tags, we can also predict how the words are related. 
For example, whether a word is the subject of the sentence or an object.

The .dep_ attribute returns the predicted dependency label.

The .head attribute returns the syntactic head token. You can also think of it as the parent token this word is attached to.
'''

for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)


'''
Label	  Description	           Example
-----------------------------------------------
nsubj	  nominal subject	       She
dobj	  direct object	           pizza
det	      determiner (article)	   the
'''