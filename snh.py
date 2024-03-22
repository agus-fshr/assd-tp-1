import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

class Sim():
    def __init__(self, T, dt):
        self.T = T
        self.dt = dt
        self.time_array = np.arange(0, T, dt)
        self.square_wave = None
        self.aaf = None
        self.zoh = None
        self.switch = None
        self.recovery_filter = None
        self.components = {
            'square_wave': True,
            'aaf': True,
            'zoh': True,
            'switch': True,
            'recovery_filter': True
        }


    def gen_square_wave(self, frequency, amplitude, duty_cycle):
        self.square_wave = amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
        return amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
    
    def plot_square_wave(self, square_wave):
        plt.plot(self.time_array, square_wave)
        plt.xlim(0, 2 / square_wave.frequency)
        plt.show()
    
    def design_chebyshev_filter(self, fp, fa, Ap, Aa, fs):
        wp = fp / (fs/2)
        wa = fa / (fs/2)
        N, Wn = signal.cheb1ord(wp, wa, Ap, Aa)
        b, a = signal.cheby1(N, Ap, Wn, 'low')
        w, h = signal.freqz(b, a, fs=fs)
        return a, b, w, h, Wn, Ap, fs
        
    def plot_filter_response(self, w, h, Wn, Ap, fs):
        plt.figure()
        plt.semilogx(w, 20 * np.log10(abs(h)), 'b')  # Change to semilogx
        plt.semilogx(Wn*fs/2, -Ap, 'ro')  # Change to semilogx
        plt.title('Chebyshev Type I lowpass filter frequency response')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude [dB]')
        plt.margins(0, 0.1)
        plt.grid(which='both', axis='both')
        plt.axvline(Wn*fs/2, color='green')  # cutoff frequency
        plt.ylim(-50, 1)
        # plt.xlim(0, 90e3)
        plt.show()

    def apply_filter(self, b, a, in_wave):
        out_wave = signal.lfilter(b, a, in_wave)
        self.aaf = out_wave
        return out_wave