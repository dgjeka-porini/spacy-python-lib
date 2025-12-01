# Introduction to spaCy

This section introduces the basics of using spaCy for natural language processing in Python.

## Example: Creating a spaCy Doc

```python
import spacy

nlp = spacy.blank("en")

doc = nlp('This is a sentence')

print(doc.text)
```

- `nlp` is the language model object.
- `doc` is the processed text as a spaCy Doc object.
- You can print the text of the Doc using `doc.text`.
