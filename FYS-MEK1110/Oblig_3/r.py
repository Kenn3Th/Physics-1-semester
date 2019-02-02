from pylab import*
from seaborn import*

#variable
k = 100.0; m = 0.1 #masse og fjaerkonstant
v0 = 0.1; b = 0.1; u = 0.1
time = 2.0; dt = 1/1000.0 #tid og tidssteg
w = sqrt(k/m)
#funksjoner
x = lambda t: u*t - (v0/w)*sin(w*t) #eksakt
xb = lambda t: u*t + b
#Euler-Cromer
n = int(round(time/dt))
t = linspace(0,2,n)
xi = zeros(n)
v = zeros(n)
a = zeros(n)

for i in range(n-1):
    F = k*(xb(t[i]) - xi[i] - b)
    a[i] = F/m
    v[i+1] = v[i] + a[i]*dt
    xi[i+1] = xi[i] + v[i+1]*dt
#plott  
plot(t,x(t),t,xi)
legend(['Eksakt','Euler-Cromer'], loc=0)
title('Eksakt vs Euler-Cromer');xlabel('Tid [s]');ylabel('Posisjon [m]')
savefig('r.png')
show()
