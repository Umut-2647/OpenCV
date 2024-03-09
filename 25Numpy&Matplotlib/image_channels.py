import numpy as np
import matplotlib.pyplot as plt

#rgb olarak okuyor
img=plt.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\map.jpg")

plt.imshow(img)
plt.show()

#resmin butun piksellerindeki r,g,b degerleri
r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]

#dstack fonksiyonu ile daha once elde ettigimiz piksel degerlerini kullanarak orijinal resmi olusturabiliriz
output2=np.dstack((r,g,b))
plt.imshow(output2)
plt.show()



output=[img,r,g,b]

titles=["Image","Red","Green","Blue"]

for i in range(4): # img,r,g,b 0 1 2 3 degisken oldugu icin range(4) yazdık
    plt.subplot(2,2,i+1) #alt grafik olusturuyor
    plt.axis("off") #eksenleri kapatiyoruz
    plt.title(titles[i])
    if i==0:
        plt.imshow(output[i])
    else:
        #aydınlık olan kisimlarda r,g,b oranı daha yuksek demek
        plt.imshow(output[i],cmap="gray")
    plt.show()
