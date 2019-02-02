# -*- coding: utf-8 -*-

from pylab import*

h = np.array([0, 20, 40, 60, 80, 100])/1e3 + 1e-10
x = np.array([230, 34, 12.8, 6.2, 3.6, 2.6])/1e3

p = polyfit(x,h,2)
b = polyval(p,x)

def B(h):
    mu_0 =4.*pi*10**(-7)
    Js = 1 ; t = 0.01; a = .0017
    B = (mu_0*Js/2.0)*((h+t)/sqrt((h+t)**2+a**2) - h/sqrt(h**2 + a**2))
    return B

B_h = zeros(len(h))
for i in xrange(len(h)):
    B_h[i] = B(i)

subplot(2,1,1)
title(u'Målinger', size=20)
plot(h,x,'rx')
plot(h,x,'b-')
ylabel('$B_h$ [T]', size=15)
subplot(2,1,2)
plot(h, B_h,'rx')
plot(h, B_h,'b-')

title('Analytisk', size=20)
xlabel('$h$ [m]', size=15)
ylabel('$B_h$ [T]', size=15)
savefig('2.png')
show()
