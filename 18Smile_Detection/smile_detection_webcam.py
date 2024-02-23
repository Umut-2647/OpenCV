import cv2
import numpy as np

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\frontalface.xml")
#bu fonksiyon sayesinde yuz algılama cascade dosyasını calısmamiza dahil ediyoruz

smile_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\smile.xml")
#bu fonksiyon sayesinde gulumseme algılama cascade dosyasını calısmamiza dahil ediyoruz

while 1:
    ret,frame=cap.read()
    if ret==False:
        break
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


    roi_frame=frame[y:y+h,x:x+w]
    roi_gray=gray[y:y+h,x:x+w]

    smiles=smile_cascade.detectMultiScale(roi_gray,1.5,9)

    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    cv2.imshow("Frame",frame)
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()