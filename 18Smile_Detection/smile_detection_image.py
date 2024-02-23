import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\smile.jpg")

##mantık su sekilde ilk once yuz tespit edilcek yuz tespit edildikten sonra gulumsemeler aranacak bu yuzden her iki haar cascade de eklenecek

face_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\frontalface.xml")
#bu fonksiyon sayesinde yuz algılama cascade dosyasını calısmamiza dahil ediyoruz

smile_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\smile.xml")
#bu fonksiyon sayesinde gulumseme algılama cascade dosyasını calısmamiza dahil ediyoruz


gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi gri tonlara ceviriyorz

faces=face_cascade.detectMultiScale(gray,1.3,7)   #bu fonksiyon cascade dosyasını kullanarak resim uzerindeki yuzleri bulup koordinatlari degiskene atıyor

##bu smiles degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)  ##burda bulunan yuze bir dikdortgen ciziyoruyuz


img2=img[y:y+h,x:x+w]       #yukarda dikdortgen cizdigimiz degerleri yaziyoruz       #yuzlerin yakalandıgı bolgeyi tutacak
gray2=gray[y:y+h,x:x+w]

smiles=smile_cascade.detectMultiScale(gray2,1.1,7)

for (sx,sy,sw,sh) in smiles:
    cv2.rectangle(img2,(sx,sy),(sx+sw,sy+sh),(0,255,0),2)


cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()