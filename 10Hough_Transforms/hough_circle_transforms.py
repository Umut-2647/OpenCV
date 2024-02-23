import cv2
import numpy as np

coins=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\coins.jpg")
balls=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\balls.jpg")

gray_c=cv2.cvtColor(coins,cv2.COLOR_BGR2GRAY)  ##resimleri gri tona ceviriyoruz
gray_b=cv2.cvtColor(balls,cv2.COLOR_BGR2GRAY)

coins_blur=cv2.medianBlur(gray_c,5)  ##resimleri blurluyoruz
balls_blur=cv2.medianBlur(gray_b,5)



circles=cv2.HoughCircles(gray_c,cv2.HOUGH_GRADIENT,1,coins.shape[0]/4,param1=200,param2=10,minRadius=60,maxRadius=90)



##bunun içine girilen değerler oldukça önemlidir

print(circles)  ##içinde çıkan değerler küsüratlı değerlerdir


if circles is not None:
    circles=np.uint16(np.around(circles))  ##circlesin içinde tuttuğu değerleri yuvarlayıp tekrar circles değişkenine atıyoruz
    for i in circles[0,:]:
        cv2.circle(coins,(i[0],i[1]),i[2],(0,255,0),3)

cv2.imshow("Coins",coins)
cv2.waitKey(0)
cv2.destroyAllWindows()










