import cv2

img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #ilk gri tonlara ceviriyoruz
_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  #gri tonlara cevirdigimiz resmi siyah beyazlara ceviriyoruz

M=cv2.moments(thresh)
#print(M) ##asagıda yazdıgımız degerlerden burdan geliyor

X=int(M["m10"]/M["m00"])  ##agırlık mnerkezini buluyoruz

Y=int(M["m01"]/M["m00"])

cv2.circle(img,(X,Y),5,(255,255,0),-1) #buldugumuz degerlere cember ciziyoruz

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
