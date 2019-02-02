import numpy as np, matplotlib.pyplot as plt
from lineaertilpassing import*

lam = 595e-9
L = 30e-3
B = np.array([119.0, 102.0 ,83.0, 63.0, 43.0])
Bn = np.array([-43.0, -63.0, -83.0, -102.0, -119.0])
I = np.array([3.0, 2.5, 2.0, 1.5, 1.0])
In = np.array([-1.0, -1.5, -2.0, -2.5, -3.0])
theta = np.array([44.6, 44.8, 45.6, 46.8, 47.4])
thetan = np.array([50.0, 51.0, 52.0, 52.6, 53.0])

Vp = theta/(L*B)
Vn = thetan/(L*Bn)

plt.plot(B,Vp,'*')
plt.plot(Bn,Vn,'*')
plt.xlabel('Magnetisk flukstetthet B [mT]')
plt.ylabel('Verdet-konstanten')
plt.title('Verdet-konstanten')
plt.legend(['Positiv magnetfelt','Negativ magnetfelt'],\
           loc = 'best')
plt.savefig('verdet.png')
plt.show()

lin = linear(B,Vp)
c,m,dc,Dm,d = lin.Gen_linje()
print m, Dm
lin = linear(Bn,Vn)
c,M,dc,DM,d = lin.Gen_linje()
print M, DM

print (m+M)/2.0, np.sqrt(Dm**2+DM**2)
