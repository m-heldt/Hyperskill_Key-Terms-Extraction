import nltk


sent = ['The', 'horse', 'that', 'was', 'raced', 'past', 'the', 'barn', 'fell', 'down', '.']

tagged = nltk.pos_tag(sent)
print(tagged[4][1])
