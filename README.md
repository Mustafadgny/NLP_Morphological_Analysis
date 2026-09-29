# 🔍 Morphological Analysis with spaCy

This repository demonstrates how to perform detailed linguistic and morphological analysis on text using the spaCy library in Python.

## 🚀 Key Features

The script inspects each token across several linguistic dimensions:
- Lemmatization (token.lemma_): Base dictionary form of the token.
- Part-of-Speech Tagging (token.pos_, token.tag_): Coarse and fine-grained grammatical category.
- Dependency Parsing (token.dep_): Syntactic role in the sentence.
- Morphological Analysis (token.morph): Grammatical features such as tense, case, and number (e.g., detecting plural nouns).
- Lexical Attributes: Checks whether tokens are alphabetic (token.is_alpha), stop words (token.is_stop), or follow specific casing shapes (token.shape_).

## 🛠️ Tech Stack
- Python
- spaCy
- en_core_web_sm model

## 💻 Installation & Setup

1. Install spaCy:
pip install spacy

2. Download the English language model:
python -m spacy download en_core_web_sm

3. Run the script:
python morphological_analysis.py

## 📊 Example Output

For the input sentence "I go to schools", the output for the token "schools":

Text: schools
Lemma: school
POS: NOUN
Tag: NNS
Dependency: pobj
Shape: xxxx
Is alpha: True
Is stop: False
Morfoloji: Number=Plur
Is plural: True
