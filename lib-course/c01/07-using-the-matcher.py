'''
To use a pattern, we first import the matcher from spacy.matcher.

We also load a pipeline and create the nlp object.

The matcher is initialized with the shared vocabulary, nlp.vocab. You'll learn more about this later – for now, just remember to always pass it in.

The matcher.add method lets you add a pattern. The first argument is a unique ID to identify which pattern was matched. The second argument is a list of patterns.

To match the pattern on a text, we can call the matcher on any doc.

This will return the matches.
'''

import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)

'''
When you call the matcher on a doc, it returns a list of tuples.

Each tuple consists of three values: the match ID, the start index and the end index of the matched span.

This means we can iterate over the matches and create a Span object: a slice of the doc at the start and end index.
'''