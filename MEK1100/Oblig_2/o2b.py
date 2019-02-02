from oblig2 import*
#Definerer en variabel til konturplott
Z = sqrt(u**2+v**2)
v1 = linspace(500,4500,7)
v2 = linspace(0,500,7)
#kontur plott
subplot(2,1,1) #Luft
c=contourf(x,y,Z,v1)
colorbar(c)
plot(xit,yit,'*',color='black')
title('Luft')
ylabel('Y-akse')
subplot(2,1,2) #Vann
cs=contourf(x,y,Z,v2)
colorbar(cs)
plot(xit,yit,'*',color='black')
title('Vann')
xlabel('X-akse')
ylabel('Y-akse')
savefig('2b.png')
show()
