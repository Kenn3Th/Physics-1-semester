from Solmal import*

#Escape velocity for my home planet
pm = vekt*1.98892*10**30       #sunmass to kg (hjemplanet)
pr = rad*1000                  #km to m (hjemplanet)
v_esc = np.sqrt((2*G*pm)/pr) #[m/s]

print 'The escape velocity for my planet is'
print '%.2f m/s' %v_esc

random.seed(313)
N = 10**5                   #Number of paricles 
k = 1.38064852*10**(-23)    #Boltzmann konstant [J/K]
T = 10**4                   #Temperatur [K]
h2 = 3.35*10**-27           #Hydrogen molecule mass [kg]
L = 10**-6                  #Size of box
m_sat = 1000                #Satelite mass [kg]
mu = 0                      #mean
sigma = np.sqrt((k*T)/h2)   #deviation
ts = 1000                #Time steps
dt = 10**-9              #DeltaTime
at = float(dt)/float(ts) #gjevnt fordelt steg

part_pos = np.zeros((N, 3, ts)) #Position of particle
part_vel = np.zeros((N,3))      #Velocity of particle

for i in range(N):
    for j in range(3):
        part_pos[i,j,0] = random.uniform(0,L)  #Places the particle at random
        part_vel[i,j] = random.gauss(mu,sigma) #Gives the particle a random velocity
        
#Kinetic energy
kinetic = lambda m,v : 0.5*m*v**2 #Formula Kinetic energy
kix = np.zeros(len(part_vel))     #x-direction
kiy = np.zeros(len(part_vel))     #y-direction
kiz = np.zeros(len(part_vel))     #z-direction
for i in range(len(part_vel)):
      kix[i] = part_vel[i][0]
      kiy[i] = part_vel[i][1]
      kiz[i] = part_vel[i][2]
#mean kinetic energy
mean_kin = np.mean(kinetic(h2,np.sqrt(kix**2+kiy**2+kiz**2)))
#mean velocity
mean_vel = np.mean(np.sqrt(part_vel[:,0]**2+part_vel[:,1]**2+part_vel[:,2]**2))

print 'Kinetic Energy'
print 'Exact (3/2)kT'
print (3./2.)*(k*T)
print 'My calculation of mean kinetic energy'
print mean_kin
print 'Mean velocity'
print 'Analytic solution for mean velocity (sqrt((8kT)/(pi m))'
print np.sqrt((8*k*T)/(np.pi*h2))
print 'My calculation of mean velocity'
print mean_vel

#box
L = 10**-6           #Size of box     
nr_ut = 0            #Number of particles that escapes 
mom_loss = 0         #Momentum out the hole
y_mom = 0            #Momentum on wall (y-aksen+)
hit = 0              #How many particles hit the wall
hole_min = L/4.0     #Where the hole starts
hole_max = (3*L)/4.0 #Where the hole ends

for i in xrange(ts-1):
    part_pos[:,:,i+1] = part_pos[:,:,i] + part_vel[:,:]*at
    for j in xrange(N):
        if part_pos[j, 0, i+1] >= L: #x+
            if part_vel[j, 0] > 0:
                part_vel[j,0] = part_vel[j,0]*-1.0
                if ((hole_min < part_pos[j,1,i+1] < hole_max) and #Hole
                    (hole_min < part_pos[j,2,i+1] < hole_max)):
                    nr_ut += 1
                    mom_loss += 2*h2*np.abs(part_vel[j,0])#Momentum formel(2px where px = m*vx)
                else:
                    continue
        elif part_pos[j,0, i+1] <= 0: #x-
            if part_vel[j, 0] < 0:
                part_vel[j,0] = part_vel[j,0]*-1.0
            else:
                continue
        elif part_pos[j,1,i+1] >= L: #y+
            if part_vel[j,1] > 0:
                part_vel[j,1] = part_vel[j,1]*-1.0
                hit += 1                            #Hit the wall
                y_mom += 2*h2*np.abs(part_vel[j,1]) #Momentum formel (2py where py = m*vy)
            else:
                continue
        elif part_pos[j,1,i+1] <= 0: #y-
            if part_vel[j,1] < 0:
                part_vel[j,1] = part_vel[j,1]*-1.0
            else:
                continue
        elif part_pos[j,2,i+1] <= 0: #z-
            if part_vel[j,2] < 0:
                part_vel[j,2] = part_vel[j,2]*-1.0
            else:
                continue
        elif part_pos[j,2,i+1] >= L: #z+
            if part_vel[j,2] > 0:
                part_vel[j,2] = part_vel[j,2]*-1.0
            else:
                continue

Trykk = lambda F,A : float(F)/A #Trykkformel
A = L**2                        #Areal of box
Ap = (float(N)/L**3)*(k*T)      #P = nkT
             
print 'Analytic pressure'
print Ap
print 'My numerical calculation of pressure'
print Trykk(y_mom/dt,A)

F = float(mom_loss)/dt #Force due to momentum loss of box F = dp/dt [kgm/s^2]
dv = float(F)/m_sat    #The acceleration dv= F/m [(kgm/s^2)/kg -> m/s^2] = a

a_esc = v_esc/1200     #acceleration needed to achieve escape velocity in 20 min [m/s^2]
num_box = a_esc/dv     #number of boxes needed to achieve escape velocity in 20 min
tot_h2_esc = (1200.0/dt*nr_ut)*num_box #Total amount H2 molecules that escapes in 20 min
init_fuel = tot_h2_esc*h2*num_box      #Fuel needed to reach the escape velocity in 20 min

print 'The force the momentum creates is'
print F
print 'The change in velocity the box gains of the momentum loss is'
print dv
print 'The acceleration needed to achive escape velocity whitin 20 minutes'
print a_esc
print 'The number of boxes needed to achieve the acceleration'
print num_box
print 'Number of particles that escapes in 10^-9 seconds'
print nr_ut*num_box
print 'Number of particles that escapes in 1200 (20min) seconds'
print tot_h2_esc
print 'Amount of H2 molecules (Fuel) thats been used in those 20 min'
print init_fuel
