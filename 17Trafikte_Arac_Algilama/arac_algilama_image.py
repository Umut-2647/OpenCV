import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\car.jpg")

##cascade dosyaları her zaman duzgun calısmayabilir
car_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\car.xml")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi gri tonlara ceviriyorz

cars=car_cascade.detectMultiScale(gray,1.1,1)

##bu cars degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik


for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()