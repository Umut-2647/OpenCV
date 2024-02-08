import cv2


img = cv2.imread("klon.jpg")
print(img.shape)

roi = img[15:80, 270:320]


cv2.imshow("image", img)
cv2.imshow("roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()