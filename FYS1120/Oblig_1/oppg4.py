from pylab import*

V0 = 10.0           #[V]
e0 = 8.85*10**(-12) #[F/m]
d = 0.01            #[m]
rho = -10**(-5)     #[C/m^3]
E = lambda x: V0/d - (rho*d)/(2*e0) + (x*rho)/e0
V = lambda x: V0 + (-V0/d + (rho*d)/(2*e0))*x - (rho*x**2)/(2*e0)
st = linspace(0,0.01,100)

plot(st,V(st))
xlabel('x = meter')
ylabel('Volt')
title('Graf av V(x)')
show()


q = -1.6*10**(-19)
m = 9.11*10**(-31)
v0 = sqrt(((V(0.005885)*q- V0*q)*2)/m)

print V0/d
