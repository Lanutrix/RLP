from keras.engine.input_layer import Input
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Conv2D, Flatten
from keras.models import load_model
# import cv2 as cv


model = keras.models.load_model('/home/dmodv/git_project/testing/norm_neironki/model_1.h5')
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train/255
x_test = x_test/255
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)
# x_test[n] = cv.imread("/home/dmodv/git_project/testing/norm_neironki/5.png")
# x = np.expand_dims(x_test[n], axis=0)/255
n=595
x = np.expand_dims(x_test[n], axis=0)
def prd(x):
    return model.predict(x)

print(np.argmax(prd(x)))



plt.xticks([])
plt.yticks([])
plt.imshow(x_test[n], cmap=plt.cm.binary)
plt.show()