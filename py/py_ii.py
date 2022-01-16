from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "py_ii/yolo.h5"))
detector.loadModel()

def forFrame(frame_number, output_array, output_count):
    car=0
    for i in output_array:
        if i['name']=='car':
            car+=1
            print(i['name'])
    try:
        f = open('text.txt', "r+")
    except:
        f = open('text.txt', "w+")
    f.write("car:"+str(car)+"\n")
    f.close()
    

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "py_ii/Traffic10881.mp4"),
                            output_file_path=os.path.join(execution_path, "py_ii/Traffic1183.mp4")
                            , frames_per_second=20, log_progress=True, minimum_percentage_probability=40, detection_timeout=1, per_frame_function=forFrame)

