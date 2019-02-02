from pylab import*

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

    starnr = filename[4]
    """
    #plot
    subplot(2,1,1)
    title('Stjerne' + starnr)
    plot(tid,V, color = 'purple')
    ylabel('m/s')
    subplot(2,1,2)
    plot(tid,flux, color='orange')
    xlabel('Dager')
    ylabel('Realtiv fluks')
    savefig( starnr + '.png')
    show()
    """

    return flux, V

v_r = lambda t,t0,P,vr: vr*cos((2*pi)/P*(t-t0))

V,fl = stjerne('star4_1.34.txt')
T = 20
t_0 = linspace(3500,4000,T)
V_r = linspace(40,60,T)
P = linspace(3500,8500,T)

def delta(t0,p,vr):
    de = []
    d_min = 1
    I = 0
    J = 0
    K = 0
    for i in range(len(t_0)):
        for j in range(len(P)):
            for k in range(len(V_r)):
                d = sum(V[i]-v_r(T,t_0[i],p[j],V_r[k]))**2
                de.append(d)
                if d < d_min:
                    d_min = d
                    I = i
                    J = j
                    K = k
                
    delta = asarray(de)
    return delta, I, J, K

Sm =1.9889*10**(30)
G = 6.67*10**(-11)
d = (24*3600)
jm = 1.898*10**(27)
ms = 1.34*Sm
mp = lambda v,ms,p: ((ms**(2./3))*v*(p**(1./3)))/((2*pi*G)**(1./3))
    
D, I, J, K = delta(t_0,P,V_r)
Delta = min(D)
print 'Delta = %.14f i = %i j = %i k = %i'%(Delta,I,J,K)
print 't_0 = %.2f P = %.2f v_r = %.2f' %(t_0[I],P[J],V_r[K])

p_m_k = mp(V_r[K],ms,P[J]*d)
p_m_g = mp(55,ms,5000*d)

print 'massen til planeten kalkulert ved kun aa studere grafen = %.2f Jupiter masse' %(p_m_g/jm)
print 'massen til planeten kalkulert med minste kvadratiske metode = %.2f Jupiter masse' % (p_m_k/jm)
print 'forskjellen mellom bye-eye og minste kvadratisk metode = %.2f'%((p_m_g/jm)-(p_m_k/jm))
