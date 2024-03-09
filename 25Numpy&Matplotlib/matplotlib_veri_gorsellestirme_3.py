import numpy as np
import matplotlib.pyplot as plt


x=np.arange(3)
print(x)
#y degerim sirasiyla x in icinde donsun ve x in karesini alsin
plt.plot(x,[y**2 for y in x])

#y degerim sirasiyla x in icinde donsun ve x in kupunu alsin
plt.plot(x,[y**3 for y in x])

plt.plot(x,2*x)
plt.plot(x,5.2*x)
#bu fonksiyon ile hangi cizginin hangi fonksiyona ait oldugunu ogrenicez

plt.legend(["x**2","x**3","x*2","x*5.2"],loc="upper center")
#upper right/center/left
#lower right/center/left

plt.grid(True) #ızgara eklensin demek

#eksenlere ad veriyoruz

plt.xlabel("x=np.arrange(3)")
plt.ylabel("y=f(x)")

#x ve y deki minimum ve maksimum degerleri verir
print(plt.axis())

#ilk iki arguman x in min ve maks noktasini son iki arguman ise y nin min ve maks noktasi olacak
plt.axis([0,2,0,10])

# figuru kaydetmemizi saglar, figuru kaydedecegimiz yer ve adi
plt.savefig("C:\\Users\\umuty\\Desktop\\OpenCV\\fig.png")
plt.show()
