import cv2 as cv

def add_img(path, x, y):
    img = cv.imread(path)
    img = cv.resize(img, (x,y))
    img = img / 255
    img = img.astype("float32")
    
    return img

if __name__=="__main__":
    img_input = add_img("norm_neironki/5.png", 32, 32)
    cv.imshow("pain", img_input)
    cv.waitKey(0)