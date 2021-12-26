from imageai.Detection import ObjectDetection
from numpy.core.numeric import False_
import os

img="test2"

detector = ObjectDetection()

detector.setModelTypeAsYOLOv3()


detector.setModelPath("yolo.h5")
detector.loadModel()

custom = detector.CustomObjects(person=True, dog=True)


detections = detector.detectCustomObjectsFromImage(custom_objects=custom,input_image=(img+".jpg"), output_image_path=(img+"_new.jpg"), minimum_percentage_probability=30)
for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")