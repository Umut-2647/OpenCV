import  cv2
import numpy as np

img=cv2.imread("helikopter.jpg",0)

row,col=img.shape

M=np.float32([[1,0,100],[0,1,70]])  #(ilk yataydaki , sonra dikeydeki)
dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("Helikopter",img)
cv2.imshow("Donusum Dizey",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()