import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Downloads\\map.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))

ret,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) ##önce konturları buluyoruz
hull=[]   ##kontuları saklayacağımız boş bir dizi oluşturuyoruz


for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))  ##0 dan len(contours) a kadar olan degerleri bukup indislerini döndürücek

back_ground=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)


for i in range(len(contours)):
    cv2.drawContours(back_ground,contours,i,(255,0,0),3,8)
    ##burdaki 8 kesinitisiz çizgi demek ve burda konturları çiziyoruz
    cv2.drawContours(back_ground,hull,i,(0,255,0),1,8) #burda ise dışbükeyleri çiziyoruz




cv2.imshow("thresh",thresh)
cv2.imshow("ConvexHull",back_ground)


cv2.waitKey(0)
cv2.destroyAllWindows()