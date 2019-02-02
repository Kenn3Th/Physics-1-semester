from pylab import*
from Solmal import*
from seaborn import*

time = 0.05  #tidssteg dt
tmax = 330.0  #aar
n = int(round(tmax/time)) #antall tidssteg
n_tid = zeros(n)
g = 4*pi*pi #Gravitasjons konstant i [AU]

#Center of Mass
m_planeter = [Mass[0], Mass[2], Mass[3]] #sum = 6.2e^-4 [solmasser]
pX_0 = [pl_x0[0],pl_x0[2],pl_x0[3]]    #x_0 planeter
pY_0 = [pl_y0[0],pl_y0[2],pl_y0[3]]    #y_0 planeter
vX_0 = [pl_vx0[0],pl_vx0[2],pl_vx0[3]] #vx_0 planeter
vY_0 =[pl_vy0[0],pl_vy0[2],pl_vy0[3]]  #vy_0 planeter
#Stjerne 
StarPos = zeros((2,1,n))
s_hast = zeros((2,1,n))
M = solMass
#Planeter
planetPos = zeros((2,len(m_planeter),n))
hast = zeros((2,len(m_planeter),n))

for i in xrange(n-1):
    for j in xrange(len(m_planeter)):
        n_tid[i+1] = n_tid[i] + time
        planetPos[0,j,0] = pX_0[j]
        planetPos[1,j,0] = pY_0[j]
        hast[0,j,0] = vX_0[j]
        hast[1,j,0] = vY_0[j]
        
        r = sqrt(planetPos[0,j,i]**2+planetPos[1,j,i]**2)
        #Krefter
        F1 = (G*(M*m_planeter[0])/r**3)*(planetPos[:,0,i]-StarPos[:,0,i])
        F2 = (G*(M*m_planeter[1])/r**3)*(planetPos[:,1,i]-StarPos[:,0,i])
        F3 = (G*(M*m_planeter[2])/r**3)*(planetPos[:,2,i]-StarPos[:,0,i])
        #Euler-Cromer
        a = -((g*solMass)/(r**3))*planetPos[:,j,i] 
        hast[:,j,i+1] = hast[:,j,i] + a*time
        planetPos[:,j,i+1] = planetPos[:,j,i] + hast[:,j,i+1]*time

    
    #Euler-Cromer, star
    a_star = (F1+F2+F3)/M    
    s_hast[:,0,i+1] = s_hast[:,0,i] + a_star*time
    StarPos[:,0,i+1] = StarPos[:,0,i] + s_hast[:,0,i+1]*time


vr = s_hast[0,0]-mean(s_hast[0,0])
mu = 0
sigma = max(vr)/5.0            
nois = normal(mu,sigma,size=len(n_tid))

plot(StarPos[0,0,:],StarPos[1,0,:])            
plot(planetPos[0,0,:],planetPos[1,0,:])
plot(planetPos[0,1,:],planetPos[1,1,:])
plot(planetPos[0,2,:],planetPos[1,2,:])
legend(['stjerne','planet1','planet2','planet3'],loc ="best")
xlabel('[AU]'); ylabel('[AU]')
#savefig('planet_sol_bane.png')
show()
plot(n_tid,(vr+nois))
plot(n_tid,vr)
xlabel('Tid [aar]')
ylabel('[AU]')
#savefig('uten_nois.png')
show()
#print (m_planeter[0]*1.98892*10**30)/float(1.89813*10**(27))
#print (m_planeter[1]*1.98892*10**30)/float(1.89813*10**(27))
#print (m_planeter[2]*1.98892*10**30)/float(1.89813*10**(27))

