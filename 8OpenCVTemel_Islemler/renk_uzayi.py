import cv2


img = cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\klon.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   ##renklerin birbirine donusumu
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.imshow("Klon GRAY",img_gray)
cv2.imshow("Klon HSV",img_hsv)
cv2.imshow("Klon RGB",img_rgb)
cv2.imshow("Klon BGR",img)
cv2.waitKey(0)
cv2.destroyAllWindows()