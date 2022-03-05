from keras.engine.input_layer import Input
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense, Conv2D, Flatten


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# x_train = x_train.reshape(60000, 28,28,1)
# x_test = x_test.reshape(10000, 28,28,1)
x_train = x_train/255
x_test = x_test/255
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

plt.figure(figsize=(10,5))
for i in range(25):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.imshow(x_train[i],cmap=plt.cm.binary)
  
plt.show()
model = Sequential()

model = Sequential()

model.add(Conv2D(64, kernel_size=(3,3), activation="relu", input_shape = (28, 28, 1)))
model.add(Conv2D(32, kernel_size=(3,3), activation="relu"))
model.add(Flatten())
model.add(Dense(10, activation="softmax"))

print(model.summary())

batch_size = 128
epochs = 10

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)



score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])



n=5952
x = np.expand_dims(x_test[n], axis=0)

result=model.predict(x)
plt.imshow(x_test[n],cmap=plt.cm.binary)
print(np.argmax(result))



model.save('education/model_1.h5', save_format='h5')