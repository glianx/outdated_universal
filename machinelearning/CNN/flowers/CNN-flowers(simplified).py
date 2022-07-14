import matplotlib.pyplot as plt
import random
import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks

DATADIR = "/Users/gordon/Downloads/flowers/Test"
CATEGORIES = ["rose", "sunflower"]

print('\nHow CNNs work (visualization): https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=UTz3y0GUkn50HM \n')
print('https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=JqvnzDCvxok2QM \n')
print('https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=FarHsk7CVirL8M \n')

import pickle

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

#Convolutional Neural Network (CNN)

#saving model
#model.save('/Users/gordon/Downloads/flowersCNN')
#loading model
from tensorflow import keras
model = keras.models.load_model('/Users/gordon/Downloads/flowersCNN')

#testing with image

IMG_SIZE = 40
DATADIR = "/Users/gordon/Downloads/flowers"
for category in CATEGORIES: 
    path = os.path.join(DATADIR,category) 

pet_li = ['rose','sunflower']
rose_predictions, rose_actual, sunflower_predictions, sunflower_actual, true_positives, true_negatives, false_positives, false_negatives = [0 for x in range(8)]


flowers = ['rose','sunflower']
for x in range(100):
    flower = random.choice(flowers)
    if flower == 'rose':
        start_val = 669
    elif flower == 'sunflower':
        start_val = 626
    img = f'/Users/gordon/Downloads/flowers/Test/{flower}/flower{x+start_val}.jpg'

    #processing image
    test_image = cv2.resize(cv2.imread(img, cv2.IMREAD_GRAYSCALE),  (IMG_SIZE,IMG_SIZE))
    test_image = np.array(test_image).reshape( -1, IMG_SIZE, IMG_SIZE, 1)

    #print(model.predict(test_image),[[pet_li.index(flower)]]) #returns index [[0.]] or [[1.]]
    prediction = CATEGORIES[int(model.predict(test_image))]
    print(f'{img} prediction = {prediction}')
    if flower == 'rose':
        rose_actual += 1
    else:
        sunflower_actual += 1
    if prediction == 'rose':
        rose_predictions += 1
    else: 
        sunflower_predictions += 1
    if prediction == flower: #correct prediction
        if flower == 'rose':
            true_positives += 1
        else:
            true_negatives += 1
    else: #wrong prediction
        if prediction == 'rose':
            false_positives += 1
        else:
            false_negatives += 1
            
print(f'rose_predictions, rose_actual, sunflower_predictions, sunflower_actual = '
      f'{rose_predictions, rose_actual, sunflower_predictions, sunflower_actual}')
print(f'true positives = {true_positives}')
print(f'true negatives = {true_negatives}')
print(f'false positives = {false_positives}')
print(f'false negatives = {false_negatives}')
print(f'rose precision = {round(true_positives/(true_positives+false_positives),3)}')
print(f'sunflower precision = {round(true_negatives/(true_negatives+false_negatives),3)}')
print(f'rose recall = {round(true_positives/(true_positives+false_negatives),3)}')
print(f'sunflower recall = {round(true_negatives/(true_negatives+false_positives),3)}')
print(f'overall precision = {(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)}')