from pylab import*

x=linspace(-0.5*pi,0.5*pi,30)
X,Y = meshgrid(x,x,indexing='ij')
T = 1 - 0.5*X**2 - 0.5*Y**2
contour(X,Y,T)
xlabel('x-akse')
ylabel('y-akse')
title(r'$T_2\psi = 1-\frac{x^2}{2}-\frac{y^2}{2}$')
savefig('te30.png')
show()
x=linspace(-0.5*pi,0.5*pi,5)
X,Y = meshgrid(x,x,indexing='ij')
T = 1 - 0.5*X**2 - 0.5*Y**2
contour(X,Y,T)
title(r'$T_2\psi = 1-\frac{x^2}{2}-\frac{y^2}{2}$')
xlabel('x-akse')
ylabel('y-akse')
savefig('te5.png')
show()
