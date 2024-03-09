import cv2
import numpy as np
import matplotlib.pyplot as plt


#bgr formatta okuyor
img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\smile.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(img) #rgb olarak gosteriyor
plt.show()

#gri formatta gostermek icin;
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

plt.imshow(img,cmap="gray",interpolation="BICUBIC") #rgb olarak gosteriyor
plt.show()
