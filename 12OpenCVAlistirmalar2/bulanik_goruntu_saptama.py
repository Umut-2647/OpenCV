import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Downloads\\starwars.jpg")

blurry_img=cv2.medianBlur(img,1)

laplacian=cv2.Laplacian(blurry_img,cv2.CV_64F).var() # icinde blurlu resmi giriyoruz   ##bu fonksiyon sayesinde resim blurlu olup olmadığını kontrol ediyoruz

#eger bu deger belli bir degerin altındaysa blurlu diyebiliriz

if laplacian<500:
    print("Blurry image")

print(laplacian)

cv2.imshow("Resim",img)
cv2.imshow("Blurry",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()