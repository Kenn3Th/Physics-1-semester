import numpy as np, matplotlib.pyplot as plt

#konstanter
k = 1.01e-6
D = 10
n = 130
A = 6.5e-3
#data
Stop = np.array([619.51, 449.15, 387.20, 314.92, 227.16, \
                118.74, -51.63, -191.02])
Sbunn = np.array([-562.73, -681.47, -665.98, -650.49, -619.51,\
                  -578.21, -557.56, -485.29])
Itop = np.array([4.41, 3.93, 3.51, 3.03, 2.55, 2.20, 1.74, 1.31])
Ibunn = np.array([-4.48, -4.06, -3.58, -3.17, -2.69, -2.34, \
                  -1.93, -1.45])

deltaS = (np.abs(Stop) + np.abs(Sbunn))/2.0
Im = (np.abs(Itop) + np.abs(Ibunn))/2.0
deltaB = (k*D*deltaS)/(n*A)
B = deltaB/2.0
I = np.linspace(4,0.5,8)

#plott
plt.plot(Im,B*1e3, '*')
plt.legend(['Maalepunkter'], loc = 'best')
plt.title('Magnet felt B mot strom I')
plt.xlabel('Strom I [A]')
plt.ylabel('Magnetfelt B [mT]')
plt.axis([1,4.5,1.5,3.6])
plt.savefig('BvsI.png')
plt.show()




print 'delta B'
print deltaB
print 'delta S'
print deltaS
print 'B'
print B
print 'I'
print Im
