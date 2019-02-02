from numpy import*
from numpy.linalg import norm
def Bmak(S):
    k = 1.18*10**(-6)
    D = 10
    A = 2*pi*(pi*(4.3*10**(-3))**2)
    return (k*D*S)/A

def Hmaks(I):
    N = 460
    R = 58
    return (N*I)/(2*pi*R)

bta = [[4.72,4.77],[4.15,4.77],[2.86,2.91],[2.22,2.25],[1.35,1.46],[0.83,0.87]]
bta = array(bta)
btavg = average(bta,axis=1)
hmaxer = Hmaks(btavg)

sdiff = array([[1996.25-1376.63],[1642.18-1031],[2133.45-1531.53],[2248.52-1673.16],[2295-1779.27],[2315.63-1921.72]])
bmaxer = Bmak(sdiff)
print bmaxer
print hmaxer
print btavg
