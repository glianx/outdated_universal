import matplotlib.pyplot as plt
from tensorflow import keras
#import keras_metrics
from tensorflow.python.keras.metrics import Metric
import random
import cv2                 # working with, mainly resizing, images
import numpy as np         # dealing with arrays
import os                  # dealing with directories
from tqdm import tqdm      # a nice pretty percentage bar for tasks
from icecream import ic
from tensorflow import keras
import tensorflow as tf
dirname = os.path.dirname(__file__)
TRAIN_DIR = os.path.join(dirname, "PetImages/Train/")

CATEGORIES = ["Dog", "Cat"]

#Image processing

IMG_SIZE = 40
epochs = 10
training_data = []
X = []
y = []


for category in CATEGORIES:  
    sub_dir = os.path.join(TRAIN_DIR,category)  
    x = 0
    for img_name in tqdm(os.listdir(sub_dir)): 
        x += 1
        #if x > 2000: break
        try:
            img = keras.preprocessing.image.load_img(
                os.path.join(sub_dir,img_name), target_size=(IMG_SIZE,IMG_SIZE), color_mode='grayscale'
            )
            img_array = keras.preprocessing.image.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0)
            
            X.append(img_array)
            y.append(CATEGORIES.index(category))
        except Exception as e:
            #ic(e)
            pass
            

        #img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
        #new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size

#X,y are lists
ic(type(X),type(y))      

#convert X,y to np arrays
X = np.array(X)          
y = np.array(y)
ic(type(X),type(y),X.shape)     

#reshape X from (None, 1, IMG_SIZE, IMG_SIZE, 1) to (None, IMG_SIZE, IMG_SIZE, 1)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) 
ic(X.shape,y.shape,y[:10])     

#shuffle X,y in unison
p = np.random.permutation(len(y)) 
X = X[p]
y = y[p]

ic(y[:10])     
ic(y)
# =============================================================

#save images
'''
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
'''
# =============================================================

import tensorflow as tf
#from tensorflow.keras.datasets import cifar10
#from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
#import pickle
import time

NAME = "Cats-vs-dogs-CNN"

X = X/255.0

# =============================================================
  
#Convolutional Neural Network (CNN)

model = Sequential()

model.add(Conv2D(256, kernel_size = (3,3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
 
model.add(Conv2D(256, kernel_size = (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy']) #metrics=[keras.metrics.Precision(), keras.metrics.Recall()]

model.summary()

history = model.fit(np.array(X), np.array(y),batch_size=32,epochs=epochs,validation_split=0.2)

 
# =============================================================
  


#saving model
#model.save('/Users/gordon/Downloads/TensorflowCNN')
#loading model
from tensorflow import keras
#model = keras.models.load_model('/Users/gordon/Downloads/TensorflowCNN')

 
# =============================================================
  

#testing with image

dirname = os.path.dirname(__file__)
test_dir = os.path.join(dirname, 'PetImages/Test')

pet_li = ['Dog','Cat']
dog_predictions, dog_actual, cat_predictions, cat_actual, true_positives,\
true_negatives, false_positives, false_negatives = [0 for x in range(8)]
right,wrong = 0,0
# =============================================================
ic(model.predict(X[:10]))
ic(y[:10])
for i in CATEGORIES:
    for img_name in os.listdir(os.path.join(test_dir,i)):

        img = keras.preprocessing.image.load_img(
            os.path.join(test_dir,i,img_name), target_size=(IMG_SIZE,IMG_SIZE), color_mode='grayscale'
        )

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis

        predictions = model.predict(img_array)
        score = predictions[0]
        #print(
        #    f"This image is {(100 * (1 - score))} percent cat and {100 * score} percent dog."
        #)
        cat = int(100 * (1 - score))
        dog = int(100 * score)

        p = CATEGORIES[(cat,dog).index(max(cat,dog))]
        if p == i: #correct prediction
            if i == 'Dog':
                dog_actual += 1
                true_positives += 1
                dog_predictions += 1
            else:
                true_negatives += 1
                cat_predictions += 1
                cat_actual += 1
        else:                           #wrong prediction
            if p == 'Dog':
                false_positives += 1
                dog_predictions += 1
                cat_actual += 1
            else:
                false_negatives += 1
                cat_predictions += 1
                dog_actual += 1
        
        ic(i,p,i == p) 
        
ic(dog_predictions, dog_actual, cat_predictions, cat_actual)
ic(true_positives)
ic(true_negatives)
ic(false_positives)
ic(false_negatives)

dog_precision = round(true_positives/(true_positives+false_positives),3)
cat_precision = round(true_negatives/(true_negatives+false_negatives),3)
dog_recall = round(true_positives/(true_positives+false_negatives),3)
cat_recall = round(true_negatives/(true_negatives+false_positives),3)
dog_F1 = round(2*((dog_precision*dog_recall)/(dog_precision+dog_recall)),3)
cat_F1 = round(2*((cat_precision*cat_recall)/(cat_precision+cat_recall)),3)
#F1 score
#2*((precision*recall)/(precision+recall))

overall_precision = round((true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives),3)

ic(dog_precision)
ic(cat_precision)
ic(dog_recall)
ic(cat_recall)
ic(dog_F1)
ic(cat_F1)

ic(overall_precision)
#print(f'dog precision = {round(true_positives/(true_positives+false_positives),3)}')
#print(f'cat precision = {round(true_negatives/(true_negatives+false_negatives),3)}')
#print(f'dog recall = {round(true_positives/(true_positives+false_negatives),3)}')
#print(f'cat recall = {round(true_negatives/(true_negatives+false_positives),3)}')
#print(f'overall precision = {(true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)}')

print()


X_test = []
y_test = []

for i in CATEGORIES:
    for img_name in os.listdir(os.path.join(test_dir,i)):
        img = keras.preprocessing.image.load_img(
            os.path.join(test_dir,i,img_name), target_size=(IMG_SIZE,IMG_SIZE), color_mode='grayscale'
        )

        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        X_test.append(img_array)
        y_test.append(CATEGORIES.index(i))
        
ic(type(X_test),type(y_test))

X_test = np.array(X_test)

ic(type(X_test),type(y_test),X_test.shape)

X_test = np.array(X_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
X_test = X_test/255.0
y_test = np.array(y_test)

ic(type(X_test),type(y_test),X_test.shape,y_test.shape)

evaluation = model.evaluate(X_test, y_test, batch_size = 32)
print("Test loss:", evaluation[0])
print("Test accuracy:", evaluation[1])

# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy

ic(model.predict(X_test[:10]))
ic(y_test[:10])

for metric in ('accuracy','precision','recall','loss'):
    ic(metric,'val_' + metric,'model ' + metric)
    plt.plot(history.history[metric]) #i.e. ['accuracy']
    plt.plot(history.history['val_' + metric]) #i.e.['val_accuracy']
    plt.title('model ' + metric) #i.e. 'model accuracy'
    plt.ylabel(metric) #i.e. 'accuracy'
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
'''
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
'''

from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test, y_score)

print('Average precision-recall score: {0:0.2f}'.format(
    average_precision))

