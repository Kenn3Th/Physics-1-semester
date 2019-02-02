import numpy as np, matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy import signal

def FFT(p,n): #p = perioder, n = samplinger
    t = np.linspace(0,p,n)
    signal = np.sin((2*np.pi)*t)
    FFT = fft(signal)/float(n)
    fs = 1.0/(t[1]-t[0])
    freq = np.linspace(0,fs,n)
    return signal,FFT,freq,t
def square(p,n): #p = perioder, n = samplinger
    t = np.linspace(0,p,n)
    square = signal.square((2*np.pi)*t)
    fs = 1.0/(t[1]-t[0])
    freq = np.linspace(0,fs,n)
    FFT = fft(square)/n
    return square,FFT,freq,t
#konstanter
N = 512.0
n = 2**(14)
#
signal_a,FFT_a,freq_a,t_a = FFT(13,N)
signal_b,FFT_b,freq_b,t_b = FFT(13.2,N)
square,FFT_square,freq_square,t_s = square(16,n)


#plot
#signal a
plt.subplot(1,2,1)
plt.plot(t_a,signal_a)
plt.title('Tidsbildet')
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [rad]')
plt.subplot(1,2,2)
plt.title('Frekvensspekteret')
plt.plot(freq_a,np.abs(FFT_a))
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Fourierkonst. |X(f)|')
plt.axis([0,20,0,0.6])
#plt.savefig('13perioder.png')
#signal b
plt.figure()
plt.subplot(1,2,1)
plt.plot(t_b,signal_b)
plt.title('Tidsbildet')
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [rad]')
plt.subplot(1,2,2)
plt.title('Frekvensspekteret')
plt.plot(freq_b,np.abs(FFT_b))
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Fourierkonst. |X(f)|')
plt.axis([0,20,0,0.6])
#Firkantbolge
plt.figure()
plt.subplot(1,2,1)
plt.plot(t_s,square)
plt.title('Tidsbildet')
plt.xlabel('Tid [s]')
plt.ylabel('Utslag [rad]')
plt.axis([0,16.5,-1.2,1.2])
plt.subplot(1,2,2)
plt.title('Frekvensspekteret')
plt.plot(freq_square,np.abs(FFT_square))
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Fourierkonst. |X(f)|')
plt.axis([0,500,0,0.1])

#Analytisk amplitude
Amplitude = np.zeros(n)
for i in xrange(n):
    Amplitude[i] = 2.0/(np.pi*(2*i-1))
t = np.linspace(0,16,n)
plt.figure()
plt.plot(t,Amplitude)
plt.ylabel('Amplitude')
plt.xlabel('Tid')
plt.show()


