
#formula C = (5.0/9.0)*(F - 32)
#formula F = (9.0/5.0)*C + 32

def F2C(f):
    return (5.0/9.0)*(f - 32)

Cdegrees = []

for f in range(50, 101, 10):
    f = F2C(f)
    Cdegrees.append(f)

def C2F(c):
    return (9.0/5.0)*c + 32

Fdegrees = []

for c in Cdegrees:
    c = C2F(c)
    Fdegrees.append(c)

print '      From Farenheit to celcius'

for C, F in zip(Cdegrees, Fdegrees):
    print 'Farenheit = %-10g Celcius = %-10g' %(F, C)

print '      From Celcius to farenheit'

Farenheit = []
for c in range(0, 40, 5):
    c = C2F(c)
    Farenheit.append(c)

Celcius = []
for f in Farenheit:
    f = F2C(f)
    Celcius.append(f)

for Q, B in zip(Celcius, Farenheit):
    print 'Celcius = %-10g Farenheit = %-10g' %(Q, B)
