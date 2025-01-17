from numpy import * #importing everything from numpy

def h(x): #formula
    return (1./sqrt(2*pi))*exp(-0.5*x**2)

x = linspace(-4, 4, 41) #creating an array with 41 uniformly spaced x coordinates in [-4,4]
y = h(x) #creating an array with the formula h(x) with every value of x in x-array
    
print '----------------------------------------------------------------------------'
print '                    x values in a', type(x)
print '----------------------------------------------------------------------------'
print x 
print '----------------------------------------------------------------------------'
print '                   h(x) values, in a', type(y)
print '--------------------------------------------------------------------'
print y
print '--------------------------------------------------------------------'

"""
Terminal> python fill_arrays_vectorized.py 
----------------------------------------------------------------------------
                    x values in a <type 'numpy.ndarray'>
----------------------------------------------------------------------------
[-4.  -3.8 -3.6 -3.4 -3.2 -3.  -2.8 -2.6 -2.4 -2.2 -2.  -1.8 -1.6 -1.4 -1.2
 -1.  -0.8 -0.6 -0.4 -0.2  0.   0.2  0.4  0.6  0.8  1.   1.2  1.4  1.6  1.8
  2.   2.2  2.4  2.6  2.8  3.   3.2  3.4  3.6  3.8  4. ]
----------------------------------------------------------------------------
                   h(x) values, in a <type 'numpy.ndarray'>
--------------------------------------------------------------------
[  1.33830226e-04   2.91946926e-04   6.11901930e-04   1.23221917e-03
   2.38408820e-03   4.43184841e-03   7.91545158e-03   1.35829692e-02
   2.23945303e-02   3.54745928e-02   5.39909665e-02   7.89501583e-02
   1.10920835e-01   1.49727466e-01   1.94186055e-01   2.41970725e-01
   2.89691553e-01   3.33224603e-01   3.68270140e-01   3.91042694e-01
   3.98942280e-01   3.91042694e-01   3.68270140e-01   3.33224603e-01
   2.89691553e-01   2.41970725e-01   1.94186055e-01   1.49727466e-01
   1.10920835e-01   7.89501583e-02   5.39909665e-02   3.54745928e-02
   2.23945303e-02   1.35829692e-02   7.91545158e-03   4.43184841e-03
   2.38408820e-03   1.23221917e-03   6.11901930e-04   2.91946926e-04
   1.33830226e-04]
--------------------------------------------------------------------
"""
