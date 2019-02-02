#i)
import numpy as np, matplotlib.pyplot as plt

F = 400; fc = 488; fv = 25.8 #kreftene som vikrere [N], fv = psykisk kraft[sN/M]
m = 80.0   #[kg]
p = 1.293  #luft tetthet
A = 0.45   #Arealet til loeperen
Cd = 1.2   #Drag koeffisient
w = 0      #Luft hastighet
time = 10  #tid
tc = 0.67  #tids koeffisient som er brukt til aa regne ut funksjoner
dt = 1./1000; #tids steg
n = int(time/dt) 
a = np.zeros(n); t = np.zeros(n) 
x = np.zeros(n); v = np.zeros(n)
v[0] = 0; x[0] = 0; t[0] = 0 #initial verdier
q = 0 #teller, naar den naar hundre stopper for loopen

D = lambda t,v: A*(1 - 0.25*np.exp(-(t/tc)**2))*0.5*p*Cd*(v-w)**2 #luftmotstand
Fv = lambda v: -v*fv #Psykisk
Fc = lambda t: fc*np.exp(-(t/tc)**2) #fra kroket til staande funksjon
             
for i in range(int(n-1)):
    a[i] = (F + Fc(t[i]) + Fv(v[i]) - D(t[i],v[i]))/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i+1]*dt
    t[i+1] = t[i] + dt
    if x[i+1] > 100:
        q = i + 1
        break

plt.subplot(3,1,1)
plt.title('Bevegelses diagram')
plt.plot(t[0:q],x[0:q])
plt.ylabel('x [m]')
plt.subplot(3,1,2)
plt.plot(t[0:q],v[0:q])
plt.ylabel('v [m/s]')
plt.subplot(3,1,3)
plt.plot(t[0:q],a[0:q])
plt.ylabel('a [m/s^2]')
plt.xlabel('t [sekund]')
plt.show()

