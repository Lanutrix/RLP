import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.engine.input_layer import Input
from keras import Sequential, Model
from tensorflow import keras
from keras.layers import Dense
from tensorflow import keras

input = np.array([[1,1],[1,0],[0,1],[0,0]])
output= np.array([0,1,1,0])

model = keras.Sequential()
model.add(Dense(16, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="mse", optimizer=keras.optimizers.Adam(0.01))

model.fit(input,output, epochs=3000)