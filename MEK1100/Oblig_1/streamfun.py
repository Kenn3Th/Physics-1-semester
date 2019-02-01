from numpy import linspace, meshgrid, cos, pi

def streamfun(n=20):
    '''Regner ut et grid og en stromfunksjon'''
     
    x=linspace(-0.5*pi,0.5*pi,n)
    #resultatet er en vektor med n elementer, fra -pi/2 til pi/2
    [X,Y] = meshgrid(x,x)
    psi=cos(X)*cos(Y)

    return X, Y, psi
