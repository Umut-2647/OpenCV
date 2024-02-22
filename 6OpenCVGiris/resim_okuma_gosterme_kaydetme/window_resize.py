import cv2


cv2.namedWindow("Image")  #ımage adlı pencere olusturup resmi o pencerede gostericek
img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\klon.jpg" )
cv2.resize(img,(640,480))  ##burda resmi tekrardan boyutluyor
cv2.imshow("Image",img)
cv2.waitKey(0)

cv2.destroyAllWindows()