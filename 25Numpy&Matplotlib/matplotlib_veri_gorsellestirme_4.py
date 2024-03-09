import numpy as np
import matplotlib.pyplot as plt


img=plt.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\coins.jpg")

print(img);print("Type :",type(img));print("Shape :",img.shape)

print("Channel degeri :",img.ndim);print("Size :",img.size);print("Data type :",img.dtype)


#rgb olarak dusunuyoruz --> r=0. indis g=1. indis b=2. indis
print("red channel :",img[50,50,0]);print("green channel :",img[50,50,1]);print("blue channel :",img[50,50,2])
#tumunu elde etmek istiyorsak;
print("rgb channel :",img[50,50,:])