import cv2


cv2.namedWindow("Image")
img=cv2.imread("klon.jpg")
cv2.resize(img,(640,480))
cv2.imshow("Image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()