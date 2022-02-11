from imageai.Detection import VideoObjectDetection
import os
from lol import *

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "py/yolo.h5"))
detector.loadModel()

text=""

def forFrame(frame_number, output_array, output_count):
    global text
    text=dep(frame_number,output_array,text)
    

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "scr/video/VID_2022.mp4"),
                            output_file_path=os.path.join(execution_path, "scr/video/vid2022_new")
                            , frames_per_second=20, log_progress=True, minimum_percentage_probability=40, detection_timeout=4, per_frame_function=forFrame)


nastr(text)