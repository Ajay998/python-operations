import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
import os
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from tensorflow.keras.utils import to_categorical
from tensorflow.python.keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,GlobalAveragePooling2D,Activation,Dropout
from tensorflow.python.keras import Sequential,backend,optimizers
from tensorflow.keras.layers import BatchNormalization



parasitized_data = os.listdir('/home/flock/PycharmProjects/sample1/json_operations/projects/malaria_detection/archive/cell_images/Parasitized/')
uninfected_data = os.listdir('/home/flock/PycharmProjects/sample1/json_operations/projects/malaria_detection/archive/cell_images/Uninfected/')

data = []
labels = []

for img in parasitized_data:
    try:
        img_read = plt.imread('/home/flock/PycharmProjects/sample1/json_operations/projects/malaria_detection/archive/cell_images/Parasitized/' + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(1)
    except:
        None

for img in uninfected_data:
    try:
        img_read = plt.imread('/home/flock/PycharmProjects/sample1/json_operations/projects/malaria_detection/archive/cell_images/Uninfected/' + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(0)
    except:
        None

image_data = np.array(data)
labels = np.array(labels)
print("image_data:", len(labels))
print("labels:", len(labels))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(image_data, labels, test_size = 0.2,random_state = 0)

y_train = to_categorical(y_train, num_classes = 2)
y_test = to_categorical(y_test, num_classes = 2)

print("X_train:",len(X_train))
print("X_test:",len(X_test))
print("y_train:",len(y_train))
print("y_test:",len(y_test))

model = Sequential()

inputShape = (50, 50, 3)

if backend.image_data_format() == 'channels_first':
    inputShape = (3, 50, 50)
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=inputShape))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization(axis=-1))
model.add(Dropout(0.2))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization(axis=-1))
model.add(Dropout(0.2))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization(axis=-1))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(512, activation='relu'))
model.add(BatchNormalization(axis=-1))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.summary()

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.fit(X_train, y_train, epochs = 2, batch_size = 32)
predict = model.evaluate(X_test, y_test)
print("Loss: ",predict[0])
print("Accuracy: ",predict[1]*100)

model.save('a95e25model.h5')

