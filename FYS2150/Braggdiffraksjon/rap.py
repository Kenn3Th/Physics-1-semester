import numpy as np, matplotlib.pyplot as plt

#konstanter
t = 60
bakgrunn = 5.0
foton = [61,69,58,67,60,50,75,58,66,93,145,177,250,284,319,338,367,368,426,433,446]
f = [i - bakgrunn for i in foton]
theta = np.linspace(12,22,21)
d = 401e-12

#usikkerhet i antall fotoner
def usikkerhet(f):
    res = np.zeros(len(f))
    for i,j in enumerate(f):
        res[i] = np.sqrt(j)
    return res
#formler
def intensitet(f,t):
    f = np.array(f)
    I = np.zeros(len(f))
    for i,j in enumerate(f):
        I[i] = float(j)/t
    return I

def lam(theta,d):
    lam = np.zeros(len(theta))
    for i,j in enumerate(theta):
        lam[i] = d*np.sin(0.5*np.deg2rad(j))
    return lam

def energi(lam):
    hc = 1.241e-6
    E = np.zeros(len(lam))
    for i,j in enumerate(lam):
        E[i] = float(hc)/j
    return E

#verdier
bolge = lam(theta,d)
en = energi(bolge)
intens = intensitet(f,t)

print f
print usikkerhet(f)
print en
print intens
print bolge*1e12

#plott
plt.plot(en*1e-3,intens)
plt.title('Rontgenspektrum')
plt.xlabel('Energi kV')
plt.ylabel('Intensitet')

plt.figure()
plt.plot(bolge,intens)
plt.show()


#alpha
ad = 629e-12
at = 10
alpha = [22,27,24,32,46,43,38,57,39]
a = [i - bakgrunn for i in alpha]
atheta = np.linspace(12,16,9)
abolge = lam(atheta,ad)
aen = energi(abolge)
aint = intensitet(a,t)
"""
#plott
plt.plot(abolge*1e12,aint)
plt.title('Alpha')
plt.xlabel('$\lambda$ pm')
plt.ylabel('Intensitet')
plt.savefig('alpha.png')
"""
#beta
bd = 629e-12
bt = 10
beta = [74,274,267,207,85,99,510,1278,1044,764,80,55,70]
b = [i - bakgrunn for i in beta]
btheta = np.linspace(24,30,13)
bbolge = lam(btheta,bd)
ben = energi(bbolge)
bint = intensitet(b,t)
"""
#plott
plt.figure()
plt.plot(bbolge*1e12,bint)
plt.title('Beta')
plt.xlabel('$\lambda$ pm')
plt.ylabel('Intensitet')
plt.savefig('beta.png')

plt.show()

print 'Alpha'
print abolge*1e12
print 'Beta'
print bbolge*1e12
"""
