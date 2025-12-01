'''
spaCy provides a number of trained pipeline packages you can download using the spacy download command. 
For example, the "en_core_web_sm" package is a small English pipeline that supports all core capabilities 
and is trained on web text.

The spacy.load method loads a pipeline package by name and returns an nlp object.

The package provides the binary weights that enable spaCy to make predictions.

It also includes the vocabulary, meta information about the pipeline and the configuration file used to train it. 
It tells spaCy which language class to use and how to configure the processing pipeline.


command: python -m spacy download en_core_web_sm
'''
import spacy

nlp = spacy.load("en_core_web_sm")

