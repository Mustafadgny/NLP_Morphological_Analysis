"""
Morphological and Linguistic Analysis with spaCy
"""

import spacy

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Target sentence or phrase to analyze
word = "I go to schools"

# Process the text through the spaCy NLP pipeline
doc = nlp(word)

# Iterate over each token and print linguistic attributes
for token in doc:
    print(f"Text: {token.text}")                  # Raw token text
    print(f"Lemma: {token.lemma_}")              # Base form (lemma) of the word
    print(f"POS: {token.pos_}")                  # Coarse-grained part-of-speech tag
    print(f"Tag: {token.tag_}")                  # Fine-grained part-of-speech tag
    print(f"Dependency: {token.dep_}")           # Syntactic dependency relation
    print(f"Shape: {token.shape_}")              # Word shape (capitalization, digits, length)
    print(f"Is alpha: {token.is_alpha}")         # Checks if the token consists of alphabetic characters
    print(f"Is stop: {token.is_stop}")           # Checks if the token is a stop word
    print(f"Morphology: {token.morph}")          # Detailed morphological features
    print(f"Is plural: {'Number=Plur' in token.morph}") # Checks if the token has plural inflection
    print()