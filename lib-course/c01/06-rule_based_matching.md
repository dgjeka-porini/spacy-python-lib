
# Rule-based Matching in spaCy

## Why not just regular expressions?

Compared to regular expressions, spaCy's matcher works with `Doc` and `Token` objects instead of only strings. It's more flexible: you can search for texts, but also other lexical attributes, and even write rules that use a model's predictions.

> For example, you can find the word "duck" only if it's a verb, not a noun.

---

## Match Patterns

Match patterns are **lists of dictionaries**. Each dictionary describes one token. The keys are the names of token attributes, mapped to their expected values.

### Example: Match exact token texts
```python
[{"TEXT": "iPhone"}, {"TEXT": "X"}]
```

### Example: Match lexical attributes
```python
[{"LOWER": "iphone"}, {"LOWER": "x"}]
```

### Example: Match any token attributes
```python
[{"LEMMA": "buy"}, {"POS": "NOUN"}]
```

- **Lists of dictionaries:** one per token
- **Flexible matching:** exact text, lexical attributes, or model predictions
