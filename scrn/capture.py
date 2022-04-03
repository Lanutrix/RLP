import cv2 as cv
from check import recognize
def start_cv(path):
    cap = cv.VideoCapture(path)
    if not cap.isOpened():
        print("Cannot open camera")
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        frame = recognize(frame)
        cv.imshow('enter Q', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()