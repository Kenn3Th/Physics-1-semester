from pylab import*

Tid = 20 #Dager
x = zeros((Tid,3,1)) #Xn-vektor
P = array((
    [0.4,0.3,0.2],
    [0.5,0.5,0.2],
    [0.1,0.2,0.6]))
#Likevekts-vektor
q = array((
    [16/53.0],
    [22/53.0],
    [15/53.0]))
#Initialbetingelser
x[0] = array((
    [2*10**4],
    [2.5*10**4],
    [8000]))
      
for i in range(Tid-1):
    x[i+1] = dot(P,x[i]) #matrise multiplikasjon

print 'Dag 4'
print x[3]
print 'Dag 10'
print x[9]
print 'Dag 20'
print x[19]
print'Analytisk svar. likevekts-vektor*befolkning'
print q * 53000
