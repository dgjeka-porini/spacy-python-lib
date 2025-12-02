
# Using operators and quantifiers in spaCy Matcher

Operators and quantifiers let you define how often a token should be matched in a pattern. They are added using the `"OP"` key.

## Example: Using operators and quantifiers

```python
pattern = [
	{"LEMMA": "buy"},
	{"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
	{"POS": "NOUN"}
]

doc = nlp("I bought a smartphone. Now I'm buying apps.")
matcher = Matcher(nlp.vocab)
matcher.add("BUY_PATTERN", [pattern])
matches = matcher(doc)

for match_id, start, end in matches:
	print(doc[start:end].text)
```

Output:
```
bought a smartphone
buying apps
```

Operators and quantifiers let you define how often a token should be matched. They can be added using the `"OP"` key.

Here, the `?` operator makes the determiner token optional, so it will match a token with the lemma "buy", an optional article, and a noun.

---

## Operator values

| Example           | Description                  |
|-------------------|-----------------------------|
| {"OP": "!"}      | Negation: match 0 times      |
| {"OP": "?"}      | Optional: match 0 or 1 times |
| {"OP": "+"}      | Match 1 or more times        |
| {"OP": "*"}      | Match 0 or more times        |

`"OP"` can have one of four values:

- `!` negates the token, so it's matched 0 times.
- `?` makes the token optional, and matches it 0 or 1 times.
- `+` matches a token 1 or more times.
- `*` matches 0 or more times.

Operators can make your patterns a lot more powerful, but they also add more complexity – so use them wisely.
