import numpy as np, matplotlib.pyplot as plt

n = 1000
x = np.arange(n)
F = np.abs(np.sin(4*np.pi*x/float(n)))
v = np.cos(4*np.pi*x/float(n))*4*np.pi

plt.subplot(2,1,1)    
plt.plot(x/1000.0,F)
plt.title('Posisjon vs tid')
plt.xlabel('Tid [s]')
plt.ylabel('Posisjon [m]')
plt.subplot(2,1,2)
plt.scatter(1,0,color='orange')
plt.plot(F,v/1000.0)
plt.scatter(0,0.0125, color='green')
plt.scatter(0,-0.0125, color='green')
plt.title('Hastighet vs posisjon')
plt.xlabel('Posisjon[m]')
plt.ylabel('Hastighet[m/s]')
#plt.savefig('opg10.png')
plt.show()
