import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\dog.mp4")

while (1):
    _,frame=cap.read()   #hsv code for red
    if _==False:
        break
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    sensivity=26
    lower_white=np.array([0,0,255-sensivity]) ##bu degerler internette aratılıp bulunabilir
    upper_white=np.array([255,sensivity,255])

    mask=cv2.inRange(hsv,lower_white,upper_white) ##beyaz renge maske uyguluyor

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("res",res)

    if( cv2.waitKey(20)&0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()

