from pylab import*
from seaborn import*

#variable
k = 10.0; m = 0.1; g = 9.81 #masse,fjaer- og gravitasjon-konstant
v0 = 0.1; b = 0.1; u = 0.1
time = 2.0; dt = 1/1000.0 # tid og tidssteg
mud = 0.3; mus = 0.6      # friksjons konstanter
N = m*g #Normalkraften
#funksjon
Ff = lambda t,x: k*(u*t-x) #fjaerkraft
#Euler-cromer
n = int(round(time/dt))
t = linspace(0,2,n)
xi = zeros(n)
v = zeros(n)
a = zeros(n)
for i in range(n-1):
    tol = 1E-2
    if abs(v[i]) <= tol:
        if Ff(t[i],xi[i]) <= mus*N:
            F = 0
        else:
            F = Ff(t[i],xi[i]) - mud*N
    else:
        F = Ff(t[i],xi[i]) - mud*N
    a[i] = F/m
    v[i+1] = v[i] + a[i]*dt
    xi[i+1] = xi[i] + v[i+1]*dt

    #plott
subplot(2,1,1)
plot(t,xi)
title('Kloss'); ylabel('Posisjon [m]')
subplot(2,1,2)
plot(t,Ff(t,xi))
title('fjaerkraft');xlabel('tid [s]'); ylabel(r'N [$\frac{kgm}{s^2}$]')
savefig('10N.png')     
show()
