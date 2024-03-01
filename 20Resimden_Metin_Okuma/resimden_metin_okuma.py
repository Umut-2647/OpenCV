from PIL import Image   ##burdaki kutuphanelerin yuklenmesi lazım
import pytesseract

##burda kullanacagımız bilgileri ilerde plaka okumada da goreceğiz


pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img=Image.open("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\text.png") #cv2 kullanmadan resmi calısmamiza dahil ediyoruz

text=pytesseract.image_to_string(img,lang="eng") ##bu fonksiyon resimdeki metni okuyup bir degiskene atiyor

print(text)