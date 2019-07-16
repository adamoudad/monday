import numpy as np

from keras.datasets import mnist

(train_samples, train_labels), (test_samples, test_labels) = mnist.load_data()

# Normalize data
def normalize_samples(samples):
    return np.expand_dims( samples.astype('float') / 255. , axis=-1)

train_samples = normalize_samples(train_samples)
test_samples = normalize_samples(test_samples)

from keras.models import Sequential
from keras.layers import Dense, Conv2D

model = Sequential()
model.add(Conv2D(32, 3, padding='same', activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, 3, padding='same', activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(10))

