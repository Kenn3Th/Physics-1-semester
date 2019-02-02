from pylab import*
t = linspace(-5,5,501)
X,Y = meshgrid(t,t,indexing='ij')
u = sqrt(X**2 + Y**2)
vx = -4*Y/u; vy = 4*X/u
plot(vx,vy)
show()
