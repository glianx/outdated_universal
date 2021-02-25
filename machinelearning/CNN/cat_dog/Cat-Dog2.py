#simplified version uses the saved, pre-trained CNN model to save time
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
from icecream import ic
import tensorflow as tf

dirname = os.path.dirname(__file__)
test_dir = os.path.join(dirname, 'PetImages/Test')

CATEGORIES = ["Dog", "Cat"]

#this loads the model
from tensorflow import keras
model = keras.models.load_model('/Users/gordon/Downloads/Cat-Dog1')

#testing with image
IMG_SIZE = 40

# =============================================================

#testing with image

img = keras.preprocessing.image.load_img(
    os.path.join(test_dir,'Dog','12302.jpg'), target_size=(IMG_SIZE,IMG_SIZE), color_mode='grayscale'
)

img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)

score = predictions[0]

cat = int(100 * (1 - score))
dog = int(100 * score)

ic(predictions,score,cat,dog)