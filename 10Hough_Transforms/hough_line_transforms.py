import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\h_line.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,75,150) ##kenarları buluyoruz



#cv2.HoughLines()   ##bilgisayarı çok yoruyor

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=200)
##içine yazılan sayı boşluğu kapatmaya yeterli ise boşluğu kapatır

#maxLİneGap ile aradaki boşlukları kapatabilirz

for line in lines:   ##burda line[0] diyerek başlangıç ve bitiş noktalarını bularak çizgiyi yaptırıyoruz
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()