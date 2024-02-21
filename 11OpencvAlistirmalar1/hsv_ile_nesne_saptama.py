import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Downloads\\hsv.mp4")
cap1=cv2.VideoCapture(0)

##trackbar kullanacağımız için boş bir fonksiyona ihtiyacımız var

def nothing(x):
    pass

cv2.namedWindow("trackbar")

cv2.createTrackbar("LH","trackbar",0,179,nothing) #bunun aralığı 0-179 aralığıdır
cv2.createTrackbar("LS","trackbar",0,255,nothing)   #0-255
cv2.createTrackbar("LV","trackbar",0,255,nothing)    #0-255
cv2.createTrackbar("UH","trackbar",0,179,nothing)
cv2.createTrackbar("US","trackbar",0,255,nothing)
cv2.createTrackbar("UV","trackbar",0,255,nothing)

##burda trackbar için lower ve upper değerleri giriyoruz


while 1:
    _,frame=cap1.read()
    frame=cv2.flip(frame,1)  ##bu webcam den alınan goruntuler icin gecerli
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  ##burda frameleri yani webcam deki goruntuleri hsv ye çeviriyoruz


    ##burda yukarda tanımladığımız trackbarleri çağırmak için bir değişkene atayıp getTrackbarPos fonksiyonunu çağırıyoruz

    lh=cv2.getTrackbarPos("LH","trackbar")
    ls=cv2.getTrackbarPos("LS","trackbar")
    lv=cv2.getTrackbarPos("LV","trackbar")
    uh=cv2.getTrackbarPos("UH","trackbar")
    us=cv2.getTrackbarPos("US","trackbar")
    uv=cv2.getTrackbarPos("UV","trackbar")

    lower_color=np.array([lh,ls,lv])    ##yukarda aldığımız değerleri saklıyoruz
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("Bitwise",bitwise)

    if (cv2.waitKey(20) & 0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()