# put your python code here
from nltk import word_tokenize
import nltk

sentence = input()

tokenized = word_tokenize(sentence)
posed = nltk.pos_tag(tokenized)

counting = {}
for token in posed:
    counting.setdefault(token[1], 0)
    counting[token[1]] += 1

print(counting)
