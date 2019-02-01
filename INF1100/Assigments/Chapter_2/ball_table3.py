#formula y(t) = v0*t - 0.5*g*t**2
v0 = 5.0    #velocity
g = 9.81    #gravity
n = 5       

t_stop = 2*v0/g
dt = t_stop/n

t_list = []
y_list = []

for i in range(0,n+1):
    t = i*dt
    y = v0*t - 0.5*g*t**2
    t_list.append(t)
    y_list.append(y)
    
# a)    
ty1 = [t_list, y_list]

print 'a)'
for t, y in zip(ty1[0], ty1[1]):
    print '%5.2f %5.2f' %(t, y)

# b)

ty2 = []
for t ,y in zip(t_list, y_list):
    ty2.append([t, y])
   
print 'b)'
for row in ty2:
    print '%5.2f %5.2f' % (row[0], row[1])

"""
Terminal>python ball_table3.py 
a)
 0.00  0.00
 0.20  0.82
 0.41  1.22
 0.61  1.22
 0.82  0.82
 1.02  0.00
b)
 0.00  0.00
 0.20  0.82
 0.41  1.22
 0.61  1.22
 0.82  0.82
 1.02  0.00
"""
