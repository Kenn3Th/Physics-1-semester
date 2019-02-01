def yfunc(t, v0): #function to find the velocity of a particle
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt

position, velocity = yfunc(0.6, 3)

t_values = [0.05*i for i in range(10)]
for t in t_values:
    position, velocity = yfunc(t, v0=5)
    print 't=%-10g position=%-10g velocity=%-10g' %(t, position, velocity)
