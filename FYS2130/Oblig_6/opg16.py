import numpy as np, matplotlib.pyplot as plt
from numpy.fft import fft,ifft
from waveclass import*
from opg15 import Hvitstoy

#Konstanter
fsenter = 5000 #Hz
bredde = 3000 #Hz
N = 2000
K = [12,24]
omega_analyse = np.linspace(0,10000*2*np.pi,100)
#omega = np.linspace

fourier,signal,tid,frekvens = Hvitstoy(fsenter,bredde,N) #
omega = frekvens*2*np.pi
signal2 = np.square(signal)
#fourier transformasjon
fftsignal = fft(signal)
fftsignal2 = fft(signal2)
#wavelet
for j in xrange(len(K)):
    wave = []
    for i in xrange(len(omega_analyse)):
        solver = Wavelet(omega)
        psi = solver(omega_analyse[i],K[j])
        knall = ifft(fftsignal*psi)
        wave.append(knall)

    wave = np.array(np.abs(wave))
    times, freq = np.meshgrid(tid,omega_analyse)
    freq = freq/(2*np.pi)
    plt.subplot(2,1,j+1)
    amp = plt.contourf(times,freq,wave)
    cbar = plt.colorbar(amp)
    cbar.ax.set_ylabel('Amplitude')
    plt.xlabel('Tid [s]')
    plt.ylabel('Frekvens [Hz]')
    plt.title('K = %d' %(K[j]) )

plt.figure()
plt.subplot(2,1,1)
plt.plot(frekvens,fftsignal)
plt.title('Fast fourier av signalet')
plt.xlabel('Frekvens Hz')
plt.subplot(2,1,2)
plt.plot(frekvens,fftsignal2)
plt.title('Fast fourier av signal$^2$')
plt.xlabel('Frekvens Hz')
plt.show()
