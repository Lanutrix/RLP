import numpy as np
from tensorflow import keras
from add_img_lib import add_img
import cv2 as cv

path = "cv_np/frog.jpg"
x,y = 32, 32

img_input = add_img(path, x, y)

model = keras.models.load_model('education/main_1_50_eph.h5')

detectionClass=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

x = np.expand_dims(img_input, axis=0)

result = model.predict(x)
predictClass=np.argmax(result)

# print(f"Class number: {predictClass}\nHis name: {detectionClass[predictClass]}")

cv.imshow(f"its: {detectionClass[predictClass]}", img_input)
cv.waitKey(0)
# i=input()