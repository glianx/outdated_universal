import numpy as np
import keras
from keras import layers
from keras.models import Sequential
from keras.layers import Dense
import random
from icecream import ic

X_train = []
y_train = []

DATA_SIZE = 100
INPUT_DIM = 5
EPOCHS = 50
d =  [0.1,   0.2,  0.4,  0.2,  0.1]
d2 = [0.2,   0.4,  0.2,  0.1,  0.1]
d3 = [0.1,   0.1,  0.2,  0.4,  0.2]

hd =  [0.05,  0.2,    0.5,  0.2,    0.050]
hd2 = [0.2,   0.5,    0.2,  0.075,  0.025]
hd3 = [0.025, 0.075,  0.2,  0.5,    0.200]

di = hd

for donut in range(DATA_SIZE):
    fat = np.random.choice(np.arange(10,15), p = hd3) 
    sugar = np.random.choice(np.arange(10,15), p = hd3) 
    protein = np.random.choice(np.arange(10,15), p = hd2) 
    carbs = np.random.choice(np.arange(10,15), p = hd2) 
    calories = np.random.choice(np.arange(10,15), p = hd3) 

    X_train.append([fat,sugar,protein,carbs,calories])
    y_train.append(0)


for bagel in range(DATA_SIZE):
    fat = np.random.choice(np.arange(10,15), p = hd2) 
    sugar = np.random.choice(np.arange(10,15), p = hd2) 
    protein = np.random.choice(np.arange(10,15), p = hd3) 
    carbs = np.random.choice(np.arange(10,15), p = hd3) 
    calories = np.random.choice(np.arange(10,15), p = hd2) 

    X_train.append([fat,sugar,protein,carbs,calories])
    y_train.append(1)

X_train = np.array(X_train)
y_train = np.array(y_train)

p = np.random.permutation(len(y_train)) 
X_train = X_train[p]
y_train = y_train[p]

ic(y_train[:10],X_train.shape,y_train.shape)

model = Sequential()
model.add(Dense(50, input_dim = INPUT_DIM, activation = 'relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.summary()

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x = X_train,y = y_train, batch_size=20,epochs=EPOCHS,verbose = 2, validation_split=0.2)

predictions = model.predict(X_train)
predictions = np.round(predictions,0)
predictions = predictions.reshape(-1)
predictions = predictions.astype('int')

ic(predictions[:10])
ic('',y_train[:10]) #'' is so predictions[:10] and y_train[:10] can align

ic(X_train[:10])

ic(X_train.shape,y_train.shape)


evaluation = model.evaluate(X_train, y_train, batch_size = 20)
print("Test loss:", evaluation[0])
print("Test accuracy:", evaluation[1])

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
