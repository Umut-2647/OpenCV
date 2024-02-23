import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\car.mp4")

_,first_frame=cap.read()      ##burdan ilk frame i cekip diğer framelerle karşılaştıracaz
first_frame=cv2.resize(first_frame,(640,480))
##arka plan çıkarma uygulamalarında gri tonlara çevirmek ve biraz yumuşatmak daha iyi olur

first_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_gray=cv2.GaussianBlur(first_gray,(5,5),0)


while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    diff=cv2.absdiff(first_gray,gray)     ##ilk frame ile diğer frameleri karşılaştıracak ve farkları ortaya koyacak
    _,diff=cv2.threshold(diff,80,255,cv2.THRESH_BINARY)

    cv2.imshow("First_frame",first_frame)
    cv2.imshow("Frame",frame)
    cv2.imshow("Diff",diff)

    if (cv2.waitKey(20) & 0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
