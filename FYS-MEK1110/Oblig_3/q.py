from pylab import*
from seaborn import*

#variable
k = 100.0
m = 0.1; v0 = 0.1; b = 0.1 # masse[kg],hastighet[m/s]og Fjaerkonstant[N/m]
time = 2.0; dt = 1/200.0   # Tid [s] + tidssteg
#funksjoner til Euler-Cromer
n = int(round(time/dt))
t = linspace(0,2,n)        #liste me alle tidsstegene fra start til slutt
xi = zeros(n); v = zeros(n); a = zeros(n)
v[0] = 0.1 
for i in range(n-1):
    F = -k*xi[i]
    a[i] = F/m
    v[i+1] = v[i] + a[i]*dt
    xi[i+1] = xi[i] + v[i+1]*dt
#eksakt funksjon
w = sqrt(k/m)
x = lambda t: (v0/w)*sin(w*t)
#plott
subplot(2,1,1)    
plot(t,x(t))
title('Eksakt')
subplot(2,1,2)
plot(t,xi,'r')
title('Euler-Cromer'); xlabel('x-akse'); ylabel('y-akse')
savefig('q.png')
show()

