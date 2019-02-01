from pylab import*

def hastighet(n):
    t = linspace(-0.5*pi,0.5*pi,n)
    x,y = meshgrid(t,t)
    u = cos(x)*sin(y)
    v = -sin(x)*cos(y)
    return x,y,u,v
