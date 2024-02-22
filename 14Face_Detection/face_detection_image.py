import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\face.png") ##oncelikle resmi yukluyoruz

face_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\frontalface.xml")  #bu fonksiyon sayesinde cascade dosyasını calısmamiza dahil ediyoruz

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)       #resimdeki aydınlıgın ve karanlıgın daha rahat tespiti icin resmi gri tonlara ceiviriyoruz

faces=face_cascade.detectMultiScale(gray,1.3,7)   #bu fonksiyon cascade dosyasını kullanarak resim uzerindeki yuzleri bulup koordinatlari degiskene atıyor

##bu faces degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  ##burda bulunan yuze bir dikdortgen ciziyoruyuz

cv2.imshow("Yuz Bolgesi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()