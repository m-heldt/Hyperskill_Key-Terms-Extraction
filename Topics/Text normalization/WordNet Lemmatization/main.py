from nltk.stem import WordNetLemmatizer

lammer = WordNetLemmatizer()
poses = ['n', 'a', 'v']
word = input()
for posi in poses:
    print(lammer.lemmatize(word, pos=posi))
