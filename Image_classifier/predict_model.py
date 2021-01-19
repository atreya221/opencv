import os
import time
import psutil
import pathlib
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import cv2
import numpy as np
from PIL import Image


data_dir = './data/train'
subdirs = os.listdir(data_dir)
#print(subdirs)

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

# load weights into new model
model.load_weights('model.h5')
# print("Loaded model from disk")

# Compile the model
model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer = 'adam',
              metrics = ['accuracy'])

# Predict the class of the test image to be uploaded

print('Upload a test image to predict its class using your model.')

test_path = input("\nProvide the path to your test image :\n")
print("\n")
test_img = cv2.imread(test_path)
im = Image.open(test_path)
#cv2.imshow('Test Image', test_img)
im.show()
# display image for 3 seconds
time.sleep(3)

# hide image
for proc in psutil.process_iter():
    if proc.name() == "display":
        proc.kill()


import math
test_img = cv2.resize(test_img, (180,180))
test_img = test_img.reshape((1,180,180,3))
pred = model.predict(test_img)
print(
    "This image most likely belongs to {} with {:.2f}% confidence."
    .format(sorted(subdirs)[np.argmax(pred)], 100 * np.max(pred))
)