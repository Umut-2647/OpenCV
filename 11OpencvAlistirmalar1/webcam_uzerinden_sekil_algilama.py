import cv2
import numpy as np

def nothing(x):      #trackbar kullanılacağı için boş bir fonksiyona ihtiyacımız var
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Settings")

cv2.createTrackbar("Lower-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Lower-Value","Settings",0,255,nothing)

##burda trackbar için lower ve upper değerleri giriyoruz

cv2.createTrackbar("Upper-Hue","Settings",0,180,nothing)
cv2.createTrackbar("Upper-Saturation","Settings",0,255,nothing)
cv2.createTrackbar("Upper-Value","Settings",0,255,nothing)

font=cv2.FONT_HERSHEY_COMPLEX     ##bulacağımız şeklin adını yazacağımız için font tanımlıyoruz


while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  ##burda frameleri yani webcam deki goruntuleri hsv ye çeviriyoruz

    ##burda yukarda tanımladığımız trackbarleri çağırmak için bir değişkene atayıp getTrackbarPos fonksiyonunu çağırıyoruz
    lh=cv2.getTrackbarPos("Lower-Hue","Settings")
    ls = cv2.getTrackbarPos("Lower-Saturation", "Settings")
    lv = cv2.getTrackbarPos("Lower-Value", "Settings")
    uh = cv2.getTrackbarPos("Upper-Hue", "Settings")
    us = cv2.getTrackbarPos("Upper-Saturation", "Settings")
    uv = cv2.getTrackbarPos("Upper-Value", "Settings")

    lower_color=np.array([lh,ls,lv])   ##yukarda aldığımız değerleri saklıyoruz
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)  ##en son mask uyguluyoruz

    kernel=np.ones((5,5),np.uint8)   ##maskeledikten sonra beyaz nesneler üzerinde oluşan siyah noktaları yok eder
    mask=cv2.erode(mask,kernel)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    ##maskin en son görünütüsüne ulaştıktan sonra conturları arayabiliriz

    for cnt in contours:
        area=cv2.contourArea(cnt)   ##alan hesabi yapiliyor
        epsilon=0.02*cv2.arcLength(cnt,True)   ##deneysel veriler
        approx=cv2.approxPolyDP(cnt,epsilon,True)                       ##bulunan conturlara iyileştirme yapılıyor

        x=approx.ravel()[0]   ## ravel fonk. eğer çok boyutlu bir dizi ise tek satıra döküyor
        y = approx.ravel()[1]    ##buralar konturların başladığı noktadır

        if (area>400):   ##burda belli bir alandan buyukse çizim yaptırıyoruz
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            if (len(approx) == 3):
                cv2.putText(frame, "Ucgen", (x, y), font, 1, (0))
            elif (len(approx) == 4):
                cv2.putText(frame, "Dortgen", (x, y), font, 1, (0))
            elif (len(approx) == 5):
                cv2.putText(frame, "Besgen", (x, y), font, 1, (0))
            elif (len(approx) == 6):
                cv2.putText(frame, "Altigen", (x, y), font, 1, (0))
            else:
                cv2.putText(frame, "Elips", (x, y), font, 1, (0))


    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)

    if(cv2.waitKey(20) & 0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()