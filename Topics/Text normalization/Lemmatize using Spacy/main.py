#  write your code here
file_path = r"C:\Users\mateu\PycharmProjects\Key Terms Extraction\Topics\Text normalization\Lemmatize using Spacy\data\dataset\input.txt"

from nltk.tokenize import word_tokenize
import spacy

nlp = spacy.load('en_core_web_sm')

tokens = []
with open(file_path) as file:
    for line in file:
        text = nlp(line)
        tokens.extend([word.lemma_ for word in text])
print(" ".join(tokens))


