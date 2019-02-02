import numpy as np, matplotlib.pyplot as plt

def Hvitstoy(fsenter,bredde,N):
    Fs = 4.0*(fsenter + bredde)
    fsigma = bredde/2.0 #Hz
    y = np.zeros(N) #fft av signalet
    T = float(N)/Fs
    t = np.linspace(0,T*(N-1)/N,N)
    f = np.linspace(0,Fs*(N-1)/N,N)
    nsenter = np.floor(N*fsenter/(Fs*(N-1)/N))
    nsigma = np.floor(N*fsigma/(Fs*(N-1)/N))
    gauss = np.exp(-(f-fsenter)*(f-fsenter)/(fsigma*fsigma))
    ampl = np.random.rand(N) 
    ampl = ampl*gauss 
    faser = np.random.rand(N)
    faser = faser*2*np.pi
    y = ampl*(np.cos(faser) + 1j*np.sin(faser))
    Nhalv = np.int(np.round(N/2))
    for k in xrange(1,Nhalv):
        y[N-k] = np.conj(y[k])
    y[Nhalv+1] = np.real(y[Nhalv+1])
    y[0] = 0.0
    q = np.real(np.fft.ifft(y)*200) #signalet
    return y,q,t,f

def akorrelasjon(g,M,N):
    C = np.zeros(N-M)
    for j in xrange((N-M)-1):
        teller = 0
        nevner = 0
        for i in xrange(M):
            teller += g[i]*g[i+j]
            nevner += g[i]*g[i]
        C[j] = teller/nevner
    return C
    

if __name__ == "__main__":
    fsenter = 5000 #Hz
    bredde = 3000 #Hz
    N = 2000
    M = np.int(np.round(N/2.))
    fftsignal,signal,tid,frekvens = Hvitstoy(fsenter,bredde,N)

    C = akorrelasjon(signal,M,N)
    #plot
    plt.plot(C)
    plt.plot(7.15,np.e**-1,'o')
    plt.plot((0,30),(np.e**-1,np.e**-1),color = 'black')
    plt.plot((7.182,7.182),(-1,1), color = 'black')
    plt.legend(['Autokorrelasjon','$t_c = 7.182$'])
    plt.title('autokorrelasjon')
    plt.axis([0,30,-1,1])
    plt.xlabel('Tid[s]')
    plt.ylabel('Korrelasjons konstant C')
    plt.figure()
    plt.plot(frekvens,fftsignal)
    plt.title('fft av stoyet')
    plt.xlabel('Frekvens Hz')
    plt.ylabel('Utslag')
    plt.figure()
    plt.plot(tid,signal)
    plt.title('signal')
    plt.xlabel('tid s')
    plt.ylabel('Utslag')
    plt.show()
    
    
