#works sometimes, corrupt images
#channel error, input error
import keras
import tensorflow as tf
import numpy as np
import os
from icecream import ic
# Create a dataset.

Dir = (os.path.join(os.path.dirname(__file__), 'PetImages/Train'))
ic(Dir)

dataset = keras.preprocessing.image_dataset_from_directory(
    Dir, batch_size=32, image_size=(50,50))

ic(dataset)

# For demonstration, iterate over the batches yielded by the dataset.

for data, labels in dataset:
   ic(data.shape)  
   ic(data.dtype)  # float32
   ic(labels.shape)  
   ic(labels.dtype)  # int32
   ic(data)
   ic(labels)
   break

from tensorflow.keras.layers.experimental.preprocessing import Normalization

# Example image data, with values in the [0, 255] range

normalizer = Normalization(axis=-1)
normalizer.adapt(data)

normalized_data = normalizer(data)
ic(np.var(normalized_data))
ic(np.mean(normalized_data))

from tensorflow.keras.layers.experimental.preprocessing import CenterCrop
from tensorflow.keras.layers.experimental.preprocessing import Rescaling

# Example image data, with values in the [0, 255] range

cropper = CenterCrop(height=50, width=50)
scaler = Rescaling(scale=1.0 / 255)

output_data = scaler(cropper(data))
ic(output_data.shape)
ic(np.min(output_data))
ic(np.max(output_data))

# Let's say we expect our inputs to be RGB images of arbitrary size
inputs = keras.Input(shape=(None, None, 3))

from tensorflow.keras import layers

# Center-crop images to 150x150
x = CenterCrop(height=50, width=50)(inputs)
# Rescale images to [0, 1]
x = Rescaling(scale=1.0 / 255)(x)


# Apply some convolution and pooling layers
x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3, 3))(x)
x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)
x = layers.MaxPooling2D(pool_size=(3, 3))(x)
x = layers.Conv2D(filters=32, kernel_size=(3, 3), activation="relu")(x)

# Apply global average pooling to get flat feature vectors
x = layers.GlobalAveragePooling2D()(x)

# Add a dense classifier on top
num_classes = 1
outputs = layers.Dense(num_classes, activation="sigmoid")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy')

model.fit(dataset, epochs=10)