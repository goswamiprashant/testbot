# Libraries needed for NLP
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# Libraries needed for Tensorflow processing
import tensorflow as tf
import numpy as np
import tflearn
import random
import json

# import our chat-bot intents file
with open('intents.json') as json_data:
    intents = json.load(json_data)

intents

words = []
classes = []
documents = []
ignore = ['?']
# loop through each sentence in the intent's patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each and every word in the sentence
        w = nltk.word_tokenize(pattern)
        # add word to the words list
        words.extend(w)
        # add word(s) to documents
        documents.append((w, intent['tag']))
        # add tags to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(words)
print(classes)


