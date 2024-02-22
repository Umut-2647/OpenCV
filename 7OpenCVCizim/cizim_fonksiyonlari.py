import cv2
import numpy as np

#canvas=np.zeros((512,512,3),dtype=np.uint8)  #siyah canva icin

canvas=np.zeros((512,512,3),dtype=np.uint8) +255    #beyaz canva icin


####CİZGİ
cv2.line(canvas,(50,50),(512,512),(255,0,0),5)    #(cizim yapilacak yer,baslangic noktasi,bitis noktasi,cizginin rengi,kalinlik(thickness))
cv2.line(canvas,(100,50),(200,100),(0,0,255),thickness=7)

###DİKDÖRTGEN
cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),2)    #(sol üst köşe)(sağ alt köşe)(renk)(kalinlik)
cv2.rectangle(canvas,(50,50),(150,150),(0,255,0),-1) #dikdörtgenin içinin dolu olmasını istiyorsak -1 yazmalıyız

####DAİRE
cv2.circle(canvas,(250,250),100,(0,0,255),6)           #(merkezi)(yaricap)(renk)(kalinlik)
cv2.circle(canvas,(100,100),20,(255,0,255),-1) ##-1 ici dolu demek


####UCGEN

p1=(120,40)
p2=(50,130)
p3=(20,20)

cv2.line(canvas,p1,p2,(0,0,0),5)  ##olusturdugumuz cizgileri birlestirerek bir sekil olusturur
cv2.line(canvas,p2,p3,(0,0,0),5)
cv2.line(canvas,p1,p3,(0,0,0),5)

#####POLYLİNES FONKSİYONU

points=np.array([[[140,42],[50,150],[20,20],[120,120]]])
cv2.polylines(canvas,[points],True,(0,0,100),4)  #true ya da false olmasi kapalı ya da açık mı olmasını gerektigini söyler


###ELİPS

cv2.ellipse(canvas,(300,300),(100,50), 0, 0, 360, (255, 12, 49), -1)



cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()



