# Predicting Named Entities with spaCy

Named entities are real-world objects assigned a name, such as a person, organization, or country.

## Example: Named Entity Recognition

```python
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)
```

- `doc.ents` returns an iterator of Span objects for named entities.
- `ent.label_` gives the entity type as a string.

## Tip: Explain Entity Labels

Use `spacy.explain` to get definitions for tags and labels:

```python
spacy.explain("GPE")  # Geopolitical entity: countries, cities, states
```
