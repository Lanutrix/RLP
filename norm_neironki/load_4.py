import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.utils import np_utils
import random, time

model = keras.models.load_model('/home/dmodv/git_project/testing/education/main_1.h5')

detectionClass=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train = x_train/255
x_test = x_test/255

y_train = np_utils.to_categorical(y_train)
y_test  = np_utils.to_categorical(y_test )

while 1:
    n = random.randint(0,9999)

    x = np.expand_dims(x_test[n], axis=0)

    result = model.predict(x)

    predictClass=np.argmax(result)
    plt.imshow(x_test[n], cmap=plt.cm.binary)
    plt.show()

    print(f"Class number: {predictClass}\nHis name: {detectionClass[predictClass]}")

    time.sleep(1)
    i=input()