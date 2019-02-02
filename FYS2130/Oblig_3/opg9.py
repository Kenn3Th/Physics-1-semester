import numpy as np, matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft

"""
Enkelt eksempelprogram for aa vise hvordan fouriertransformasjon
kan gjennomfores i praksis i Matlab. Eksemplet er en modifikasjon
av et eksempelprogram paa hjelpesidene i Matlab.
"""
Fs = 1000;
delta_t = 1.0/Fs
N = 1024.0
t = np.linspace(0,Fs,N) # Tidsvektor
"""
Samplingsfrekvens
Tid mellom hver sampling
Antall samplinger
Lager her et kunstig signal som en sum av et 50 Hz sinussignal
og en 120 Hz cosinus, pluss legger til et random signal:
"""
x = 0.7*np.sin(2*np.pi*50*t) + np.cos(2*np.pi*120*t)
x = x + 1.2*np.random.randn(len(t))
plt.plot(Fs*t,x)         # Plotting av signalet i tidsbilet
plt.title('Opprinnelig signal (tidsbildet)')
plt.xlabel('tid (millisekunder)')

X = fft(x,N)/N
b = [i for i in range(int(N/2))]                      # Fouriertransformasjon
frekv = (Fs/2)*np.linspace(0,1,N/2);  # Frekvensvektor (for plot)
"""
Plotter bare lengden paa frekvenskomponentene i frekvensspekteret.
Velger aa bare ta med frekvenser opp til halve samplingsfrekvensen.
"""
plt.figure()                  # Hindrer overskriving av forrige figur
plt.plot(frekv,2*np.abs(X(b,N/2))) # Plotter halvparten av fourierspekteret
plt.title('Absolutt-verdier av frekvensspekteret')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('|X(frekv)|')
plt.show()
