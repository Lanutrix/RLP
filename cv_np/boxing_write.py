import cv2 as cv
def boxing(xy1, xy2):
    img = cv.imread("cv_np/frog.jpg")

    # (h, w) = int(img.shape[0]), int(img.shape[1])
    img = cv.rectangle(img,
        xy1,            #x1, y1
        xy2,            #x2, y2
        (255, 255, 0),  #color (RGB)
        2               #толщина в px
    )

    cv.imshow("~", img)
    cv.waitKey(0)

if __name__=="__main__":
    boxing((22,22), (33, 66))