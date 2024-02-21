import cv2
import numpy as np

img1=cv2.imread("C:\\Users\\umuty\\Downloads\\aircraft.jpg")
img1=cv2.resize(img1,(640,700))

img2=cv2.imread("C:\\Users\\umuty\\Downloads\\aircraft1.jpg")
img2=cv2.resize(img2,(640,700))

img3=cv2.medianBlur(img1,7)

##pikselleri eşit olmalıdır çünkü eğer pikseller esit değilse resimler zaten farklı resimler olarak kabul edilir

#eger her piksellerin renk degerleri birbirine esitse bu resimler esittir

"""
if (img1.shape==img2.shape):
    print("same size")
else :
    print("not same size")
"""

#difference den gelir

diff=cv2.subtract(img1,img3)   ##icine girilen iki resmin farkını bulup degiskene atar #aynı olan yerleri siyaha boyar farklı olan yerleri beyaza boyar

b,g,r=cv2.split(diff)

# countNonZero fonksiyonu icine girilen degeri tek tek kontrol edip kac tane 0 olmadığını sayar

if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("Completely equal")
else:
    print("NOT Completely equal")


cv2.imshow("Resim",img1)
cv2.imshow("Resim1",img2)
cv2.imshow("Difference",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()