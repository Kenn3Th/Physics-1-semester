"""
with open('temperature.dat', 'r') as infile:
    for i in range(3):
        infile.readline()
    for line in infile:
       lst = infile.readline().split()
       print float(lst[2])
"""

def f(f):
    return (f - 32)*(5./9)

f_deg = []

with open('temperature.dat', 'r') as infile:
    for i in range(3):
        infile.readline()
    for line in infile:
        lst = line.split()
        f_deg.append(float(lst[2]))

print f_deg

c_deg = []

for i in range(len(f_deg)):
    c_deg.append(f(f_deg[i])
                 
print c_deg

with open('f_c.dat', 'w') as outfile:
    outfile.write('hei\n') #\n betyr linje skift
    outfile.write('hei\n')
    for i in range(len(f_deg)):
        outfile.write(%.2f, %.2f) %(f_deg[i], c_deg[i])
  
"""
infile = open ('temperature.dat', 'r')
...
infile.close()
"""
