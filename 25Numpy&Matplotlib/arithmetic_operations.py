import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\map.jpg")

# ilk deger kaca kaclık oluscagını soyluyor ikinci deger ise kacinci siraya konulacagini belirliyor

plt.subplot(4, 2,1) # alt grafik olusturuyor
plt.title("Original image")
plt.imshow(img)


plt.subplot(4, 2,2)
plt.title("img+img")
plt.imshow(img+img)


plt.subplot(4, 2,3)
plt.title("img-img") #ayni resimleri birbirinden cikartirsak eger siyah ekran olusur
plt.imshow(img-img)


plt.subplot(4, 2,4)
plt.title("np.flip((img,0))")
plt.imshow(np.flip(img,0)) #0 1 ve 2 olabilir : 0 x eksenine gore yansimasi demek


plt.subplot(4, 2,5)
plt.title("np.flip((img,1))")
plt.imshow(np.flip(img,1)) #0 1 ve 2 olabilir : 1 y eksenine gore yansimasi demek


plt.subplot(4, 2,6)
plt.title("np.flip((img,2))")
plt.imshow(np.flip(img,2)) #0 1 ve 2 olabilir : 2 renk formati degisiyor demek


plt.subplot(4, 2,7)
plt.title("np.fliplr(img,2)") #left to righ  (bi nevi y eksenine gore yansimasi)
plt.imshow(np.fliplr(img))


plt.subplot(4, 2,8)
plt.title("np.flipud((img)") #up down (bas asagiya demek)  (bi nevi x eksenine gore yansimasi)
plt.imshow(np.flipud(img))



plt.show()