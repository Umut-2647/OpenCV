import cv2
import numpy as np

cv2.namedWindow("Live Video")

cap=cv2.VideoCapture(0)
print("Width :"+str(cap.get(3)))  #get fonksiyonun icine 3 yazildigi zaman enini verir
print("Height :"+str(cap.get(4)))  #get fonksiyonun icine 4 yazildigi zaman yüksekliği verir

cap.set(3,1280)
cap.set(4,720)

print("Width* :"+str(cap.get(3)))
print("Height* :"+str(cap.get(4)))   ##degisen degerler


while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    if ret==False:
        break

    cv2.imshow("Live Video",frame)

    if(cv2.waitKey(1) &  0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()