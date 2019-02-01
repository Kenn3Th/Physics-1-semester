import numpy as np
import matplotlib.pyplot as plt

def c(F): #Function for calculating aproximate celcius degrees
    return (F-30)/2.0

def C(F): #Function for calculating exact celcius degrees
    return (F-32.0)*(5/9.0)

F = np.linspace(-20, 120, 29)
y = np.zeros(len(F))
x = np.zeros(len(F))

for i in xrange(len(F)): #Calculating celcius-degrees
    y[i] = c(F[i])
    x[i] = C(F[i])

plt.plot(x, F)
plt.plot(y, F)
plt.axis([-30, 100, -20, 130]) #Celcius-min, Celcius-max, Farenheit-min, Farenheit-max
plt.legend(['C = (F-32)*5/9.0)','c = (F-30)/2.0'])
plt.title('Farenheit to Celcius')
plt.xlabel('Celcius')
plt.ylabel('Farenheit')
plt.show()

"""
Terminal> python f2c_shortcut_plot.py
"""
