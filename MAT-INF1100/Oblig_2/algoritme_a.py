import numpy as np
import matplotlib.pyplot as plt

class pos_aks:

    def __init__(self, t, v):
        self.t, self.v = t, v
#a)
    def aks(self):
        t = np.array(self.t); v = np.array(self.v)
        a = np.zeros(len(t))
        for i in xrange(1,len(t)):
            a[i] = (v[i]-v[i-1])/(t[i]-t[i-1])
        return a
#b)
    def pos(self):
        t = np.array(self.t); v = np.array(self.v)
        s = np.zeros(len(v))

        for i in xrange(1,len(t)):
            s[i] = s[i-1] + (((v[i-1])+(v[i]))/2.0)*(t[i]-t[i-1])
            
        return s


t = []; v = []

infile = open('running.txt','r')
for line in infile:
    tnext, vnext = line.strip().split(',')
    t.append(float(tnext)), v.append(float(vnext))
infile.close()

#c)
ap = pos_aks(t,v)
a = ap.aks()
p = ap.pos()

plt.subplot(2,1,1)
plt.plot(t,a)
plt.title('Akselerasjon graf')
plt.ylabel('a(t)')
plt.legend(['akselerasjon'])
plt.subplot(2,1,2)
plt.plot(t,p,'black')
plt.title('Posisjon graf')
plt.axis([0,7000,0,2.8e4])
plt.xlabel('t')
plt.ylabel('s(t)')
plt.legend(['posisjon'])
plt.show()
