import numpy as np, matplotlib.pyplot as plt

n = 1000
x = np.arange(n)
F = np.sin(2*np.pi*x/float(n))
v = np.cos(2*np.pi*x/float(n))*2*np.pi


plt.subplot(2,1,1)    
plt.plot(x/1000.0,F)
plt.title('Posisjon vs tid')
plt.xlabel('Tid [s]')
plt.ylabel('Posisjon [m]')
plt.subplot(2,1,2)
plt.plot(F,v/1000.0)
plt.title('Hastighet vs posisjon')
plt.xlabel('Posisjon [m]')
plt.ylabel('Hastighet [m/s]')
#plt.savefig('opg9.png')
plt.show()
