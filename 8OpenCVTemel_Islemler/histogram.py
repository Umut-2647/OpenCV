import cv2
import numpy as np
from matplotlib import pyplot as plt  #eğer yüklü değilse cmd =>  pip install matplotlib


img=cv2.imread("helikopter.jpg")

"""
img=np.zeros((500,500),np.uint8)
cv2.rectangle(img,(0,60),(200,160),(255,255,255),-1)
cv2.rectangle(img,(200,160),(350,270),(255,255,255),-1)
"""

b,g,r=cv2.split(img)


cv2.imshow("Img",img)

#plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

