import cv2 as cv
from check import recognize


def start_cv(capture):
    # try:
    #     path = int(path)
    #     cap = cv.VideoCapture(path)
        
    #     if not cap.isOpened():
    #         print("Не получается запустить камеру")
        
    #         return False
        
    # except Exception:
    #     print("Не получается запустить камеру")
        
    #     return False
    while True:
        # Capture frame-by-frame
        ret, frame = capture.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Завершение работы камеры(остановка мониторинга?). Конец...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        frame = recognize(frame)
        cv.imshow('enter Q', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    capture.release()
    cv.destroyAllWindows()
    return True