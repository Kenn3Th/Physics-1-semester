from numpy import linspace, meshgrid, cos, pi

def streamfun(n=20):
    #Calculate a grid and a streamfunkction
    x=linspace(-0.5*pi,0.5*pi,n)
    # The result is a vector with n elements, from -pi/2 to pi/2
    [X,Y] = meshgrid(x,x)
    psi=cos(X)*cos(Y)

    return X, Y, psi
