import numpy as np

from keras.datasets import mnist

(train_samples, train_labels), (test_samples, test_labels) = mnist.load_data()

# Normalize data
def normalize_samples(samples):
    return np.expand_dims( samples.astype('float') / 255. , axis=-1)

train_samples = normalize_samples(train_samples)
test_samples = normalize_samples(test_samples)

input_shape = train_samples.shape[1:]

from keras.models import Model
from keras.layers import Dense, Conv2D, Input, Lambda, Flatten, Reshape
import keras.backend as K

def sampling(args):
    z_mean, z_log_var = args
    batch_size = K.shape(z_mean)[0]
    latent_dimension = K.int_shape(z_mean)[1]
    epsilon = K.random_normal(shape=(batch_size, latent_dimension))
    return z_mean + K.exp(0.5 * z_log_var) * epsilon

latent_dimension = 20

inputs = Input(shape=input_shape, name='encoder_input')
x = Flatten()(inputs)
x = Dense(512, activation='relu')(x)
z_mean = Dense(latent_dimension, name='z_mean')(x)
z_log_var = Dense(latent_dimension, name='z_log_var')(x)
z = Lambda(sampling, output_shape=(latent_dimension,), name='z')([z_mean, z_log_var])

encoder = Model(inputs, [z_mean, z_log_var, z], name='encoder')

latent_inputs = Input(shape=(latent_dimension,), name='z_sampling')
x = Dense(512, activation='relu')(latent_inputs)
outputs = Dense(np.product(input_shape), activation='sigmoid')(x)
outputs = Reshape(input_shape)(outputs)

decoder = Model(latent_inputs, outputs, name='decoder')

outputs = decoder(encoder(inputs)[2])
vae = Model(inputs, outputs, name='vae_mlp')

from keras.losses import binary_crossentropy

reconstruction_loss = binary_crossentropy(inputs, outputs)
reconstruction_loss *= np.product(input_shape)
kl_loss = 1 + z_log_var - K.square(z_mean) - K.exp(z_log_var)
kl_loss = -0.5 * K.sum(kl_loss, axis=-1)
vae_loss = K.mean(reconstruction_loss + kl_loss)
vae.add_loss(vae_loss)
vae.compile(optimizer='adam')
# model.add(Conv2D(32, 3, padding='same', activation='relu', input_shape=(28, 28, 1)))
# model.add(Conv2D(64, 3, padding='same', activation='relu'))
# model.add(Dense(32, activation='relu'))
# model.add(Dense(10))


