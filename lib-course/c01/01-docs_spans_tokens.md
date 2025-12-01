# Docs, Spans, and Tokens in spaCy

Learn about the main objects in spaCy: Doc, Token, and Span.

## Example: Slicing Docs

```python
import spacy

nlp = spacy.blank("en")

doc = nlp("I like tree kangaroos and narwhals.")

tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

tree_kangaroos_and_narwhals = doc[2:-1]
print(tree_kangaroos_and_narwhals.text)
```

- A **Doc** is a container for the processed text.
- A **Token** is a single word or punctuation.
- A **Span** is a slice of the Doc, representing a group of tokens.
