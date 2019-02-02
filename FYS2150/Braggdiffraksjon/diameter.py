import numpy as np
#konstanter
L = 14.0e-2       #cm
dL = 0.3e-2       #cm
lam_c = 2.426e-12 #pm
e = 1.602e-19     #C
m = 9.11e-31      #kg
c = 3e8           #m/s

#verdier
U = np.linspace(3,5,11)*1e3
id1 = [2.72,2.62,2.44,2.32,2.37,2.19,2.10,2.20,2.50,2.00,2.02]
yd1 = [3.32,3.35,3.20,3.05,3.10,2.91,2.83,2.70,2.71,2.63,2.53]
id2 = [4.75,4.78,4.43,4.00,4.34,4.20,4.13,3.99,3.94,3.90,3.57]
yd2 = [5.52,5.44,5.20,5.20,4.94,4.85,4.76,4.67,4.45,4.43,4.39]
id1 = np.array(id1)*1e-2
yd1 = np.array(yd1)*1e-2
id2 = np.array(id2)*1e-2
yd2 = np.array(yd2)*1e-2

def diameter(di,dy):
    n = len(di)
    d = np.zeros(n)
    for i in xrange(n):
        d[i] = (di[i]+dy[i])/2
    return d

def lam(U):
    return lam_c*np.sqrt((m*c**2)/(2*e*U))

def phi(D,lam):
    phi = np.zeros(len(D))
    for i in range(len(D)):
        phi[i] = float(lam[i])/D[i]
    return phi

def sigm(phi):
    n = len(phi)
    d = [i - np.mean(phi) for i in phi]
    s = np.sqrt(np.sum(np.square(d))/n)
    sigm = np.sqrt(1.0/(n-1))*s
    return sigm

#snitt til hver enkelt diamenter
d1_mean = diameter(id1,yd1)
d2_mean = diameter(id2,yd2)
#snitt til snittet til hver eneklet diameter
R1d_mean = np.mean(d1_mean)
R2d_mean = np.mean(d2_mean)
#standardavvik
R1_std = np.std(d1_mean)
R2_std = np.std(d2_mean)
#bolgelengde
bolger = lam(U)
#phi
phi1 = phi(d1_mean,bolger)
phi2 = phi(d2_mean,bolger)
phi1_ = np.mean(phi1)
phi2_ = np.mean(phi2)

"""
print R1_std*1e2
print R2_std*1e2
print R1d_mean*1e2
print R2d_mean*1e2
print bolger*1e12
print np.mean(bolger*1e12)
"""
print np.std(phi1)
print np.std(phi1)/np.sqrt(len(phi1))
print np.std(phi2)
print np.std(phi2)/np.sqrt(len(phi2))
print phi1*1e12
print phi1_*1e12
print phi2*1e12
print phi2_*1e12
