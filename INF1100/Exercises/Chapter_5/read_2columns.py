import matplotlib.pyplot as plt

infile = open('xy.dat','r')

x = []
y = []

for line in infile:
    word = line.split
    x.append(float(words[0])
    y.append(float(word[1])

infile.close()

mean_y = sum(y)/len(y)
print "Mean = %g, min = %g, max = %g" %(mean_y, min(y), max(y)

plt.plot(x, y)
plt.show()
