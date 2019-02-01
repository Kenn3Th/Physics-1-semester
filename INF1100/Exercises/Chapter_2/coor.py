a = 0
b = 10
n = 20

h = float(b-a)/n

#a)
coor = []
for i in range(n+1):
    xi = a+i*h
    coor.append(xi)
print'a)'
print len(coor)
print coor

#b)
coor = [a+i*h for i in range(n+1)]

print 'b)'
print coor

"""
Terminal>python coor.py 
a)
21
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
b)
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
"""
