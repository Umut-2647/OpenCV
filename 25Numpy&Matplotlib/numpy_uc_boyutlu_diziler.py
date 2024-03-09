import numpy as np

#iki tane duzlemli dizi ekledikten sonra basa ve sona birer dizi isareti daha koyuyoruz
x=np.array([ [[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]] ],np.int16)
print(x)              #0. nci index          #1. nci index
print("------")
print(x[0,0,0])
print(x[0,1,0])
print(x[1,1,1])