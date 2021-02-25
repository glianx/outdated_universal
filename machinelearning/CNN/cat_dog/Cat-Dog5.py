#works very successfully
#from https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d 
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import os
from icecream import ic
# dimensions of our images.
img_width, img_height = 30,30

train_data_dir = os.path.join(os.path.dirname(__file__),'PetImages/Train')
validation_data_dir = os.path.join(os.path.dirname(__file__),'PetImages/Test')

nb_train_samples = 11000
nb_validation_samples = 150
epochs = 3
batch_size = 32

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
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

right, wrong = 0,0

ic(type(train_generator))
ic(train_generator) 

X_test = []
y_test = []

CATEGORIES = ['cat','dog']

for i in CATEGORIES:
    for img_name in os.listdir(os.path.join(validation_data_dir,i)):
        img = keras.preprocessing.image.load_img(
            os.path.join(test_dir,i,img_name), target_size=(img_width,img_height), color_mode='grayscale'
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

# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


from sklearn.metrics import average_precision_score
average_precision = average_precision_score(y_test, y_score)

print('Average precision-recall score: {0:0.2f}'.format(
    average_precision))