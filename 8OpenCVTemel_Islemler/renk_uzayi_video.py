import cv2
from cv2 import VideoCapture

cap=VideoCapture("video.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  ##her frami gri tonlarına cevirip tekrar frame deigiskenine atar
    if ret==False:
        break

    cv2.imshow("Video",frame)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()