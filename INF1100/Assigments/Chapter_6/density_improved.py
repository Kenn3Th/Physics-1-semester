#a)
def read_densities(filename):
    infile = open(filename,'r')
    densities = {}

    for line in infile:
        line.strip()
        words = line.split()
        density = float(words[-1])
        substance = ' '.join(words[:-1])
        densities[substance] = density
        
    infile.close()
    return densities
#b)
def substance_densities(filename):
    infile = open(filename,'r')
    densities = {}

    for line in infile:
        substance = line[0:10].strip()
        density = float(line[10:-1].strip())
        densities[substance] = density
        
    infile.close
    return densities
#c)
def test_sub_den():
    comp1 = read_densities('densities.dat')
    comp2 = substance_densities('densities.dat')
    success = (comp1 == comp2)
    msg = 'Something went horribly wrong!'
    assert success, msg

test_sub_den()

"""
Test funksjonen min tester om funksjon 1 er lik funksjon 2.

Jeg hentet filen jeg brukte til aa lage programmet her:
Terminal> curl https://raw.githubust/scipro-primer/master/src/dictstring/densities.dat < densities.dat

Jeg
"""
