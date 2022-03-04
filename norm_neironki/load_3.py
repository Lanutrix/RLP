# import os
# from keras.engine.input_layer import Input
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
# from keras import Sequential
# from keras.layers import Dense, Conv2D, Flatten
# import normalizing as norm

def norma(path):
    x = cv.imread(path)
    x = cv.cvtColor(x, cv.COLOR_BGR2GRAY)
    x=x/255
    return x

img_input = norma("norm_neironki/5.png")

# n=5928

# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# # x_train = x_train.reshape(60000, 28,28,1)
# # x_test = x_test.reshape(10000, 28,28,1)

# x_train = x_train/255
# x_test = x_test/255
# y_train = keras.utils.to_categorical(y_train)
# y_test = keras.utils.to_categorical(y_test)


model = keras.models.load_model('/home/dmodv/git_project/testing/norm_neironki/model_1.h5')


# print(np.shape(img_input))
x = np.expand_dims(img_input, axis=0)
# print(np.shape(x))

result=model.predict(x)
plt.imshow(img_input,cmap=plt.cm.binary)
plt.show()

result = np.argmax(result)
print(result)