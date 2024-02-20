import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Downloads\\kamera.jpg")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_black=np.array([0,0,0])
upper_black=np.array([180,255,27])

mask=cv2.inRange(hsv,lower_black,upper_black)

cv2.imshow("Original",img)
cv2.imshow("Mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
