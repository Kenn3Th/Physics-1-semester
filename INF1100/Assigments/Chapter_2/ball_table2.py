
#formula y(t) = v0*t - 0.5*g*t**2
v0 = 5.0    #velocity
g = 9.81    #gravity
n = 5       

t_stop = 2*v0/g
dt = t_stop/n

t_list = []
y_list=[]

#for loop

for i in range(0,n+1):
    t = i*dt
    y = v0*t - 0.5*g*t**2
    t_list.append(t)
    y_list.append(y)

for y, t in zip(y_list, t_list):
    print '%5.2f %5.2f' % (t, y)


"""
Terminal>python ball_table2.py 
 0.00  0.00
 0.20  0.82
 0.41  1.22
 0.61  1.22
 0.82  0.82
 1.02  0.00
 """
