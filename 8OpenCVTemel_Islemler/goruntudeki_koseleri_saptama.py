import cv2
import numpy as np

img1=cv2.imread("C:\\Users\\umuty\\esktop\\OpenCV\\test_images\\text.png")
img2=cv2.imread("C:\\Users\\umuty\\esktop\\OpenCV\\test_images\\contour.png")

gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)
corners=cv2.goodFeaturesToTrack(gray,1000,0.01,10) ##bu fonksiiyonla koseleri tespit ediyoruz

corners=np.intp(corners)

for corner in corners:  ##her koordinat icin donuyor ve koordinaltlara bir cember birakiyor
    x,y=corner.ravel()
    cv2.circle(img2,(x,y),3,(0,0,255),-1)




cv2.imshow("Corner",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()