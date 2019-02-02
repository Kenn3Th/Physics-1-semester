from scipy.constants import*
import numpy as np

me = 511*10**3
def realfaktor(U):
    if 1>U:
        U = np.array(U)
        f = np.zeros(len(U))
        for i in len(U):
            f[i] = 1./np.sqrt(1+(U[i])/(2*me))
    else:
        f = 1./np.sqrt(1+float(U)/(2*me))
    return f
U = 8*10*3
#print realfaktor(U)
#print 1./np.sqrt(1+float(U)/(2*me))

with open('diameter.txt', 'r') as infile:
    U = []
    Dy = []
    for line in infile:
        lst= line.split()
        U.append(float(lst[0]))
        Dy.append(float(lst[1]))
infile.close()

U = np.array(U)
Dy = np.array(Dy)
n = len(U)
N = 1.0/n
lam = (h*c)/(e*U)
phi = [lam[i]/Dy[i]for i in range(n)]
res = [phi[i]-np.mean(phi)]
s = np.sqrt(np.mean(np.square(res)))


phi_mean = np.mean(phi)
Delta_phi = np.sqrt(1.0/(n-1))*s

print phi_mean
print Delta_phi
