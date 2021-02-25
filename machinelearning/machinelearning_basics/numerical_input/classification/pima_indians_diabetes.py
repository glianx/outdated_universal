import numpy as np
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import os
from icecream import ic
dirname = os.path.dirname(__file__)
DATASET_PATH = os.path.join(dirname, "pima_indians_diabetes.csv")
ic(dirname,DATASET_PATH)

epochs = 50
batch_size = 10

# load the dataset
dataset = loadtxt(DATASET_PATH, delimiter=',')
# split into input (X) and output (y) variables

#Preprocessing
X = dataset[:,0:8]
y = dataset[:,8]

X = np.array(X)
y = np.array(y)

np.set_printoptions(suppress=True)
ic(X[:5],y[:5],X.shape,y.shape)

#Neural Network
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

history = model.fit(X, y, epochs=epochs, batch_size=batch_size, validation_split=0.2, verbose=2)

predictions = (model.predict(X) > 0.5).astype("int32")
#print(predictions)
# summarize the first 5 cases
for i in range(10):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))


np.set_printoptions(suppress=True, precision=0)
predictions = model.predict(X)
predictions = predictions.reshape(-1)

ic(predictions[:10], y[:10])

np.set_printoptions(suppress=True, precision=3)
# evaluate the model
print(model.evaluate(X, y, verbose=0),type(model.evaluate(X, y, verbose=1)))
loss, accuracy= model.evaluate(X, y, verbose=1)

#accuracy = model.evaluate(X, y)
ic(loss, accuracy)

