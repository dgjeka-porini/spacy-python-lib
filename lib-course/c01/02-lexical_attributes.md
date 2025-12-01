# Lexical Attributes in spaCy

Lexical attributes provide information about tokens, such as their text, part-of-speech, lemma, and more.

## Example: Finding Percentages in Text

```python
import spacy

nlp = spacy.blank("en")

# Process the text
text = (
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)
doc = nlp(text)

# Iterate over the tokens in the doc
for i, token in enumerate(doc):
    # Check if the token resembles a number
    if token.like_num:
        # Get the next token in the document (if it exists)
        if i + 1 < len(doc):
            next_token = doc[i + 1]
            # Check if the next token's text equals "%"
            if next_token.text == "%":
                print("Percentage found:", token.text + next_token.text)
```

### Common Lexical Attributes
- `token.text`: The original text of the token
- `token.lemma_`: The base form of the token
- `token.pos_`: Part-of-speech tag
- `token.like_num`: Boolean, does the token resemble a number?
- `token.is_alpha`: Boolean, is the token an alphabetic word?
- `token.is_punct`: Boolean, is the token punctuation?

---

*Use lexical attributes to extract structured information from text efficiently!*