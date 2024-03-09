import numpy as np

#3 3 luk bos(gelisiguzel) bir dizi olusturduk  np.uint8 demek negatif sayilar girilmesin demek
x=np.empty([3,3],np.uint8)
print("x :",x)
print("------")

#dizi uc boyutlu olur 5 degeriyle doldurur
y=np.full((3,3,3),dtype=np.int16,fill_value=5)
print("y :",y)
print("-------")

#icine yazilan matrixin tamami 1 lerden olusur
z=np.ones((2,5,5),dtype=np.int8) #beyaz ekrani temsil eder
print("z :",z)

#icine yazilan matrixin tamami 1 lerden olusur
j=np.zeros((2,3,3),dtype=np.int8)   #siyah ekrani temsil eder
print("j :",j)