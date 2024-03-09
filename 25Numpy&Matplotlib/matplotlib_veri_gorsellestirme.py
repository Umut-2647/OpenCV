import numpy as np
import matplotlib.pyplot as plt


#0 dan 5 e kadar yazdirir (5 dahil degil)
x=np.arange(5)
y=x
print(x)
print(y)

plt.plot(x,y,"o-") #o , o- , o--
plt.plot(x,-y,"o--")
plt.plot(-x,y,"o")
plt.title("y=x, y=-x")
plt.show()
