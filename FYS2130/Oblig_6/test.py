import numpy as np
import matplotlib.pyplot as plt

def HvitStoyGauss(N,fsenter,fullbredde):
    Fs = 2.*(fsenter + fullbredde) + 1
    fsigma = fullbredde/2.0 # sigma
    y = np.zeros(N) #blir fft av stoysignal
    T = N/Fs #antall malinger
    t = np.linspace(0,T*(N-1)/N,N)
    f = np.linspace(0,Fs*(N-1)/N, N)
    nsenter = np.floor(N*fsenter/(Fs*(N-1)/N))
    nsigma = np.floor(N*fsigma/(Fs*(N-1)/N))
    gauss = np.exp(-(f-fsenter)*(f-fsenter)/(fsigma*fsigma)) #gaussisk fordelt frekvenser
    ampl = np.random.rand(N) #stoy
    ampl = ampl*gauss #gaussisk fordelt frekvenser med stoy
    faser = np.random.rand(N)
    faser = faser*2*np.pi
    y = ampl*(np.cos(faser) + 1j*np.sin(faser))
    Nhalv = np.round(N/2)
    for k in range(1,Nhalv):
        y[N-k] = np.conj(y[k])
    y[Nhalv+1] = np.real(y[Nhalv+1])
    y[0] = 0.0
    q = np.real(np.fft.ifft(y)*200)
    return y, q,t,f
def plotstoy():
    y, q, t, f = HvitStoyGauss(20000,5e+3,3e+3)
    plt.plot(f,y)
    plt.title('fft av et stoysignal')
    plt.show()
    plt.plot(t,q)
    plt.title('stoysignalet med senterfrekvens '+str(5e+3)+ ' og stoybredde ' +str(round(3e+3/2)))
    plt.show()
plotstoy()
