import cv2
import numpy as np

# 2. Webcam'den veya harici bir kameradan görüntü almak için 0,1 gibi değerler yazarız. Webcam için bu değer '0' dır.
cap=cv2.VideoCapture(0)

# 3. Kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade=cv2.CascadeClassifier("C:\\Users\\umuty\\Desktop\\OpenCV\\haarCascade\\frontalface.xml")  #bu fonksiyon sayesinde cascade dosyasını calısmamiza dahil ediyoruz

#4. Sonsuz bir döngü ile her kareyi(frame) tek tek inceleyelim.

while 1:
    ret,frame=cap.read() #iki deger dondurur biri dogru okuduysa 1 degerini yanlıs okuduysa 0 degerini digeride frameleri
    frame=cv2.flip(frame,1)  ##daha guzel bir goruntu elde edebilmek icin ters ceviriyoruz

    if ret==False:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #resimdeki aydınlıgın ve karanlıgın daha rahat tespiti icin resmi gri tonlara ceiviriyoruz

    faces=face_cascade.detectMultiScale(gray,1.1,7) #bu fonksiyon cascade dosyasını kullanarak resim uzerindeki yuzleri bulup koordinatlari degiskene atıyor
    ##bu faces degiskeni 4 deger tutar. Sol ust kosenin koordinatları ve genislik ve yukseklik

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)                               ##burda bulunan yuze bir dikdortgen ciziyoruyuz

    cv2.imshow("Frame",frame)
    if cv2.waitKey(5)& 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()