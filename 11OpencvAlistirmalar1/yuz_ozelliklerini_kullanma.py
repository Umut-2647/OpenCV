import math

import cv2
import numpy as np

cap=cv2.VideoCapture(0)


def findMAxContour(contours):        #maks konturları bulmak için bir fonksiyon tanımlıyoruz
    max_i=0
    max_area=0

    for i in range(len(contours)):
        area_face=cv2.contourArea(contours[i])   ##burda her değer için kontur alanı hesaplanıyor ve if bloğuyla en büyük olan max_area değişkenine aktarılıyor

        if max_area<area_face:
            max_area=area_face
            max_i=i
        try:                                                 ##hata alama ihtimalimiz oldugu için try expect blogu açıyoruz
             c=contours[max_i]  #maks alanı tutacak

        except:
            contours=[0]
            c=contours[0]
        return c



while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)


    roi=frame[180:450,220:500]   ##frame[y1:y2,x1:x2]

    cv2.rectangle(frame,(220,180),(500,450),(0,0,255),0)  #(x1,y1) (x2,y2)

    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color=np.array([0,45,79],dtype=np.uint8)
    upper_color=np.array([17,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,lower_color,upper_color)

    kernel=np.ones((5,5),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)      ##burda görüntüdeki karıncalanmaları yok ediyoruz
    mask=cv2.medianBlur(mask,15)    ##çok daha temiz bir görüntü oluşur

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  ##artık konturları arayabiliriz maskden sonra yazılanlar varsayılan olarak yazılıyor

    if len(contours)>0:              ##hata alama ihtimalimiz oldugu için try expect blogu açıyoruz
        try:
            c=findMAxContour(contours)

            #en sol dendiginde x en kucuk noktası o yuzden argmin kullanıldı
            en_sol=tuple(c[c[:,:,0].argmin()][0])                                            ##bu kısmın görevi bütün konturları dolaşarak en kucuk x leri bulacak

            # en sag dendiginde x en buyuk noktası o yuzden argmax kullanıldı
            en_sag = tuple(c[c[:, :, 0].argmax()][0])

            #0 dendiğinde x lere bakıyor
            en_ust = tuple(c[c[:, :, 1].argmin()][0])
            #1 dendiğinde y lere bakıyor

            en_alt= tuple(c[c[:, :, 1].argmax()][0])

            cv2.circle(roi,en_sol,5,(0,255,0),2)
            cv2.circle(roi,en_sag,5,(0,255,0),2)
            cv2.circle(roi,en_ust,5,(0,255,0),2)
            cv2.circle(roi, en_alt, 5, (0, 255, 0), 2)

            cv2.line(roi, en_ust, en_sol, (255, 0, 0),2)                      #buldugumuz konumları birlestirerek sekil olusturuyoruz
            cv2.line(roi, en_sol, en_alt, (255, 0, 0), 2)
            cv2.line(roi, en_alt, en_sag, (255, 0, 0), 2)
            cv2.line(roi, en_sag, en_ust, (255, 0, 0), 2)

            #buldugumuz sekilden aradaki acıyı hesaplıcaz

            a=math.sqrt((en_sag[0]-en_ust[0])**2+(en_sag[1]-en_ust[1])**2)
            b=math.sqrt((en_alt[0]-en_sag[0])**2+(en_alt[1]-en_sag[1])**2)
            c=math.sqrt((en_alt[0]-en_ust[0])**2+(en_alt[1]-en_ust[1])**2)
        except:
            pass

        try:
            ab_arasi_aci=math.acos((a**2+b**2-c**2)/(2*b*c))*57   ##bu ondalıklı degerler dondurur tam sayi icin inte donusturebilir
            cv2.putText(roi,str(ab_arasi_aci),(en_sag[0]-100,en_sag[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)

        except:
            cv2.putText(roi," ? ",(en_sag[0]-100,en_sag[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)





    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("Mask",mask)
    if(cv2.waitKey(5)& 0xFF==ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
