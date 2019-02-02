import numpy as np, matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from waveclass import*
#konstanter
fs = 10**4
f1 = 10**3
f2 = 1.6*10**3
c1 = 1.0
c2 = 1.7
dt = 1.0/fs
N = 8192.0
tid = np.arange(N)*dt
#signal
sig = c1*np.sin(2*np.pi*f1*tid) + c2*np.sin(2*np.pi*f2*tid)
#FFT
FFTsig = fft(sig)/N
freq_FFT = np.linspace(0,fs,N)/10.0**3
#wavelet
n = 100
K = [24,200]
omegaa = np.linspace(800,2000,n)*(2*np.pi)
omega = np.linspace(0,fs,N)*(2*np.pi)

for j in xrange(len(K)):
    wave = []
    for i in xrange(len(omegaa)):
        solver = Wavelet(omega)
        psi = solver(omegaa[i],K[j])
        knall = ifft(FFTsig*psi)
        wave.append(knall)

    wave = np.array(np.abs(wave))
    times, freq = np.meshgrid(tid,omegaa)
    freq = freq/(2*np.pi)
    plt.subplot(2,1,j+1)
    amp = plt.contourf(times,freq,wave)
    cbar = plt.colorbar(amp)
    cbar.ax.set_ylabel('Amplitude')
    plt.xlabel('Tid [s]')
    plt.ylabel('Frekvens [Hz]')
    plt.title('K = %d' %(K[j]) )


#plot
plt.figure()
plt.plot(freq_FFT,np.abs(FFTsig))
plt.xlabel('Frekvens [kHz]')
plt.ylabel('Fourier koeffisient |X(f)|')
plt.title('Frekvensspekter')
plt.axis([0,5,-0.1,0.8])
plt.show()

