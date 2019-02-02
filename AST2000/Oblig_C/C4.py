from pylab import *

def stjerne(filename):
    lam0 = 656.3
    c = 3*10**8
    
    t = []
    l = []
    f = []
    with open(filename,'r') as infile:
        for line in infile:
            dat = line.split()
            t.append(float(dat[0]))
            l.append(float(dat[1]))
            f.append(float(dat[2]))
    tid = asarray(t)
    lam = asarray(l)
    flux = asarray(f)
         
    vr = ((lam-lam0)/lam0)*c #peculiar velocity
    mvr = mean(vr)           #mean velocityr
    V = vr - mvr             #total hastighet

    starnr = float(filename[4]) + 1

    #plot
    subplot(2,1,1)
    title('Stjerne %d' %starnr)
    plot(tid,V, color = 'purple')
    ylabel('m/s')
    subplot(2,1,2)
    plot(tid,flux, color='orange')
    xlabel('Dager')
    ylabel('Realtiv fluks')
    savefig( 'stjerne%d.png'%starnr)
    show()

    return flux, V

stjerne('star0_1.05.txt')
stjerne('star1_6.20.txt')
stjerne('star2_1.51.txt')
stjerne('star3_1.21.txt')
stjerne('star4_1.34.txt')

Sm =1.9889*10**(30)
G = 6.67*10**(-11)
d = (24*3600)
jm = 1.898*10**(27)
mp = lambda v,ms,p: ((ms**(2./3))*v*(p**(1./3)))/((2*pi*G)**(1./3))

v = [10,25,50,55]
P = [4250,2700,4000,5000]
ms = [1.05,1.51,1.21,1.34]

pm = zeros(len(v))

for i in range(len(v)):
    pm[i] = mp(v[i],ms[i]*Sm,P[i]*d)

print pm
