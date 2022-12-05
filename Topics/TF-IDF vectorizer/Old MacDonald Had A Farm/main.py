#  write your code here 
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(input='file', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1),
                             stop_words=None)

filename = 'input.txt'

with open(filename) as file:
    X = vectorizer.fit_transform([file])
    X_array = X.toarray()
    print(X)
