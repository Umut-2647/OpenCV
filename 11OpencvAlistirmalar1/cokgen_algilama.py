import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX   ##opencv fonts diye aratılabilir
font1=cv2.FONT_HERSHEY_COMPLEX

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\polygons.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  ##ilk resmi graye çeviriyoruz

_,threshold=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  ##ardından threshold uyguluyoruz # (başına alt tre koymamızın sebebi threshold tek deger dondurmuyor)

contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) ##burda thresholdan sonra yazılanlar default olarak yazılabilir

for cnt in contours:
    epsilon=0.01*cv2.arcLength(cnt,True) ##burda konturlara daha da yaklaşıyoruz

    approx=cv2.approxPolyDP(cnt,epsilon,True)

    cv2.drawContours(img,[approx],0,(0),5)

    x=approx.ravel()[0]  ##burda koordinaltları alıyoruz
    y=approx.ravel()[1]

    print(len(approx)) ##burda şeklin kaç köşeli olduğunu söyler

    if (len(approx)==3):
        cv2.putText(img,"Ucgen",(x,y),font,1,(0))
    elif (len(approx)==4):
        cv2.putText(img,"Dortgen",(x,y),font,1,(0))
    elif (len(approx) == 5):
        cv2.putText(img, "Besgen", (x, y), font, 1, (0))
    elif (len(approx) == 6):
        cv2.putText(img, "Altigen", (x, y), font, 1, (0))
    else:
        cv2.putText(img, "Elips", (x, y), font, 1, (0))




cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()