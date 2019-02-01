# y = v0*t - 0.5*g*t**2 formula

v0 = 5.0
g = 9.81
n = 5

t_stop = 2*v0/g
dt = t_stop/n

#for loop
print 'for loop'
for i in range(0,n+1):
    t = i*dt
    y = v0*t - 0.5*g*t**2
    print "%5.2f , %5.2f" % (t, y)

#while loop
print 'while loop'
t=0
while t <= t_stop:
    y = v0*t - 0.5*g*t**2
    print "%5.2f %5.2f" %(t, y)
    t += dt

"""
Terminal>python ball_table1.py 
for loop
 0.00 ,  0.00
 0.20 ,  0.82
 0.41 ,  1.22
 0.61 ,  1.22
 0.82 ,  0.82
 1.02 ,  0.00
while loop
 0.00  0.00
 0.20  0.82
 0.41  1.22
 0.61  1.22
 0.82  0.82
 1.02  0.00
 """
