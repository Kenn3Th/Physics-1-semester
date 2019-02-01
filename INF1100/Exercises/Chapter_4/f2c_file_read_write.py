def f(f):
    return (f - 32)*(5./9)

f_deg = []

with open('temperature.dat', 'r') as infile:
    for i in range(3):
        infile.readline()
    for line in infile:
        lst = line.split()
        f_deg.append(float(lst[2]))

#print f_deg

c_deg = []

for i in range(len(f_deg)):
    C = f(f_deg[i])
    c_deg.append(C)

#print c_deg

with open('f_c.dat','w') as outfile:
    outfile.write('hei\n') #\n betyr linje skift
    outfile.write('\n')
    outfile.write('-------------------------- \n')
    outfile.write('farenheit  |  celcius\n')
    outfile.write('--------------------------\n')
    for i in range(len(f_deg)):
        outfile.write(('%6.2f, %10.2f \n') %(f_deg[i], c_deg[i]))
    
