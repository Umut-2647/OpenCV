import  cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\helikopter.jpg",0)

row,col=img.shape

M=cv2.getRotationMatrix2D((col/2,row/2),90,1)
#burda col ve row degeri bir arguman olarak yazılıyor     #(ilk sutun,sonra satır) +saat yonunun tersi
dst=cv2.warpAffine(img,M,(col,row))

cv2.imshow("Original",img)
cv2.imshow("DST",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()