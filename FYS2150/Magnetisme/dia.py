import numpy as np, matplotlib.pyplot as plt
from lineaertilpassing import*

#konstanter
mu0 = 4*np.pi*1e-7
A = 1.02e-2
m0 = 390.25e-3
g = 9.81
#raadata
I = np.linspace(0,2.4,13)
dm = np.array([0, -0.02, -0.03, -0.05, -0.08, -0.10, -0.13, -0.17, \
     -0.21, -0.23, -0.26, -0.28, -0.31])*1e-3
B1 = np.array([17.8, 100.0, 186.0, 278.0, 368.0, 443.0,\
      510.0, 577.0, 636.0, 690.0, 728.0, 766.0, 800.0])*1e-3
B2 = np.array([0.3, 0.5, 1.0, 1.5, 1.8, 2.1, 2.3, 2.6, \
               2.3, 2.2, 2.2, 2.3, 2.2])*1e-3

Fz = dm*g
B = np.square(B1)-np.square(B2)
chi = - (Fz*2*mu0)/(A*B)
#print Fz, chi
#usikkerhet
def umulti(z,a,b,da,db):
    dz = np.sqrt(z**2*((da/a)**2+(db/b)**2))
    return dz
def uaddi(da,db):
    dz = np.sqrt(da**2+db**2)
    return dz
def ueksp(z,n,a,da):
    dz = n*(da/a)*z
    return dz

dA = 0.05e-3
dBm = 0.01e-3
dvekt = 0.03e-3

dB12 = ueksp(B1**2,2,B1,dBm)
dB22 = ueksp(B2**2,2,B2,dBm)
dB = uaddi(dB12,dB22)
dchi = umulti(chi,A,B,dA,dB)

B1l = np.log(B1[1:-1])
chil = np.log(chi[1:-1])
#B2 = 0
lin = linear(B1[1:-1],chil)
c,m,dc,Dm,d = lin.Gen_linje()
print m, Dm
#lineaer regresjon
p = np.polyfit(B1[1:-1],chil,1)
fit = np.polyval(p,B1[1:-1])
p2 = np.polyfit(B1,Fz,1)
fit2 = np.polyval(p2,B1)
#plott
plt.plot(B1[1:-1],chil,'*')
plt.plot(B1[1:-1],fit)
plt.xlabel('$B_1$')
plt.ylabel('$\chi$')
plt.legend(['Raadata','Lineaer reggresjon'])
plt.title('Graf av $B_1$ mot log($\chi$)')
plt.savefig('grafvismut.png')
plt.figure()
plt.plot(B1,Fz,'*')
plt.plot(B1,fit2)
plt.title('B-feltet mot kraften $F_z$')
plt.legend(['Maalepunkter','Lineaer regresjon'])
plt.xlabel('$B_1$ [T]')
plt.ylabel('$F_z$ [N]')
#plt.savefig('FzvsB1.png')
plt.show()

lin = linear(B1,Fz)
c,m,dc,Dm,d = lin.Gen_linje()
print m, Dm
