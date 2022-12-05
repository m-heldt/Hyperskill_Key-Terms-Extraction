import nltk


poem = ['Twinkle', ',', 'twinkle', ',', 'little', 'star', ',',
        'How', 'I', 'wonder', 'what', 'you', 'are', '.',
        'Up', 'above', 'the', 'world', 'so', 'high', ',',
        'Like', 'a', 'diamond', 'in', 'the', 'sky', '.']

posed = nltk.pos_tag(poem)
posed_nouns = [noun[0] for noun in posed if noun[1] == 'NN']

for noun in posed_nouns:
    print(noun)
