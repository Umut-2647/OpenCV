import numpy as np

x=np.array([[1,2,3],[4,5,6]],np.int16) #iki boyutlu bir dizi olusturmus olduk

print(x)
print("------")
"""

print(x[0][1]) #or print(x[0,1])


y=np.array([[1,2,3],[4,5,6],[7,8,9]],np.int16) #uc boyutlu bir dizi olusturmus olduk
print(y)
"""

print(x[:,0]);print(x[:,1]);print(x[:,2]) #sırasıyla ilk sutündaki verileri getirir
print("--------")

print(x[0,:]);print(x[1,:]) #sirasiyla satir satir getirir