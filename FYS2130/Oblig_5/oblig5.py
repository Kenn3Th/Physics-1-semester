import numpy as np, matplotlib.pyplot as plt

#Genererer posisjons array
delta_x = 0.1
x = np.linspace(-20,20,401)
n = len(x)

#Genrerer posisjonen ved t=0
sigma = 2.0
u = np.exp(-(x/(2*sigma))*(x/(2*sigma))) #gaussisk form
#plt.plot(x,u)

#Genererer div parametre og tidsderiverte av utslaget vd t=0
v = 0.5 ; delta_t = 0.1
faktor = (delta_t*v/delta_x)**2
dudt = (v/(2*sigma**2)*x*u)
#dudt = -dudt
dudt = dudt*0.5
#dudt = 2*dudt
#Angir effektive initialbetingelser
u_jminus1 = u - delta_t*dudt
u_j = u
u_jpluss1 = np.zeros(n)
N = 1000

for t in xrange(N):
    u_jpluss1[1:n-1] = (2*(1-faktor))*u_j[1:n-1] - u_jminus1[1:n-1] + faktor*(u_j[2:n]+u_j[0:n-2])
    #handtering av randproblemet, setter uj-1 = uj+1 = 0
    u_jpluss1[0] = (2*(1-faktor))*u_j[0]-u_jminus1[0] + faktor*u_j[1]
    u_jpluss1[n-1] = (2*(1-faktor))*u_j[n-1]-u_jminus1[n-1] + faktor*u_j[n-2]

    if t % 250 == 0:
        plt.plot(x,u_j)
    u_jminus1 = u_j.copy()
    u_j = u_jpluss1.copy()

plt.legend(['$t=0$','$t=t+\Delta t$','$t=t+2\Delta t$','$t=t+3\Delta t$'],loc = 'best')
plt.title('0.5*du/dt')
plt.ylabel('Utslag')
plt.savefig('05dudt.png')
plt.show()


    

