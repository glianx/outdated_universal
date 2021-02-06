import matplotlib.pyplot as plt
import random
import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from random import shuffle # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm      # a nice pretty percentage bar for tasks

DATADIR = "/Users/gordon/Downloads/flowers/Train"
CATEGORIES = ["rose", "sunflower"]

print('\nHow CNNs work (visualization): https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=UTz3y0GUkn50HM \n')
print('https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=JqvnzDCvxok2QM \n')
print('https://www.google.com/search?q=convolution+gif&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjbh-uluqnuAhUBMVkFHbxtChEQ_AUoAXoECA4QAw&biw=1280&bih=631#imgrc=FarHsk7CVirL8M \n')

#Image processing

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
        plt.imshow(img_array, cmap='gray')  # graph it
        #plt.show()  # display!

        break  # we just want one for now so break
    break  #...and one more!
print(img_array)
print(img_array.shape)

IMG_SIZE = 40 

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
#plt.show()

print(f'new array = {new_array}')
print(f'new array shape = {new_array.shape}')

training_data = []

def create_training_data():
    for category in CATEGORIES:  # do dogs and cats

        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat

        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass

create_training_data()

print(len(training_data))
print(f'training data shape = {np.array(training_data).shape}')

#print(training_data)

import random
random.shuffle(training_data)

for sample in training_data[:10]:
    print(sample[1])
    
X = []
y = []

for features,label in training_data:
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

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

#Convolutional Neural Network (CNN)

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
import pickle
import time

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0
print(len(training_data))
print(f'training data shape = {np.array(training_data).shape}')
model = Sequential()

model.add(Conv2D(1000, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
model.add(Conv2D(1000, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))


model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'],)

model.fit(np.array(X), np.array(y),batch_size=20,epochs=5,validation_split=0.1)
print(len(training_data))
print(f'training data shape = {np.array(training_data).shape}')
print('model training complete')

#saving model
#model.save('/Users/gordon/Downloads/flowersCNN')

#loading model
#from tensorflow import keras
#model = keras.models.load_model('/Users/gordon/Downloads/flowersCNN')

#testing with image

IMG_SIZE = 40
DATADIR = "/Users/gordon/Downloads/flowers/Test"
for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats

pet_li = ['rose','sunflower']
rose_predictions, rose_actual, sunflower_predictions, sunflower_actual, true_positives, true_negatives, false_positives, false_negatives = [0 for x in range(8)]


flowers = ['rose','sunflower']
for x in range(100):
    flower = random.choice(flowers)
    img = f'/Users/gordon/Downloads/flowers/{flower}/flower{x+1}.jpg'

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
    if prediction == 'sunflower':
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
            
print(f'dog_predictions, dog_actual, cat_predictions, cat_actual = {rose_predictions, rose_actual, sunflower_predictions, sunflower_actual}')
print(f'true positives = {true_positives}')
print(f'true negatives = {true_negatives}')
print(f'false positives = {false_positives}')
print(f'false negatives = {false_negatives}')
print(f'rose precision = {round(true_positives/(true_positives+false_positives),3)}')
print(f'sunflower precision = {round(true_negatives/(true_negatives+false_negatives),3)}')
print(f'rose recall = {round(true_positives/(true_positives+false_negatives),3)}')
print(f'sunflower recall = {round(true_negatives/(true_negatives+false_positives),3)}')
print(f'overall precision = {(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)}')
