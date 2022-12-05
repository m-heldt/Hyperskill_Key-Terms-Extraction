# put your python code here
from nltk import word_tokenize
import nltk
from collections import Counter

# sentence = "The Tiber island is the only river island in the part of the Tiber which runs through Rome"
sentence = input()

tokenized = word_tokenize(sentence)
posed = nltk.pos_tag(tokenized)

counted = Counter([word[1] for word in posed])


print(counted.most_common(1)[0][0])
