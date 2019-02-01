import sys

def c(f):
    return (f - 32)*(5.0/9)

try:
    degree = sys.argv[1]   #Fetches variables from cmd-window
    degree = float(degree)
except:
    print "No command line argument"
    #sys.exit(1) #avslutter programmet

    degree = raw_input("f = ")
    try:
        degree = float(degree)
    except:
        degree = float(raw_input('f = '))
        
print '%.2f, %.2f' % (degree, c(degree))
