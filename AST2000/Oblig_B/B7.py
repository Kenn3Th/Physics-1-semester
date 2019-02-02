from pylab import*
from Solmal import*
from seaborn import*

Au = 149597870691   #Astronomisk enhet i meter
SM = 1.98892*10**30 #1 solmasse i kg

time = 0.5  #tidssteg dt
tmax = 330.0  #aar
n = int(round(tmax/time)) #antall tidssteg
n_tid = zeros(n)
g = 4*pi*pi #Gravitasjons konstant i [AU]

planetPos = zeros((2,nr_planeter,n))
xhast = zeros((2,nr_planeter,n))
yhast = zeros((2,nr_planeter,n))

for i in xrange(n-1):
    for j in xrange(nr_planeter):
        n_tid[i+1] = n_tid[i] + time
        planetPos[0,j,0] = pl_x0[j]
        planetPos[1,j,0] = pl_y0[j]
        xhast[0,j,0] = pl_vx0[j]
        yhast[1,j,0] = pl_vy0[j]
        #Euler-Cromer
        r = sqrt(planetPos[0,j,i]**2+planetPos[1,j,i]**2)
        ax = -((g*solMass)/(r**3))*planetPos[0,j,i] 
        ay = -((g*solMass)/(r**3))*planetPos[1,j,i]
        xhast[0,j,i+1] = xhast[0,j,i] + ax*time
        yhast[1,j,i+1] = yhast[1,j,i] + ay*time
        planetPos[0,j,i+1] = planetPos[0,j,i] + xhast[0,j,i+1]*time
        planetPos[1,j,i+1] = planetPos[1,j,i] + yhast[1,j,i+1]*time
      
plot(planetPos[0,0,:],planetPos[1,0,:])
plot(planetPos[0,1,:],planetPos[1,1,:])
plot(planetPos[0,2,:],planetPos[1,2,:])
plot(planetPos[0,3,:],planetPos[1,3,:])
plot(planetPos[0,4,:],planetPos[1,4,:])
plot(planetPos[0,5,:],planetPos[1,5,:])
plot(planetPos[0,6,:],planetPos[1,6,:])
plot(planetPos[0,7,:],planetPos[1,7,:])
plot(0,0,'o',color='yellow')
title('Solsystem "Pjokknes"')
axis((-80,110,-80,80))
legend(['Hjemplanet','planet2','planet3','planet4','planet5','planet6','planet7','planet8', 'Stjerna'])
xlabel('[AU]')
ylabel('[AU]')
show()
        
#system.orbit_xml(planetPos,n_tid)
