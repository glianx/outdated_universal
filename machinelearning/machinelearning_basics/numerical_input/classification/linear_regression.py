from tensorflow import keras
import numpy as np
import random
from icecream import ic
import matplotlib.pyplot as plt
from math import exp

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer='sgd', loss = 'mean_squared_error')

print(model.summary())

x = []
y = []

slope = random.randrange(-5,5,2)
intercept = random.randrange(-5,5)
ic(slope,intercept)

def function(x):
    return slope * x + intercept
    # return x
    # return 1.0 / (1.0 + exp(-x)) 

error = 5

for data_point in range(50):
    x_point = random.randrange(-10,10)
    y_point = function(x_point)

    random_variation = random.randrange(-error,error)
    # random_variation = 0
    x.append(x_point)
    y.append(y_point + random_variation)

plt.plot(x,y,'ro')
plt.show()

x = np.array(x)
y = np.array(y)

model.fit(x,y, epochs = 100, verbose=2, batch_size=30)
ic(model.predict([20]))

ic(slope,intercept,error,x,y)

plt.plot(x,y,'bo')
# plt.plot([0,1,2],[3,4,5])
b = model.predict([0])
d = model.predict([20])
plt.plot([0,b],[20,d])
plt.show()