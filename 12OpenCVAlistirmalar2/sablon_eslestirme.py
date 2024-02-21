import cv2
import numpy as np

img=cv2.imread("C:\\Users\\umuty\\Downloads\\starwars.jpg")
template=cv2.imread("C:\\Users\\umuty\\Downloads\\starwars2.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_template=cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)

w,h=gray_template.shape[::-1]

result=cv2.matchTemplate(gray_template,gray_img,cv2.TM_CCOEFF_NORMED)  ##burda resim uzerinde sablonun yerini ariyor

location=np.where(result>=0.95)

for point in zip(*location[::-1]): #boyle yapıldığında anlamlı koordinatlar elde ediliyor     ##yükseklik ve genislik olarak alıyor
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)






#cv2.imshow("result",result)   ##beyaz nokta ###
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()