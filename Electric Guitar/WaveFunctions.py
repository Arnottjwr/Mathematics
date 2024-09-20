import numpy as np 
from scipy.fft import fft,fftfreq

def get_frequency(signal,sr):
    """
    Obtains the frequency values for a given signal and sample rate

    Parameters:
        signal (array-like): The input signal.
        sampling_rate (float): The sampling rate of the signal.

    Notes:
        Performs well for arrays of shape ~300 

    Credit:
        https://docs.scipy.org/doc/scipy/tutorial/fft.html#fast-fourier-transforms
    """

    N = len(signal)
    T = 1.0 / sr
    y = signal[:N]
    yf = fft(y)
    xf = fftfreq(N, T)[:N//2]    
    m = 2.0 / N * np.abs(yf[:N // 2])
    return xf, m        


def plucked_string(x,t,L,p,c,a,n): 

    """
    Returns a fourier representation of the wave equation 
    
    Parameters:
        x (array-like): Array to plot wave coefficients against 
        t (int): Time at which the string is plucked 
        L (int): Length of the string 
        v (int): Location of where the string is plucked 
        c (int): wave speed 
        a (int): Amplitude of initial pluck 
        n (int): Wave node; Sum for wave superposition at time t 
    """
    # Calculate the Wave Coefficient for the specified parameters 
    A = (2*a*(L**2))*np.sin(n*np.pi*p/L)/((n**2) * (np.pi**2) * p*(L-p))
    return A*np.sin((np.pi*n*x)/L)*np.cos((n*np.pi*c*t)/L)


    
def string_time_deriv(x0,t,L,p,c,a,n): 
    """
    Returns the time derivative of the string at a constant position x0 
    """
    return  (-2 * a * c * np.sin(n*np.pi*p/L) * np.sin(n*np.pi*x0/L) * np.sin(n*np.pi*c*t/L))/p*(L-p)*n*np.pi
