import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.utils import np_utils
import random, time

def norma(path):
    x = cv.imread(path)
    # cv.imshow("pain", x)
    # cv.waitKey(0)
    # x = cv.cvtColor(x, cv.COLOR_BGR2GRAY)
    x=x/255
    return x

img_input = norma("norm_neironki/car.png")

model = keras.models.load_model('/home/dmodv/git_project/testing/education/main_1_50_eph.h5')

detectionClass=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

# x_train = x_train.astype("float32")
# x_test = x_test.astype("float32")

# x_train = x_train/255
# x_test = x_test/255

# y_train = np_utils.to_categorical(y_train)
# y_test  = np_utils.to_categorical(y_test )

# for i in range(2):
#     n = random.randint(0,9999)
#     print(np.shape(x_test[n]))

x = img_input.astype("float32")
x = np.expand_dims(img_input, axis=0)
print(np.shape(x))
result = model.predict(x)

predictClass=np.argmax(result)
plt.imshow(img_input, cmap=plt.cm.binary)
plt.show()

print(f"Class number: {predictClass}\nHis name: {detectionClass[predictClass]}")

time.sleep(1)
# i=input()