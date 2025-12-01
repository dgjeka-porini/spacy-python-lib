# Pipeline Packages in spaCy

spaCy provides trained pipeline packages for different languages. These packages include models for tokenization, tagging, parsing, and more.

## Downloading a Pipeline Package

Use the following command to download a pipeline package:

```bash
python -m spacy download en_core_web_sm
```

## Loading a Pipeline Package

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

- The pipeline package contains binary weights, vocabulary, meta information, and configuration files.
- The `nlp` object is used to process text and make predictions.
