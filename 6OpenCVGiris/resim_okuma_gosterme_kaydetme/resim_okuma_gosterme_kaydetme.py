import cv2


img=cv2.imread("klon.jpg", ) #0 demek gri şekilde okumak demek

#print(img)

cv2.namedWindow("Image",cv2.WINDOW_NORMAL) #resmi boyutlandırabilir hale getirmek için kullanılır
cv2.imshow("Image",img)
cv2.imwrite("kayit.jpg", img)
cv2.waitKey(0) #herhangi bir tuşa basana kadar veya pencereyi kapatana kadar (içine yazılan değer milisaniyedir)
cv2.destroyAllWindows()


