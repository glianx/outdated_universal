#image classification from scratch - keras example
#works ok, sometime corrupt images
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from icecream import ic
import os
import numpy

main_dir = os.path.join(os.path.dirname(__file__),"PetImages")
train_dir = os.path.join(main_dir,"Train")
test_dir = os.path.join(main_dir,"Test")

#main_dir = os.path.join(os.path.dirname(__file__),"PetImages2")
#train_dir = os.path.join(os.path.dirname(__file__),"PetImages2","Test")
#test_dir = os.path.join(os.path.dirname(__file__),"PetImages","Test")


#ic(main_dir)
ic(train_dir)
ic(test_dir)

image_size = (30,30)
batch_size = 32
epochs = 7

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    train_dir,
    validation_split=0.2,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    test_dir,
    validation_split=0.2,
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

import matplotlib.pyplot as plt

plt.figure(figsize=(5,5))
x_test = []
y_test = []
for images, labels in train_ds.take(1):
    x_test.append(images)
    y_test.append(labels)

y_test = numpy.array(y_test)
y_test = y_test.reshape(32)

for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")
        #ic(images)
        ic(labels, labels[i])
plt.show()

data_augmentation = keras.Sequential(
    [
        layers.experimental.preprocessing.RandomFlip("horizontal"),
        layers.experimental.preprocessing.RandomRotation(0.1),
    ]
)

plt.figure(figsize=(5,5))

for images, _ in train_ds.take(1):
    for i in range(9):
        augmented_images = data_augmentation(images)
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(augmented_images[0].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")
plt.show()

train_ds = train_ds.prefetch(buffer_size=32)
val_ds = val_ds.prefetch(buffer_size=32)

def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    # Image augmentation block
    x = data_augmentation(inputs)

    # Entry block
    x = layers.experimental.preprocessing.Rescaling(1.0 / 255)(x)
    x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [128, 256, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        activation = "sigmoid"
        units = 1
    else:
        activation = "softmax"
        units = num_classes

    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(units, activation=activation)(x)
    return keras.Model(inputs, outputs)


model = make_model(input_shape=image_size + (3,), num_classes=2)
keras.utils.plot_model(model, show_shapes=True)



callbacks = [
    keras.callbacks.ModelCheckpoint("save_at_{epoch}.h5"),
]
model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)
model.fit(
    train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds, verbose = 1
)
pets = ["Cat","Dog"]
right, wrong = 0,0
dog_predictions, dog_actual, cat_predictions, cat_actual, true_positives, true_negatives, false_positives, false_negatives = [0 for x in range(8)]
for i in pets:
    for img_name in os.listdir(os.path.join(test_dir,i)):

        img = keras.preprocessing.image.load_img(
            os.path.join(test_dir,i,img_name), target_size=image_size
        )
        img_array = keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis

        predictions = model.predict(img_array)
        score = predictions[0]
        print(
            f"This image is {(100 * (1 - score))} percent cat and {100 * score} percent dog."
        )
        cat = 100 * (1 - score)
        dog = 100 * score

        p = pets[(cat,dog).index(max(cat,dog))]
        ic(cat,dog,i,p==i)
        if p == i:
            right += 1
        else:
            wrong += 1
    
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

ic(dog_predictions, dog_actual, cat_predictions, cat_actual)
ic(true_positives)
ic(true_negatives)
ic(false_positives)
ic(false_negatives)
if true_positives+false_positives > 0:
    print(f'dog precision = {round(true_positives/(true_positives+false_positives),3)}')
if true_negatives + false_negatives > 0:
    print(f'cat precision = {round(true_negatives/(true_negatives+false_negatives),3)}')
print(f'dog recall = {round(true_positives/(true_positives+false_negatives),3)}')
print(f'cat recall = {round(true_negatives/(true_negatives+false_positives),3)}')
ic(right,wrong,right/(right+wrong))

from sklearn.metrics import classification_report
import numpy as np
y_pred = model.predict(x_test, batch_size=64, verbose=0)
y_pred_bool = np.argmax(y_pred, axis=1)
target_names = ['Cat','Dog']
print('\n',classification_report(y_test, y_pred_bool, target_names=target_names))

evaluation = model.evaluate(train_ds, verbose=0)
print("Test loss:", evaluation[0])
print("Test accuracy:", evaluation[1])