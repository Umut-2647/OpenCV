import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("C:\\Users\\umuty\\Desktop\\OpenCV\\test_images\\smile.jpg")

print(img)
#resimdeki min ve maks piksel degerleri
print("Min value :",img.min())
print("Max value :",img.max())
#bu renklerin ortalamasi
print("Mean :",img.mean())
#medyan degeri (median)
print("Median :",np.median(img))
#bu renklerin ortalamasi(average)
print("Ortalama :",np.average(img))