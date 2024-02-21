import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Downloads\\eye_motion.mp4")

##bu uygulamayı yapabilmek için göz kısmını rio olarak belirliyoruz

while 1:
    ret,frame=cap.read()
    if ret==False:
        break

    roi=frame[80:210,230:450]
    rows,cols,_=roi.shape  ##burda roi nin shapeleri degiskenlerin icinde tutulacak #+channel degeri de var

    gray=cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret,threshold=cv2.threshold(gray,4,255,cv2.THRESH_BINARY_INV)
    #burda amacımız beyaz olan göz bebeğini siyah yapıp geri kalanları beyaz yapmak olduğu için THRESH_BINARY_INV kullandık

    #simdi ise goz bebeğinin konturlarını bulacagız

    contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours, key= lambda x : cv2.contourArea(x),reverse=True)

    #konturların alanlarına gore sıralama yapacak     #icine girilen foksiyonun degerleri siralar #reverse tam tersi siralar

    for cnt in contours:
        (x,y,w,h)=cv2.boundingRect(cnt)    ##koordinat degerlerini bu fonksiyon sayesinde cekebiliyoruz
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)  ##genislik ve yukseklik
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)

        break

    cv2.imshow("Roi",roi)

    if (cv2.waitKey(80)& 0XFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()