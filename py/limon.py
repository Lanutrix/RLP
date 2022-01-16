from imageai.Detection import VideoObjectDetection
import os


def forFrame(frame_number, output_array, output_count):
    print("Output count for unique objects : ", output_count)
    for i in output_count:
        try:
            f = open('text.txt', "r+")
        except:
            f = open('text.txt', "w")
        if i == "car":
            f.read("car: "+output_count["car"]+"/n")



video_detector = VideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
video_detector.loadModel()


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, ""), output_file_path=os.path.join(execution_path, "video_frame_analysis") ,  frames_per_second=20, per_frame_function=forFrame,  minimum_percentage_probability=30)