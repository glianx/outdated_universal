#not working yet
import keras
import tensorflow as tf
import numpy as np
import os
from icecream import ic
from keras import layers

Dir = os.path.join(os.path.dirname(__file__), 'PetImages/Train')

training_dataset = tf.keras.preprocessing.image_dataset_from_directory(Dir, labels='inferred', batch_size=5,image_size=(50,50), color_mode='rgb')                    
ic(training_dataset)

for images, labels in training_dataset.take(1):  # only take first element of dataset
    ic(images.shape) #ic(images.numpy())
    ic(labels.numpy())

image = tf.keras.preprocessing.image.load_img(os.path.join(Dir, 'Dog/8.jpg'))
input_arr = keras.preprocessing.image.img_to_array(image)
input_arr = np.array([input_arr])  # Convert single image to a batch.
#ic(input_arr)
ic(input_arr.shape)

import cv2

img = cv2.imread(os.path.join(Dir, 'Dog/8.jpg'))
res = cv2.resize(img, dsize=(50,50), interpolation=cv2.INTER_CUBIC)

ic(res.shape)