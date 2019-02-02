from ast2000solarsystemviewer_v2 import AST2000SolarSystemViewer
import numpy as np, matplotlib.pyplot as plt, random as random

seed = 59750
system = AST2000SolarSystemViewer(seed)

#Helesystemet
nr_planeter = system.number_of_planets
Radius = system.radius #radius til alle planetene [km]
Mass = system.mass     #Massen til hele systemet [Solmasse]
pl_x0 = system.x0      #planetenes initial posisjon i x-retning [AU]
pl_y0 = system.y0      #planetenes initial posisjon i y-retning [AU]
pl_vx0 = system.vx0    #planetenes initial hastighet i x-retning [AU]
pl_vy0 = system.vy0    #planetenes initial hastighet i y-retning [AU]
rho = system.rho0      #Atmospheric density at surface [kg/m^3]
G = 6.67428*10**-11    #Newtons gravitasjons konstant [m^3/(kg*s^2)]

#Sola
solMass = system.star_mass    #[Solmasse]
sol_rad = system.star_radius  #Radius av sola [km]
sol_temp = system.temperature #Overflate temperatur av Sola [K]

#hjemplanet
vekt = Mass[0]  #Massen [solmasse]
rad = Radius[0] #Radius til hjemplanet [km]
atm = rho[0]    #Atmosfaeren til hjemplaneten [kg/m**3]
pm = vekt*1.98892*10**30       #sunmass to kg (hjemplanet)
pr = rad*1000                  #km to m (hjemplanet)
x0 = pl_x0[0]
y0 = pl_y0[0]
vx0 = pl_vx0[0]
vy0 = pl_vy0[0]
v_esc = np.sqrt((2*G*pm)/pr) #[m/s]

