import cv2


img = cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\klon.jpg")
print(img.shape)

roi = img[15:80, 270:320] ##girilen degerlerde kalan kısmı gosterir


cv2.imshow("image", img)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()