from pylab import*
from seaborn import*

#variable
k = 100.0; m = 0.1; g = 9.81 #masse,fjaer- og gravitasjon-konstant
v0 = 0.1; b = 0.1; u = 0.1
time = 2.0; dt = 1/1000.0 # tid og tidssteg
mud = 0.3; mus = 0.6      # friksjons konstanter
N = m*g #Normalkraften
#funksjon
xb = lambda t: u*t + b
#Euler-cromer
n = int(round(time/dt))
t = linspace(0,2,n)
xi = zeros(n)
v = zeros(n)
a = zeros(n)
for i in range(n-1):
    Ff = k*(xb(t[i]) - xi[i] - b)
    tol = 1E-2
    if abs(v[i]) <= tol:
        if Ff <= mus*N:
            F = 0
        else:
            F = Ff - mud*N
    else:
        F = Ff - mud*N
    a[i] = F/m
    v[i+1] = v[i] + a[i]*dt
    xi[i+1] = xi[i] + v[i+1]*dt
#plott
plot(t,xi)
title('Kloss = 0.1 kg'); xlabel('tid [s]'); ylabel('Posisjon [m]')
savefig('0.1kg.png')
show()
