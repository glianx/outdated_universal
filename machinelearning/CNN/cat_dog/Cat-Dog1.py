import matplotlib.pyplot as plt
import random
import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks
from icecream import ic

dirname = os.path.dirname(__file__)
DATADIR = os.path.join(dirname, "PetImages/Train/")

ic(dirname,DATADIR)

CATEGORIES = ["Dog", "Cat"]

#Image processing

IMG_SIZE = 40

training_data = []
X = []
y = []
def create_training_data():
    for category in CATEGORIES:  # do dogs and cats
        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat
        
        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                #training_data.append([new_array, class_num])  # add this to our training_data
                X.append(new_array)
                y.append(class_num)
            except Exception as e:
                ic(e)
                break
        
            

create_training_data()

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
 
# =============================================================
  
#save images

import pickle

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

 
# =============================================================
  
import tensorflow as tf
#from tensorflow.keras.datasets import cifar10
#from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import pickle
import time

NAME = "Cats-vs-dogs-CNN"

X = X/255.0

# =============================================================
  
#Convolutional Neural Network (CNN)

model = Sequential()

model.add(Conv2D(256, (4,4), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
model.add(Conv2D(256, (4,4)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))



model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'],)

model.fit(np.array(X), np.array(y),batch_size=20,epochs=1,validation_split=0.1)

 
# =============================================================
  


#saving model
#model.save('/Users/gordon/Downloads/TensorflowCNN')
#loading model
from tensorflow import keras
model = keras.models.load_model('/Users/gordon/Downloads/TensorflowCNN')

 
# =============================================================
  

#testing with image

dirname = os.path.dirname(__file__)
DATADIR = os.path.join(dirname, 'PetImages/Test')

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats

pet_li = ['Dog','Cat']
dog_predictions, dog_actual, cat_predictions, cat_actual, true_positives, true_negatives, false_positives, false_negatives = [0 for x in range(8)]
 
# =============================================================
predictions = model.predict(X[:10])
ic(predictions)

for x in range(100):
    truepet = random.choice(pet_li)
    img = os.path.join(DATADIR, truepet, f'{12400+x}.jpg')
    #processing image
    test_image = cv2.resize(cv2.imread(img, cv2.IMREAD_GRAYSCALE),  (IMG_SIZE,IMG_SIZE))
    test_image = np.array(test_image).reshape( -1, IMG_SIZE, IMG_SIZE, 1)
    
    prediction = CATEGORIES[int(model.predict(test_image))]
    if truepet == 'Dog':
        dog_actual += 1
    else:
        cat_actual += 1
    if prediction == 'Dog':
        dog_predictions += 1
    else: 
        cat_predictions += 1
    if prediction == truepet: #correct prediction
        if truepet == 'Dog':
            true_positives += 1
        else:
            true_negatives += 1
    else:                           #wrong prediction
        if prediction == 'Dog':
            false_positives += 1
        else:
            false_negatives += 1
            
    ic(truepet,prediction,truepet == prediction) #intuitive answer (returns string)
        
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

 
