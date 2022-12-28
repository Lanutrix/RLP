@ECHO OFF
ECHO "STARTED DOWNLOADS"
powershell -Command "Invoke-WebRequest https://github.com/Shahnawax/HAR-CNN-Keras/raw/master/model.h5 -OutFile model.h5"
powershell -Command "Invoke-WebRequest https://github.com/patrick013/Object-Detection---Yolov3/raw/master/model/yolov3.weights -OutFile yolov3.weights"
python -m pip install -r requirements.txt