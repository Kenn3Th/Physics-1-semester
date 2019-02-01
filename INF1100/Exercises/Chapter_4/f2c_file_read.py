infile = open('temperature.dat','r')
    
"""    
line = infile.readline() #reads first line in file
line = infile.readline() #reads next line and so on
line = infile.readline()
line = infile.readline()
"""


for i in range(4):      # Easyer to use a for loop.
    infile.readline()

line = infile.readline()
line = line.split()
print line

#for line in infile:
#    print line

infile.close() # this is for closing the file at the end.
