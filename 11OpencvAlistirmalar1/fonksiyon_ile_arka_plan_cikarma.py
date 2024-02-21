import cv2
import numpy as np
 ##fonksiyon ile yapıldığı zaman daha iyi ve temiz oluyor
cap=cv2.VideoCapture("C:\\Users\\umuty\\Downloads\\car.mp4")
subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=50,detectShadows=True)   ##hazır fonksiyon ile arka plan çıkarma
##detectShadows=gölgeler de algılansın mı ?


while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask=subtractor.apply(frame)  #subtractor fonksiyonunu frame uygular

    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    if (cv2.waitKey(20) & 0xFF == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()