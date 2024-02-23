import cv2


img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\contour1.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #ilk gri tonlara ceviriyoruz


_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #gri tonlara cevirdigimiz resmi siyah beyazlara ceviriyoruz

contours,_=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) ##sonra konturlar bulunur

cv2.drawContours(img,contours,-1,(0,0,255),3) ##buldugumuz conturları bu fonksiyon sayesinde cizeriz

cv2.imshow("Countours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()