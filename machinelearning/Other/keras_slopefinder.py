from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer='sgd', loss = 'mean_squared_error')

model2 = keras.Sequential([keras.layers.Dense(1, input_shape = [1])])
model2.compile(optimizer='sgd', loss = 'mean_squared_error')

model3 = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model3.compile(optimizer='sgd', loss = 'mean_squared_error')

#y = 2x - 1
xs = np.array([-1.0, 0.0, 1.0])
ys = np.array([-3.0, -1.0, 1.0])

#y = 2x - 1
model.fit(xs,ys, epochs = 500)
#y = -x + 5
model2.fit(np.array([-1.0, 0.0, 1.0]),np.array([6.0, 5.0, 4.0]), epochs = 500)
#y = 0.5x + 1
model3.fit(np.array([x for x in range(3)]),np.array([x/2+1 for x in range(3)]), epochs = 500)

x = 10.0
print(f'y = 2x - 1. x = {x}, y prediction: {model.predict([x])}, y-int prediction: {model.predict([0.0])}')
print(f'y = -x + 5. x = {round(x)}, y prediction: {round(float(model2.predict([x])))}, y-int prediction:  {round(float(model2.predict([0.0])))}')
print(f'y = x/2 + 1. x = {round(x)}, y prediction: {round(float(model3.predict([x])))}, y-int prediction: {round(float(model3.predict([0.0])))}')
print('\n')