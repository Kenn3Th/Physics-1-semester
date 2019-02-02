import numpy as np, matplotlib.pyplot as plt

a = 3.5
b = 5.0
x = np.linspace(0.0,2.0,21)
y = a+float(b)*x + np.random.randn(1,len(x))
y = y[0]
p = np.polyfit(x,y,1)

m = p[0]
c = p[1]

yline = np.polyval(p,x)

if __name__ == '__main__':
    plt.plot(x,y,'*')
    plt.plot(x,yline,'-')
    plt.show()

    print m
    print c
