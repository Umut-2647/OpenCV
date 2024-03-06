import cv2
import numpy as np
import pytesseract
import imutils #bazı goruntu isleme fonksiyonları var

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


img=cv2.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\licence_plate.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  ##resmi gri tonlara ceviriyoruz
filtered=cv2.bilateralFilter(gray,6,250,250)  ##resimdeki keskin hattları yumuşatıyourz

edges=cv2.Canny(filtered,30,200) ##sonra kenarları buluyoruz


contours=cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) ##sonra konturları buluyoruz

cnts=imutils.grab_contours(contours) ##koordinat icindeki uygun konturları yakala demek

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10] #Alana gore ters cevirerek sirala

location=None

for c in cnts: #kapalı bir sekil bulmaya calisiyoruz
    epsilon=0.018*cv2.arcLength(c,True) ##deneysel olarak ispatlanmış, konturlara daha da yaklaşıyoruz
    approx=cv2.approxPolyDP(c,epsilon,True) #bu sayede hataları en aza indiriyoruz
    print(len(approx))
    if len(approx)==4: #4 kose tespit edildiyse bu bir dikdortgendir (plaka)
        location=approx

        break

    # plaka kısmını beyaz yapacagız  screen degiskeni koordinatları tutuyor

mask = np.zeros(gray.shape,np.uint8) #normal resmin buyuklugu kadar bir siyah pencere olusturcak

new_img = cv2.drawContours(mask,[location],0,(255,255,255),-1,)

new_img= cv2.bitwise_and(img, img, mask=mask)

(x,y)=np.where(mask==255)
(topx,topy)=(np.min(x),np.min(y))   ##sadece plakanın oldugumu kısmı gosteriyoruz geri kalan kısmı kırpırıyoruz
(bottomx,bottomy)=(np.max(x),np.max(y))
cropped=gray[topx:bottomx+1,topy:bottomy+1]

text=pytesseract.image_to_string(cropped,lang="eng")
print("Plakanız :",text)


cv2.imshow("Image",img)
cv2.imshow("Mask",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

