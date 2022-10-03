import cv2

def openCam():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow('Camera',frame)
        if cv2.waitKey(10)==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
