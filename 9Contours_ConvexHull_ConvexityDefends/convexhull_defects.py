import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\star.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #ilk gri tonlara ceviriyoruz

ret,thresh=cv2.threshold(gray,127,255,0) #gri tonlara cevirdigimiz resmi siyah beyazlara ceviriyoruz

contours,_=cv2.findContours(thresh,2,1) ##konturları buluyoruz

cnt=contours[0]

hull=cv2.convexHull(cnt,returnPoints=False)

defects=cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):   #defects boyutunun 0. elemanı kadar dönsün
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s,0]) #dıstaki kısımlara cizgi ciziyoruz
    end = tuple(cnt[e, 0])
    far = tuple(cnt[f, 0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,5,[0,255,0],-1)   #içe doğru bükülmüş kısımlara birer çember çiziyoruz

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()