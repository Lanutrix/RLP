import os
import numpy as np
import cv2 as cv
from interface import detect_image
def gui_ny_tipo(ok):
    print("_"*35)
    print(" "*15,ok)
    print("_"*35)
def main_fnc(path):
    cap = cv.VideoCapture(path)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = detect_image(frame)
        os.system("cls")

        gui_ny_tipo(frame)

    return "Complite"