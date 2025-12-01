# Predicting Part-of-Speech Tags with spaCy

spaCy can predict part-of-speech (POS) tags for each token in a text.

## Example: POS Tagging

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("She ate the pizza")

for token in doc:
    print(token.text, token.pos_)
```

- `token.pos_` returns the string label for the POS tag.
- Attributes ending with `_` return string values; without `_` return integer IDs.

## Example: Dependency Parsing

```python
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
```

| Label  | Description         | Example |
|--------|---------------------|---------|
| nsubj  | nominal subject     | She     |
| dobj   | direct object       | pizza   |
| det    | determiner (article)| the     |
