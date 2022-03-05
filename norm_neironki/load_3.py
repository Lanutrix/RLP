import cv2 as cv
import numpy as np
from tensorflow import keras
from add_img_lib import add_img

PATH_MODEL = "education/model_1.h5"
PATH_IMG   = "norm_neironki/5.png"

model = keras.models.load_model(PATH_MODEL)

img = add_img(PATH_IMG, 28, 28)

x = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x = np.expand_dims(x, axis=0)

result=model.predict(x)

result = np.argmax(result)
print(result)

cv.imshow(f"its: {str(result)}", img)
cv.waitKey(0)