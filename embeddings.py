# Implement Skipgram model for word embeddings using Keras and NLTK

import nltk
nltk.download('punkt')
nltk.download('stopwords')

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
from nltk.tokenize import word_tokenize
# Tokenize sentence
tokens = word_tokenize(text)
vocabulary = list(set(tokens))

import numpy as np
from keras.utils import Sequence
class SkipGramGenerator(Sequence):
  def __init__(self, tokens, vocabulary, batch_size):
    self.tokens = tokens
    self.vocabulary = vocabulary
    self.batch_size = batch_size
    self.on_epoch_end()
  def __len__(self):
    return (len(self.tokens) - 2) // self.batch_size
  def __getitem__(self, index):
    x = np.zeros((self.batch_size, len(self.vocabulary)))
    y = np.zeros((self.batch_size, len(self.vocabulary)))
    for i in range(self.batch_size):
      x[i, self.vocabulary.index(self.tokens[i + index + 1])] = 1.0
      y[i, self.vocabulary.index(self.tokens[i + index])] = 1.0
      y[i, self.vocabulary.index(self.tokens[i + index + 2])] = 1.0
    return x, y

from keras.models import Sequential
from keras.layers import Dense
embedding_size = 10
model = Sequential()
model.add(Dense(embedding_size, input_shape=(len(vocabulary),),
               activation='relu'))
model.add(Dense(len(vocabulary), activation='sigmoid'))
model.compile(optimizer='sgd', loss='binary_crossentropy')

model.fit_generator(training_generator, epochs=100)
