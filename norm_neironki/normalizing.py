import matplotlib.pyplot as plt
# from cv2 import COLOR_BAYER_GB2BGR, COLOR_BGR2GRAY, cvtColor
import cv2 as cv
import numpy as np

# path="norm_neironki/5.png"
def norma(path):
    x = cv.imread(path)
    x = cv.cvtColor(x, cv.COLOR_BGR2GRAY)
    x=x/255
    return x

    
    # print(np.shape(x))
    # x = x.reshape(-1,28,28)

    
    # x = np.expand_dims(x, axis=0)
    # print(np.shape(x))
    

    # plt.imshow(x,cmap=plt.cm.binary)
    # plt.show()

    # cv.imshow("pain", x)
    # cv.waitKey(0)

