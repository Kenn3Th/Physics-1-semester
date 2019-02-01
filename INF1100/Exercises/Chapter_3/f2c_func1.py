Cdegree = []

for C in range(-10, 42, 5):
    Cdegree.append(C)
    
def F(C):
    return (9.0/5.0)*C + 32

Fdegree = [F(C) for C in Cdegree]
for c, f in zip(Fdegree, Cdegree):
    print 'Farenheit = %5.2f Celcius = %5.2f' %(c, f)
