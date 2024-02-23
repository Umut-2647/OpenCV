import cv2
import numpy as np

def nothing(x):  #trackbar kullanacağımız icin bos bir fonksiyona ihtiyacımız var
    pass

img1=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\aircraft.jpg")

img1=cv2.resize(img1,(640,480))                     ##resimlerin ayni boyutta olamsı lazım

img2=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\balls.jpg")

img2=cv2.resize(img2,(640,480))


output=cv2.addWeighted(img1,0.5,img2,0.5,0)        ##resimlerin ağırlıklarını birbiri üzerine ekleme (Ubiri daha seffaf gibi)
cv2.namedWindow("Resim Donusum")

cv2.createTrackbar("Alpha-Beta","Resim Donusum",0,1000,nothing)

while True:
    cv2.imshow("Resim Donusum",output)

    alpha=cv2.getTrackbarPos("Alpha-Beta","Resim Donusum")/1000
    beta=1-alpha

    ##sureklı degisecek
    output=cv2.addWeighted(img1,alpha,img2,beta,0)

    print(alpha,beta)

    if cv2.waitKey(1)==27:         #yani esc ye basıldığında
        break

cv2.destroyAllWindows()