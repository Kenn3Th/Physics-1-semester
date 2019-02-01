from pylab import*
#variable
n = linspace(-5,5,1500)
X,Y = meshgrid(n,n,indexing='ij')
#variable til stagnasjonspunktene
i = linspace(-5,5,40)
x = zeros(len(i))
#Funksjon
C = Y - log(abs(X))
#plott
contour(X,Y,C)
plot(x,i,'o') #stagnasjonspunktene
title('Stroemlinje plott')
xlabel('x-aksen')
ylabel('y-aksen')
savefig('2b.png')
show()
