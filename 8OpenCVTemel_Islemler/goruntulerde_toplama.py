import cv2
import numpy as np


circle=np.zeros((512,512,3) , np.uint8)+255   ##cemberin cizilecegi yeri olusturuyoruz
cv2.circle(circle,(256,256),60,(255,0,0),-1)


rectangle=np.zeros((512,512,3) , np.uint8)+255    #dikdortgenin cizilecegi yeri olusturuyoruz
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,255),-1)

add=cv2.add(circle,rectangle)  ##birbirine ekliyor ve olusan sekli ve rengi gosteriyor
print(add[256,256])


cv2.imshow("Circle",circle)
cv2.imshow("Rectangle",rectangle)
cv2.imshow("Add",add)
cv2.waitKey(0)
cv2.destroyAllWindows()