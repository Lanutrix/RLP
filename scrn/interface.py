from model import make_yolov3_model
from weight_parser import WeightReader
from boxes import decode_netout, correct_yolo_boxes, do_nms, get_boxes
import cv2 as cv
from keras.models import load_model

# define the anchors
anchors = [[116,90, 156,198, 373,326], [30,61, 62,45, 59,119], [10,13, 16,30, 33,23]]

# define the probability threshold for detected objects
class_threshold = 0.6

# define the labels
labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
	"boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
	"bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
	"backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
	"sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
	"tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
	"apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
	"chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
	"remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
	"book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]



yolov3 = make_yolov3_model()

weight_reader = WeightReader('yolov3.weights')

weight_reader.load_weights(yolov3)

yolov3.save('model.h5')

yolov3 = load_model('model.h5')


from numpy import expand_dims
def load_image_pixels(image, shape):
    height = image.shape[0]
    width = image.shape[1]
    
    image = cv.resize(image, shape)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB )
    
    image = image.astype('float32')
    image /= 255.0
    image = expand_dims(image, 0)
    
    return image, width, height

# draw all results
def draw_boxes(image, v_boxes, v_labels, v_scores):
  
    print(v_boxes,v_labels, v_scores)
    for i in range(len(v_boxes)):
        box = v_boxes[i]
        y1, x1, y2, x2 = box.ymin, box.xmin, box.ymax, box.xmax
        # print(y1, x1, y2, x2)
        # width, height = x2 - x1, y2 - y1
        image = cv.rectangle(image, (x1, y1), (x2,y2), (255, 0, 0), 2)
    
    cv.putText(image, f"Count of people = : {len(v_boxes)}", (20, 40), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        
    return image


def detect_image(image):
    boxes = list() 
    # define the expected input shape for the model
    input_w, input_h = 416, 416

    new_image, image_w, image_h = load_image_pixels(image, (input_w, input_h))

    # make prediction
    yhat = yolov3.predict(new_image)
    # summarize the shape of the list of arrays
    print([a.shape for a in yhat])
    for i in range(len(yhat)):
        # decode the output of the network
        boxes += decode_netout(yhat[i][0], anchors[i], class_threshold, input_h, input_w)
 
    # correct the sizes of the bounding boxes for the shape of the image
        correct_yolo_boxes(boxes, image_h, image_w, input_h, input_w)

    # suppress non-maximal boxes
        do_nms(boxes, 0.5)

        # get the details of the detected objects
        v_boxesr, v_labelsr, v_scores = get_boxes(boxes, labels, class_threshold)
        v_labels, v_boxes=[],[]
    
    # print(v_boxes[0].xmin)
    for i in range(len(v_labelsr)):
        if v_labelsr[i]=="person":
            v_labels.append(v_labelsr[i])
            v_boxes.append(v_boxesr[i])
    # print(v_boxes[0].xmin)

    # summarize what we found
    for i in range(len(v_boxes)):
        print(v_labels[i], v_scores[i])
    # print(v_boxes[0].xmin)

    # draw what we found
    image = draw_boxes(image, v_boxes, v_labels, v_scores)
    
    return image