import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

import matplotlib
import matplotlib.pyplot as plt

train_labels = []
train_samples = []

#clinical drug test
#2000 total patients, half +/-65
#95% of -65 did not experience side effects (0)
#95% of +65 experienced side effects (1)

#generating labeled data

for i in range(50): #5% of tests
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1)

    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(0)

for i in range(950): #95% of tests
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)

    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(1)

 
''' for i in range(1000): #100% of tests
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)

    random_older = randint(65,100)
    train_samples.append(random_older)
    train_labels.append(1)'''

#data processing

#transform into numpy array
train_labels = np.array(train_labels)
train_samples = np.array(train_samples)
train_labels, train_samples = shuffle(train_labels,train_samples)
#print(train_labels)
#print(train_samples)

#scale data from 0-1
scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1))

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
'''
physical_devices = tf.config.experimental.list_physical_devices('GPU')
print('Num GPUs available: ', len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0],True)
'''
#layers
#dense layer = fully connected layer
model = Sequential([
    Dense(units = 16, input_shape = (1,), activation ='relu'), #1st hidden layer, w/ 16 nodes (arbitrary)
    Dense(units = 32, activation ='relu'), #relu activation function - positive returns same, else return 0
    Dense(units = 2, activation = 'softmax') #softmax function returns probabilities, curved line like sigmoid
])

#model.summary()

#compile the data
model.compile(optimizer=Adam(learning_rate=0.0001),loss='sparse_categorical_crossentropy',metrics = ['accuracy'])

#fit function- x and y are features and labels (input/output)
model.fit(x=scaled_train_samples,y=train_labels,validation_split = 0.1, batch_size=10,epochs=30,shuffle=True,verbose=2)

#testing

test_labels = []
test_samples = []

#generating labeled data - TEST
for i in range(10): #5% of tests
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(1)

    random_older = randint(65,100)
    test_samples.append(random_older)
    test_labels.append(0)

for i in range(190): #95% of tests
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(0)

    random_older = randint(65,100)
    test_samples.append(random_older)
    test_labels.append(1)
 
#data processing

#transform into numpy array
test_labels = np.array(test_labels)
test_samples = np.array(test_samples)
test_labels, test_samples = shuffle(test_labels,test_samples)
print(test_labels)
print(test_samples)

#scale data from 0-1
scaler = MinMaxScaler(feature_range=(0,1))
scaled_test_samples = scaler.fit_transform(test_samples.reshape(-1,1))

#print(scaled_test_samples)

predictions = model.predict(x = scaled_test_samples, batch_size=10,verbose=0)
#for i in predictions:
    #print(i)

rounded_predictions = np.argmax(predictions, axis=-1)
#for i in rounded_predictions:
    #print(i)

#confusion matrix
'''
#%matplotlib inline
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

#exec(%matplotlib inline)

#get_ipython().magic('matplotlib inline')

from sklearn.metrics import confusion_matrix
import itertools
import matplotlib.pyplot as plt 

cm = confusion_matrix(y_true = test_labels, y_pred = rounded_predictions)

def plot_confusion_matrix(cm,classes,
                        normalize = False,
                        title = 'Confusion Matrix',
                        cmap = plt.cm.Blues):
    pass

plt.imshow(cm,interpolation = 'nearest', cmap = cmap)
plt.title(title)
plt.colorbar()
tick_marks= np.arange(len(classes))
plt.xticks(tick_marks,classes,rotation = 45)
plt.yticks(tick_marks,classes)

if normalize:
    cm = cm.astype('float') / cm.sum(axis = 1) [:, np.newaxis]
    print('normalized confusion matrix')
else:
    print('Not normalized confusion matrix')

print(cm)

thresh = cm.max()/2
for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
    plt.text(j,i,cm[i,j])
    horizontalalignment = 'center'
    color = 'white' if cm[i,j] > thresh else 'black'
plt.tight_layout()
cm_plot_labels = ['no side effects','had side effects']
plot_confusion_matrix(cm=cm, classes = cm_plot_labels, title = 'Confusion Matrix')
'''

