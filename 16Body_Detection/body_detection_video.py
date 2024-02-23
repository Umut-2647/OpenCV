import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\body.mp4")

##cascade dosyaları her zaman duzgun calısmayabilir

body_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\fullbody.xml")

while 1:
    ret,frame=cap.read()
    if ret==False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # resmi gri tonlara ceviriyorz
    bodies = body_cascade.detectMultiScale(gray, 1.1, 1)

    ##bu bodies degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame",frame)

    if(cv2.waitKey(20)& 0xFF==ord("q")):
        break


cap.release()
cv2.destroyAllWindows()