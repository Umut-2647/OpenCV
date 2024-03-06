import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\traffic.avi")

#arka planı cıkarmak icin cagiracagimiz fonksiyon
backsub=cv2.createBackgroundSubtractorMOG2()

##aracları sayacak olan sayac ilk degeri 0 dır
c=0

while True:
    ret,frame=cap.read()
    if ret==False:
        break

    if ret:
        # arka planı cıkarıyor
        fgmask=backsub.apply(frame)
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)

        # burda hierarchy degiskeni ile bazı hataları gidericeğiz
        contours,hierarchy=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #alacagımız bazı hataları gidermek icin kullaniyoruz
        try: hierarchy=hierarchy[0]
        except: hierarchy=[]

        #cok deger dondurdugu icin zip parantezinde aldık
        for contour,hier in zip(contours,hierarchy):
            #contour degiskeni contours degiskeninde her dondugunde konumları buluyoruz
            (x,y,w,h)=cv2.boundingRect(contour)
            #eger bu değerlerdeyse bir araba gectigini anlariz
            if w>40 and h>40 :
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:
                    #arabaları sayar
                    c+=1
        cv2.putText(frame,"car :"+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow("fgmask",fgmask)
        cv2.imshow("Car counter",frame)

        if cv2.waitKey(20) & 0xff==ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
