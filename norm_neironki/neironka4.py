from keras.engine.input_layer import Input
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Conv2D, Flatten, Dropout, BatchNormalization, MaxPooling2D

name_file="/home/dmodv/git_project/testing/education/main_1"
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")

x_train = x_train/255
x_test = x_test/255

y_train = np_utils.to_categorical(y_train)
y_test  = np_utils.to_categorical(y_test )

class_num = y_test.shape[1]
print(class_num)


model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation="relu", input_shape = x_train.shape[1:], padding='same'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), padding='same', activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Conv2D(64, kernel_size=(3,3), activation="relu", padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Conv2D(128, kernel_size=(3,3), padding='same', activation="relu"))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(256, activation="relu"))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(class_num, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

# print(model.summary())

history = model.fit(x_train, y_train, epochs=50, batch_size=64)

plt.plot(history.history["loss"])
plt.grid(True)
plt.show()

n = 56
x = np.expand_dims(x_test[n], axis=0)
result = model.predict(x)
print(np.argmax(result))

model.save(name_file+'.h5', save_format='h5')