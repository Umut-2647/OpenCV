import numpy as np
import matplotlib.pyplot as plt

#girilen aralikta veri uretiyor
"""
N=11
x=np.linspace(0,10,N)
print(x)

y=x

plt.plot(x,y,"o--")
plt.axis("off") #eksenleri yok ediyor
plt.show()
"""

x=[4,9,5,7,3,10,5]
#y degerim sirasiyla x in icinde donsun ve x in karesini alsin
plt.plot(x,[y**2 for y in x])
plt.show()