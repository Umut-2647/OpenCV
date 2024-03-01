import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\car.mp4")


car_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\car_cascade\\car_cascade.xml")

while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640, 480))
    if ret == False:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # resmi gri tonlara ceviriyorz
    cars = car_cascade.detectMultiScale(gray, 1.3, 3)

    ##bu cars degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)

    if(cv2.waitKey(20)& 0xFF==ord("q")):
        break


cap.release()
cv2.destroyAllWindows()