#  write your code here 
import spacy
from nltk.tokenize import word_tokenize

with open('input.txt', encoding='utf-8') as file:

    line = file.readline()

    nlp = spacy.load('el_core_news_sm')
    processed = nlp(line)


    founded = [word.text for word in processed if word.pos_ in ['NOUN', 'PROPN']]
    print(founded)
