from pylab import*

h = [0, 2, 4, 6, 8, 10]
x = [230, 34, 12.8, 6.2, 3.6, 2.6]

p = polyfit(x,h,2)
b = polyval(p,x)

def B(h):
    mu_0 =4*pi*10**(-7)
    Js = 1 ; t = 1; a = 1.7
    B = (mu_0/2.0*Js)*((h+t)/sqrt((h+t)**2+a**2) - h/sqrt(h**2 + a**2))
    return B

B_h = zeros(len(h))
for i in xrange(len(h)):
    B_h[i] = B(i)

subplot(2,1,1)
title('Measurment')
plot(x,h,'rx')
plot(x,b)
legend([u'Maaleresultater','Interpolasjon'], prop={'size': 15})
ylabel('h [cm]')
subplot(2,1,2)
plot(B_h,h,'rx')
plot(B_h,b)
legend([u'Maaleresultater','Interpolasjon'], prop={'size': 15})
title('Analytic')
ylabel('h [cm]')
xlabel('B_h [mT]')
savefig('2.png')
show()
