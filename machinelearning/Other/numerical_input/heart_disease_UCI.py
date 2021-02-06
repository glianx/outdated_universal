import numpy as np
from numpy import loadtxt
import keras
from keras.layers import Dense
from keras.models import Sequential
import os
from icecream import ic

dirname = os.path.dirname(__file__)
DATASET_PATH = os.path.join(dirname, "heart.csv")

EPOCHS = 50
#ic(dirname,DATASET_PATH)
#dataset = loadtxt(DATASET_PATH, delimiter=',')
#ic(dataset)

import sys
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import keras

DATASET = pd.read_csv(DATASET_PATH)

ic(DATASET.shape)
ic(DATASET[:2])
ic(type(DATASET))

# remove missing data (indicated with a "?")
data = DATASET[~DATASET.isin(['?'])]
#print(data.loc[280:])

# drop rows with NaN values from DataFrame
data = data.dropna(axis=0)
#print(data.loc[280:])

# print the shape and data type of the dataframe
ic(data.shape)
ic(data.dtypes)

# transform data to numeric to enable further analysis
data = data.apply(pd.to_numeric)

# print data characteristics, usings pandas built-in describe() function
print(data.describe())
ic(type(data), type(data.describe()))

ic(DATASET.loc[:2])

X = np.array(data.drop(['target'], 1))
y = np.array(data['target'])

ic(X[0])

mean = X.mean(axis=0)
X -= mean
std = X.std(axis=0)
X /= std

ic(X[0])
ic(type(X),type(y),X.shape,y.shape)


from sklearn import model_selection

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, stratify=y, random_state=42, test_size = 0.2)

# convert the data to categorical labels
from keras.utils.np_utils import to_categorical

Y_train = to_categorical(y_train, num_classes=None)
Y_test = to_categorical(y_test, num_classes=None)
print (Y_train.shape)
print (Y_train[:10])

for x in (X_train, X_test, y_train, y_test):
    ic(x.shape,x[:4])

import keras
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(20, input_dim = 13, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

model.compile(optimizer='rmsprop',loss = 'binary_crossentropy',metrics = ['accuracy'])

history = model.fit(X_train,y_train,batch_size = 50, epochs = EPOCHS, validation_data=(X_test,y_test), verbose = 2)

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
plt.legend(['train', 'test'], loc='lower right')
plt.show()


# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='lower right')
plt.show()

# generate classification report using predictions for categorical model
from sklearn.metrics import classification_report, accuracy_score

binary_pred = np.round(model.predict(X_test)).astype(int)

print('Results for Binary Model')
print(accuracy_score(y_test, binary_pred))
print(classification_report(y_test, binary_pred))