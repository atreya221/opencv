import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import numpy as np
import PIL
import matplotlib.pyplot as plt
from tensorflow import keras
import pathlib

data_dir = pathlib.Path("./data/train")

batch_size = 32

# resize all images to size (180,180)
img_height = 180
img_width = 180


# Create training dataset using keras.preprocessing
train_ds = keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "training",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size
)

# Create validation set from images directory (train - 0.8, validation - 0.2)
val_ds = keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split = 0.2,
    subset = "validation",
    seed = 123,
    image_size = (img_height, img_width),
    batch_size = batch_size
)

classes = train_ds.class_names
num_classes = len(classes)
#print(classes)

for images, labels in train_ds:
  images_shape = images.shape
  labels_shape = labels.shape
  #print(images.shape)
  #print(type(images))
  break

# Define the model architecture

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization

data_augmentation = Sequential(
  [
    keras.layers.experimental.preprocessing.RandomFlip("horizontal", input_shape=(180, 180, 3)),
    keras.layers.experimental.preprocessing.RandomRotation(0.1),
    keras.layers.experimental.preprocessing.RandomZoom(0.1),
  ]
)

model = Sequential()


model.add(data_augmentation)
model.add(keras.layers.experimental.preprocessing.Rescaling(1./255)) # Normalize the dataset to improve accuracy
"""
model.add(Conv2D(32, (3, 3), activation='relu'))  
model.add(BatchNormalization())  # normalize the activations after each layer
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))  # random dropping of units to prevent overfitting and improve validation accuracy

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model = Sequential([
  layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  """
model.add(Conv2D(16, 3, padding='same', activation='relu'))
model.add(MaxPooling2D())  
model.add(Conv2D(32, 3, padding='same', activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(64, 3, padding='same', activation='relu'))
model.add(MaxPooling2D())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
# ])

print(model.summary())

# compile the model
model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer = 'adam',
              metrics = ['accuracy'])



# callbacks used to prevent model from diverging and
# reduce learning rate (by factor of 0.5) as we approach minima
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

earlystop = EarlyStopping(patience=10)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_loss', 
                                            patience=2, 
                                            verbose=1, 
                                            factor=0.5, 
                                            min_lr=0.00001)

callbacks = [earlystop, learning_rate_reduction]

try:
    history = model.fit(train_ds,
                    validation_data = val_ds,
                    epochs = 10,
                    callbacks = callbacks,
                    verbose=1,
                    )
except KeyboardInterrupt:
    pass

n = len([name for name in os.listdir('history') if os.path.isfile(name)])//2
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'], color='red')
plt.xlabel('epochs')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend(['Training accuracy', 'Validation accuracy'], loc = 'lower right')
plt.show()
plt.savefig(f'history/accuracy.png_{n+1}')

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'], color='red')
plt.xlabel('epochs')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend(['Training loss', 'Validation loss'], loc = 'upper right')
plt.show()
plt.savefig(f'history/loss.png_{n+1}')

#serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("\nSaved model to disk\n")