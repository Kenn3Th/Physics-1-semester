from math import pi
a = 0.11 # radius of a football
m = 0.43 # mass of football
g = 9.81 # acceleration of gravity

Q = 1.2      # denisty of air
Vh = 120/3.6 # velocity of a hard kick. Convertes from km/h to m/s
Vs = 30/3.6  # velocity of a soft kick. Convertes from km/h to m/s
A = pi*a**2  # normal to the velocity direction
Cd = 0.4     # drag coefficiant

# Fd = (1/2)*Cd*Q*A*V**2 is the formula to the drag force due to air resistance
Fds = (1.0/2)*Cd*Q*A*Vs**2 # soft kick
Fdh = (1.0/2)*Cd*Q*A*Vh**2 # hard kick
Fg = m*g                   # gravity formula

R1 = Fds/Fg # ratio between force of gravity and drag force from a soft kick
R2 = Fdh/Fg # ratio between force of gravity and drag force from a hard kick

print '''The force of gravity on a football on planet Tellus is %.2g N.
With a soft kick it has a drag force on ca %.g N, and
with a hard kick the drag force is ca %.3g
Ratio between drag force and the force of gravity
from a soft kick is %.2g and from a hard kick is %.2g''' % (Fg, Fds, Fdh, R1, R2)

"""
Terminal>python kick.py 
The force of gravity on a football on planet Tellus is 4.2 N.
With a soft kick it has a drag force on ca 0.6 N, and
with a hard kick the drag force is ca 10.1
Ratio between drag force and the force of gravity
from a soft kick is 0.15 and from a hard kick is 2.4
"""
