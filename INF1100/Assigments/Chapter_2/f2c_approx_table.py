#formula C = (F - 32)/(9.0/5.0). Converting farenheit to celcius
#formula F = (5.0/9.0)*C + 32. Converting celcius to farenheit
#formula c^ = (F - 30)/2. approximate converting from farenheit to celcius

Cdegrees = []  #Celcius degrees
Fdegrees = []  #Farenheit degrees
ACdegrees = [] #Approximate convertion from farenheit to celcius

F = 0.0        #Start Farenheit degree
dF = 10.0

while F <= 100:
    C = (F - 32)/(9.0/5.0) #Formula
    Q = (F - 30)/2
    Cdegrees.append(C), Fdegrees.append(F), ACdegrees.append(Q)
    F = F + dF

print '________________Farenheit to celcius convertion___________________'
print''
for C,F,A in zip(Cdegrees, Fdegrees, ACdegrees):
    print 'Farenheit = %-10g Accurate = %-10.2f Approximate = %-10g' %(F, C, A)

print'____________________________________________________________________'

"""
Terminal>python f2c_approx_table.py 
________________Farenheit to celcius convertion___________________

Farenheit = 0          Accurate = -17.78     Approximate = -15       
Farenheit = 10         Accurate = -12.22     Approximate = -10       
Farenheit = 20         Accurate = -6.67      Approximate = -5        
Farenheit = 30         Accurate = -1.11      Approximate = 0         
Farenheit = 40         Accurate = 4.44       Approximate = 5         
Farenheit = 50         Accurate = 10.00      Approximate = 10        
Farenheit = 60         Accurate = 15.56      Approximate = 15        
Farenheit = 70         Accurate = 21.11      Approximate = 20        
Farenheit = 80         Accurate = 26.67      Approximate = 25        
Farenheit = 90         Accurate = 32.22      Approximate = 30        
Farenheit = 100        Accurate = 37.78      Approximate = 35        
____________________________________________________________________
"""
