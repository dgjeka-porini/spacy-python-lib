# Using the Matcher in spaCy

The Matcher lets you find sequences of tokens based on patterns.

## Example: Using Matcher

```python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

doc = nlp("Upcoming iPhone X release date leaked")
matches = matcher(doc)

for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
```

- The matcher returns a list of tuples: (match ID, start index, end index).
- You can use these indices to create a Span object from the Doc.
