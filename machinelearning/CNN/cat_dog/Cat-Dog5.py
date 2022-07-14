#works successfully
#from https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d 
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import os
from icecream import ic
# dimensions of our images.
img_width, img_height = 40,40

train_data_dir = os.path.join(os.path.dirname(__file__),'PetImages/Train')
validation_data_dir = os.path.join(os.path.dirname(__file__),'PetImages/Test')

nb_train_samples = 5000
nb_validation_samples = 50
epochs = 1
batch_size = 25

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
    ic()
else:
    input_shape = (img_width, img_height, 3)
    ic()

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale= 1/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
    
ic(train_datagen)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

ic(test_datagen)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

ic(train_generator)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

ic(validation_generator)

#Convolutional Neural Network
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])



model.summary()

model.fit(
    train_generator,
    steps_per_epoch= nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps= nb_validation_samples // batch_size)

model.save_weights('first_try.h5')
ic(type(train_generator))
right, wrong = 0,0
'''
for images, labels in train_generator.take(100):  # only take first element of dataset
    ic(images.shape) #ic(images.numpy())
    ic(labels.numpy())
'''
'''
predictions = model.predict(test_features[200:700])
labels = test_labels[200:700]

ic(predictions.shape)
ic(predictions)

ic(labels.shape)
ic(labels)

for prediction,label in zip(predictions,labels):
    #ic(prediction)
    a = np.argmax(prediction)
    b = np.argmax(label)
    ic(np.argmax(prediction),np.argmax(label),a==b)
    if np.argmax(prediction) == np.argmax(label):
        right += 1
    else:
        wrong += 1
ic(right,wrong,right/(right+wrong))
'''