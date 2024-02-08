import cv2
import numpy as np

img=cv2.imread("klon.jpg")


dimension=img.shape
print(dimension)

color=img[477, 849]
print("BGR",color)

blue=img[477, 849,0]
print("blue :",blue)

green=img[477, 849,1]
print("green :",green)

red=img[477, 849,2]
print("red :",red)

img[477, 849,0]=250
print("new blue: ",img[477, 849,0])




cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()