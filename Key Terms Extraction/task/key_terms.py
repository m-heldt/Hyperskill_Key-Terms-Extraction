from lxml import etree
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import string
from operator import itemgetter
from sklearn.feature_extraction.text import TfidfVectorizer

# defining a helper class
class NewsParser(object):
    def __init__(self, xml_file_path):
        self.tree = etree.parse(xml_file_path)
        self.root = self.tree.getroot()
        self.corpus = self.root[0]

    def get_headers(self):
        return [news[0].text for news in self.corpus]

    def get_stories(self):
        return [news[1].text for news in self.corpus]

xml_path = 'news.xml'

# tokenization
news = NewsParser(xml_path)
headers = news.get_headers()
stories = news.get_stories()
stories_tokenized = [word_tokenize(story.lower()) for story in stories]

# lemmatization and deleting punctation and stopwords
lemmatizer = WordNetLemmatizer()
stories_lemmatized = []
for story in stories_tokenized:
    new_story = [lemmatizer.lemmatize(word) for word in story]
    stories_lemmatized.append(new_story)

puncts = list(string.punctuation)
puncts.extend(stopwords.words('english'))

stories_depuncted = []
for story in stories_lemmatized:
    new_story = [token for token in story if token not in puncts and nltk.pos_tag([token])[0][1] == "NN"]
    stories_depuncted.append(new_story)

# preparing input for tf-ifd vectorization
corpus = [' '.join(story) for story in stories_depuncted]

# tf-ifd vectorizarion
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
words = vectorizer.get_feature_names_out()
X_array = X.toarray()

# analysing the results of vectorization
zipped_stories = [list(zip(words, story)) for story in X_array]
sorted_stories = [sorted(story, key=itemgetter(1,0), reverse=True) for story in zipped_stories]

# printing the results
for header, story in zip(headers, sorted_stories):
    print(f"{header}:")
    words = [word[0] for word in story]
    print(" ".join(words[0:5]))
    print()


