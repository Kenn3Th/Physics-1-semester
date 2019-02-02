import numpy as np
class Linear:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def Gen_linje(self): #y = mx + c
        x = np.array(self.x); y = np.array(self.y)
        x_ = np.mean(x); y_ = np.mean(y) #gjennomsnitt
        x2 = np.sum(np.square(x)); y2 = np.sum(np.square(y))
        D = x2 - 1./(len(x))*(np.sum(x))**2
        E = np.sum(x*y)-1./(len(x))*(np.sum(x)*np.sum(y))
        F = y2 - 1./(len(y))*(np.sum(y))**2
        m = float(E)/D #stigningstallet
        c = y_ - m*x_  #konstantleddet
        dm = np.sqrt(1.0/(len(x)-2)*((D*F-E**2)/D**2))
        dc = np.sqrt(1.0/(len(x)-2)*(D/float(len(x))+x_**2)*((D*F-E**2)/D**2))
        d = np.zeros(len(x)) #residual
        for i in xrange(len(x)):
            d[i] = y[i]-m*x[i]-c
        return c,m,dc,dm,d

    def Lin_gjen_origo(self):
        x = np.array(self.x); y = np.array(self.y)
        x2 = np.sum(np.square(x)); y2 = np.sum(np.square(y))
        xy = np.sum(x*y)
        m = xy/float(x2) #stigningstall
        dm = 1.0/(len(x)-1)*((x2*y2- xy**2)/x2**2) #usikkerhet i stigningtall
        return m,dm

