import sys

if len(sys.argv) < 2:               #if test
    print 'provide a temperature!'  #prints the argument if true 
    exit()                          #closes the program
    
F = sys.argv[1]

F = float(F)
C = (F-32)*5.0/9

print '%g degrees F is %g degrees C' %(F, C)
