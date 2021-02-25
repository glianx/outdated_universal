#works successfully
# ===== DeepDev | Initialization ===== hh#
from icecream import ic
import ssl

_create_unverified_https_context = ssl._create_unverified_context

#Imports
import keras
from keras import backend as K
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import *
from keras.metrics import *
from keras.utils import to_categorical
from keras.utils import np_utils
import numpy as np
import tensorflow as tf

# ===== DeepDev | Stage 1: Load ===== #

# --- Dataset --- #
from keras.datasets import mnist
(training_features, training_labels), (test_features, test_labels) = mnist.load_data()
# --- Preprocessing --- #
#Shaping
training_features = training_features.reshape(60000, 784)
test_features = test_features.reshape(10000, 784)

#One-Hot-Encoding
training_labels = np_utils.to_categorical(training_labels, 10)
test_labels = np_utils.to_categorical(test_labels, 10)

#Normalization
training_features = training_features.astype('float32')
test_features = test_features.astype('float32')
training_features /= 255
test_features /= 255

# ===== DeepDev | Stage 2: Build ===== #

# --- Initialize --- #
model = Sequential()

# --- Layers --- #
model.add(Dense(256, input_shape = (784, ), activation='relu'))
model.add(Dense(10, activation='softmax'))


# ===== DeepDev | Stage 3: Train ===== #

# --- Compilation --- #
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# --- Training --- #
history = model.fit(x=training_features, y=training_labels, validation_split=0.2, batch_size=128, epochs=5, verbose=1, shuffle=True)


# ===== DeepDev | Exporting the Model ===== #

#Export to JSON
#model_json = model.to_json()
#with open("model.json", "w") as json_file:
#    json_file.write(model_json)

#Export to h5
#model.save('model.h5')

#=========== Predictions ================#

model = keras.models.load_model('model.h5')

right, wrong = 0,0

predictions = model.predict(test_features[:10])
labels = test_labels[:10]

ic(predictions.shape)
ic(predictions)

ic(labels.shape)
ic(labels)

for prediction,label in zip(predictions,labels):
    #ic(prediction)
    a = np.argmax(prediction)
    b = np.argmax(label)
    ic(np.argmax(prediction),np.argmax(label),a==b)
    if np.argmax(prediction) == np.argmax(label):
        right += 1
    else:
        wrong += 1
ic(right,wrong,right/(right+wrong))

# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy


# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()