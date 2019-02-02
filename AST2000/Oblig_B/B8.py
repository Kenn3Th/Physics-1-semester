from pylab import*
from Solmal import*

SM = 1.98892*10**30          #solmasse i kg
dt = 0.5
tmax = 10**7
n = int(round(tmax/dt))
n_times = zeros(n)
satPos = zeros((n,2))
v = zeros((n,2))
a = zeros((n,2))
tegn = zeros((n,2))          #tegne radius til planet
planet = 4                   #planet
rh = rho[planet]             #Atmospheric density at surface [kg/m^3]
M = Mass[planet]*SM          #massen til planeten [kg]
m = 100.0                    #massen til satelitten [kg]
A = (2*pi*(0.5**2))          #Areal til fallskjerm
rad = Radius[planet]*1000    #Radius til planeten
limit = 2.5*10**4            #Fd grense

#Formler
g = lambda x,r: ((G*M)/r**3)*x            #Gravitasjon akselerasjon
p = lambda H,Hs: rh*(e**(-(H/float(Hs)))) #rho med hensyn paa h
fd = lambda p,v: (p*A*v**2)/2.0           #drag force Fd

#initial verdier
satPos[0,1] = rad + 4*10**7 #hoyde over overflaten [km] (y-retning)
a[0,1] =g(satPos[0,1],sqrt(satPos[0,0]**2+satPos[0,1]**2))
a[0,0] =g(satPos[0,0],sqrt(satPos[0,0]**2+satPos[0,1]**2))
orbv = sqrt(a[0,1]*satPos[0,1])
v[0,0] = 1000.5
gr = G*M/rad**2

#Euler-Cromer
for i in xrange(n-1):
    n_times[i+1] = n_times[i] + dt
    h = sqrt(satPos[i,0]**2+satPos[i,1]**2)
    hs = 75200.0/gr*m
    r = sqrt(satPos[i,0]**2+satPos[i,1]**2)
    evx = - (v[i,0]/norm(v[i]))
    evy = - (v[i,1]/norm(v[i]))
    tegn[i,0] = rad*evx
    tegn[i,1] = rad*evy
    if fd(p(h,hs),norm(v[i])) >= limit:
        print'start hoyde'
        print satPos[0,1]
        print'slutt'
        print satPos[i,1]
        print 'Fd'
        print fd(p(h,hs),sqrt(v[i,0]**2+v[i,1]**2))
        break
    elif sqrt(satPos[i,0]**2+satPos[i,1]**2) <= rad:
        print 'kraesj'
        print 'Fd : %.2f' %fd(p(h,hs),sqrt(v[i,0]**2+v[i,1]**2))
        print 'Hastighet: %.4f km/t' %(norm(v[i])*3.6)
        print 'Tid: %.2f t' %(n_times[i]/3600.0)
        break
    else:
        a[i,0] = -g(satPos[i,0],r) + (p(h,hs)*A*norm(v[i])**2)/(2*m)*evx
        a[i,1] = -g(satPos[i,1],r) + ((p(h,hs)*A*norm(v[i])**2)/(2*m))*evy
        v[i+1,0] = v[i,0]+a[i,0]*dt
        v[i+1,1] = v[i,1]+a[i,1]*dt
        satPos[i+1,0] = satPos[i,0] + v[i+1,0]*dt
        satPos[i+1,1] = satPos[i,1] + v[i+1,1]*dt

print 'gravitasjons akselerasjon : %.2f' %(G*M/rad**2)

vi = zeros(n)
time = zeros(n)
for i in xrange(n):
    vi[i] = sqrt(v[i,0]**2+v[i,1]**2)*3.6
    time[i] = n_times[i]/3600.0
   
subplot(2,1,1)
plot(satPos[:,0],satPos[:,1])
plot(tegn[:,0],tegn[:,1])
legend(['Satellitt bane','Planet'])
title('Satellitt landing')
ylabel('meter')
subplot(2,1,2)
plot(time[::100],vi[::100])
xlabel('time')
ylabel('km/t')
title('Hastighets graf')
#axis([0,150,0,6500])
savefig('jord_A=50v=2500.png')
show()

#system.landing_sat(satPos[::100],n_times[::100],planet)
