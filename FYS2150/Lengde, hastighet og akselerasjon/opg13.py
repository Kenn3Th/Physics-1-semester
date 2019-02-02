import numpy as np, matplotlib.pyplot as plt
from linjetilpasning import*

#generell linje
def Gen_linje(x,y):
    x = np.array(x); y = np.array(y)
    x_ = np.mean(x); y_ = np.mean(y) #gjennomsnitt
    x2 = np.sum(np.square(x)); y2 = np.sum(np.square(y))
    D = x2 - 1./(len(x))*(np.sum(x))**2
    E = np.sum(x*y)-1./(len(x))*(np.sum(x)*np.sum(y))
    F = y2 - 1./(len(y))*(np.sum(y))**2
    m = float(E)/D #stigningstallet
    c = y_ - m*x_  #konstantleddet
    dm = np.sqrt(1.0/(len(x)-2)*((D*F-E**2)/D**2))
    dc = np.sqrt(1.0/(len(x)-2)*(D/float(len(x))+x_**2)*((D*F-E**2)/D**2))
    return c,m,dc,dm
#linje gjennom origo
def lin_gjen_origo(x,y):
    x = np.array(x); y = np.array(y)
    x2 = np.sum(np.square(x)); y2 = np.sum(np.square(y))
    xy = np.sum(x*y)
    m = xy/float(x2) #stigningstall
    dm = 1.0/(len(x)-1)*((x2*y2- xy**2)/x2**2) #usikkerhet i stigningtall
    return m,dm

konst,stig,ukonst,ustig = Gen_linje(x,y)

print m,c 
print stig,konst
print ustig,ukonst

"""
Jeg skrev om MATLAB skriptet til python kode.
om mulig laster jeg den opp sammen med denne koden (linjetilpasning.py)
hvis du prover aa kjore koden er den viktig. Om det ikke gaar send en mail
skal jeg sende den. Har lagt ved et kjore eksempel under.

Her er m og c konstantledd og stigningstallet som linjetilpasning.py
gir meg, (med andre ord polyfit)
stig og konst er stigningstallet og konstantleddet koden min gir meg.
I tillegg er ukonst og ustig usikkerheten i konstantleddet og
stigningstallet.

kjore eksempel:
terminal << python opg13.py 
4.8175370155 3.89131005522
4.8175370155 3.89131005522
0.321947775641 0.376371499977

som vi ser er min funksjons konstantled og stigningstall identisk til
polyfit sin. De to siste tallene er min kalkulerte usikkerhet i
stigningstall og konstantledd.
Jeg har tatt utgangspunkt i formelene paa side 39 i squires til funksjonen min
"""
