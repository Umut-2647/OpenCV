import cv2
import numpy as np

img=cv2.imread("helikopter.jpg",0)

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(img,kernel,iterations=1)
dilation=cv2.dilate(img,kernel,iterations=1)  #kalınlaştırma
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel) #tüm resim üzerindeki gürültüyü kaldırmış
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel) #nesnenin içindeki bozulmalar giderilmiş
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel) #resmin dış kısımını beyaz yapmış geri kalan kısmını ise siyah yapmış
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)


cv2.imshow("Helikopter",img)
"""
cv2.imshow("Erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.imshow("Gradient",gradient)
"""
cv2.imshow("Tophat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()