from cv2 import COLOR_BAYER_GB2BGR, COLOR_BGR2GRAY, cvtColor
import numpy as np
import cv2 as cv

img = cv.imread("cv_np/pain.png")
def h_w(img):
    (h, w) = int(img.shape[0]), int(img.shape[1])

    center = (int(h//2), int(w//2))
    return h, w, center

gray =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
h,w,center = h_w(gray)

res= cv.resize(gray, (int(h/1.7), int(w/1.7)),cv.INTER_NEAREST)

h,w,center = h_w(res)
r=cv.getRotationMatrix2D(center,90,1)
r_img=cv.warpAffine(res,r,(h,w))

cv.imshow("pain", r_img)
cv.waitKey(0)
