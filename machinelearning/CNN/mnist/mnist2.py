#works successfully, returns label as int, not one-hot encoding
import keras
from keras import layers
import tensorflow as tf
from icecream import ic
import numpy as np
# Get the data as Numpy arrays
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Build a simple model
inputs = keras.Input(shape=(28, 28))
x = layers.experimental.preprocessing.Rescaling(1.0 / 255)(inputs)
x = layers.Flatten()(x)
x = layers.Dense(128, activation="relu")(x)
x = layers.Dense(128, activation="relu")(x)
outputs = layers.Dense(10, activation="softmax")(x)
model = keras.Model(inputs, outputs)
model.summary()

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")

# Train the model for 1 epoch from Numpy data
batch_size = 64
print("Fit on NumPy data")
model.fit(x_train, y_train, batch_size=batch_size, epochs=1)

# Train the model for 1 epoch using a dataset
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size)
print("Fit on Dataset")
model.fit(dataset, epochs=1)

predictions = model.predict(x_test[:100])
labels = y_test[:100]

ic(predictions.shape)

ic(labels.shape)
ic(labels)

right, wrong = 0,0

for prediction,label in zip(predictions,labels):
    #ic(prediction)
    a = np.argmax(prediction)
    ic(np.argmax(prediction),label,a==label)
    if np.argmax(prediction) == label:
        right += 1
    else:
        wrong += 1
ic(right,wrong,right/(right+wrong))
    #ic(list(test_labels).index(1))

predictions = model.predict(x_test[:3])
ic(predictions)

from sklearn.metrics import classification_report

y_pred = model.predict(x_test, batch_size=64, verbose=1)
y_pred_bool = np.argmax(y_pred, axis=1)
target_names = [f'class {x}' for x in range(10)]
print('\n',classification_report(y_test, y_pred_bool, target_names=target_names))