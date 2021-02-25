from tensorflow import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer='sgd', loss = 'mean_squared_error')

print(model.summary())

#y = 2x - 1
xs = np.array([-1.0, 0.0, 1.0])
ys = np.array([-3.0, -1.0, 1.0])

#y = 2x - 1
model.fit(xs,ys, epochs = 50, verbose=2)

x = 10.0
print(model.predict([10]))
