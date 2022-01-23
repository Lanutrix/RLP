import numpy as np
import cv2 as cv

img = cv.imread("cv_np/food.png")
(h, w) = int(img.shape[1]), int(img.shape[0])

res= cv.resize(img, (int(h/1.2), int(w/1.2)),cv.INTER_NEAREST)

center = (int(h//2), int(w//2))

r=cv.getRotationMatrix2D(center,180,0.7)
r_img=cv.warpAffine(res,r,(h,w))

cv.imshow("pain", r_img)
cv.waitKey(0)