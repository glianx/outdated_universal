#simplified version uses the saved, pre-trained CNN model to save time
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random
from icecream import ic

dirname = os.path.dirname(__file__)
ic(dirname)
DATADIR = os.path.join(dirname, 'PetImages/Test')
ic(DATADIR)

CATEGORIES = ["Dog", "Cat"]

#this saves the image data
import pickle

#pickle_in = os.path.join(dirname, 'X.pickle')
pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

#this loads the model
from tensorflow import keras
model = keras.models.load_model('/Users/gordon/Downloads/TensorflowCNN')

#testing with image
IMG_SIZE = 40

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats

pet_li = ['Dog','Cat']
dog_predictions, dog_actual, cat_predictions, cat_actual, true_positives, true_negatives, false_positives, false_negatives = [0 for x in range(8)]


predictions = model.predict(X[:3])
ic(predictions)

for x in range(100):
    actualpet = random.choice(pet_li)
    img = os.path.join(DATADIR, actualpet, f'{12400+x}.jpg')
    #processing image
    test_image = cv2.resize(cv2.imread(img, cv2.IMREAD_GRAYSCALE),  (IMG_SIZE,IMG_SIZE))
    test_image = np.array(test_image).reshape( -1, IMG_SIZE, IMG_SIZE, 1)
    
    prediction = CATEGORIES[int(model.predict(test_image))]
    if actualpet == 'Dog':
        dog_actual += 1
    else:
        cat_actual += 1
    if prediction == 'Dog':
        dog_predictions += 1
    else: 
        cat_predictions += 1
    if prediction == actualpet: #correct prediction
        if actualpet == 'Dog':
            true_positives += 1
        else:
            true_negatives += 1
    else:                           #wrong prediction
        if prediction == 'Dog':
            false_positives += 1
        else:
            false_negatives += 1
            
    ic(img,prediction) #intuitive answer (returns string)
        
ic(dog_predictions, dog_actual, cat_predictions, cat_actual)
ic(true_positives)
ic(true_negatives)
ic(false_positives)
ic(false_negatives)
print(f'dog precision = {round(true_positives/(true_positives+false_positives),3)}')
print(f'cat precision = {round(true_negatives/(true_negatives+false_negatives),3)}')
print(f'dog recall = {round(true_positives/(true_positives+false_negatives),3)}')
print(f'cat recall = {round(true_negatives/(true_negatives+false_positives),3)}')
print(f'overall precision = {(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)}')


