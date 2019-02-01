from math import pi, log

def egg(M,To=20,Ty=70):    
    c = 3.7
    K = 5.4e-3    # thermal conductivity
    rho = 1.038   # density
    Tw = 100      # Water temperatur
    time = (M**(2.0/3.0)*c*rho**(1.0/3.0))/(K*pi**2*(4*pi/3)**(2.0/3.0)) \
      *log(0.76*(To-Tw)/(Ty-Tw))
    return time

TT = [60, 70]
M = [47, 67]
T0 = [4, 25]

for m in M:
    for ty in TT:
        for to in T0:
            time = egg (m, To=to, Ty=ty)
            print '''With mass %g and init temperatur %g,
the core temperature %g is reasched after %g seconds''' %(m, to, ty, time)


"""
Terminal>python egg_func.py 
With mass 47 and init temperatur 4,
the core temperature 60 is reasched after 211.744 seconds
With mass 47 and init temperatur 25,
the core temperature 60 is reasched after 124.775 seconds
With mass 47 and init temperatur 4,
the core temperature 70 is reasched after 313.095 seconds
With mass 47 and init temperatur 25,
the core temperature 70 is reasched after 226.126 seconds
With mass 67 and init temperatur 4,
the core temperature 60 is reasched after 268.202 seconds
With mass 67 and init temperatur 25,
the core temperature 60 is reasched after 158.044 seconds
With mass 67 and init temperatur 4,
the core temperature 70 is reasched after 396.576 seconds
With mass 67 and init temperatur 25,
the core temperature 70 is reasched after 286.418 seconds
"""
