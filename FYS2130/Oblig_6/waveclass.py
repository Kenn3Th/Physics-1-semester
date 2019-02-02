import numpy as np
class Wavelet:
    def __init__(self, omega):
        self.omega = omega

    def __call__(self,omegaa,K):
        omg = np.array(self.omega)
        omga = omegaa
        A = np.exp(-(K*((omg-omga)/omga))**2)
        B = np.exp(-K**2)*np.exp(-(K*omg/omga)**2)
        psi = 2*(A-B)
        return psi
