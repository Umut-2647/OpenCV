import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\helikopter.jpg",0)

ret,th1=cv2.threshold(img,120,255,cv2.THRESH_BINARY) ##siyah ve beyazlara cevirir(0 ve 1)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#gaussion daha ayrintili yapiyor

cv2.imshow("Helikopter",img)
cv2.imshow("img_th1",th1)
cv2.imshow("img_th2",th2)
cv2.imshow("img_th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()