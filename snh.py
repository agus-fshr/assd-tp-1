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

    def gen_square_wave(self, frequency: float, amplitude: float, duty_cycle: float):
        self.square_wave = amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
        return amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
    
    def plot_square_wave(self, square_wave):
        plt.plot(self.time_array, square_wave)
        plt.xlim(0, 2 / square_wave.frequency)
        plt.show()

    def makeCircuit(self, components):
        for k, v in components.items():
            if v:
                self.components[k] = getattr(self, k, None)
            else:
                self.components[k] = None

    def simulate(self):
        curr_in_wave = []
        curr_out_wave = []
        self.traces = {}
        for k,v in self.components.items():
            if k == 'square_wave':
                curr_in_wave = self.square_wave
                continue
            if v:
                curr_out_wave = k.apply(curr_in_wave)
                self.traces[k] = curr_out_wave

                

    
class Filter():
    def __init__(self, fp=50e3, fa=2*50e3, Ap=1, Aa=40, fs=1e6):
        self.redesign(fp, fa, Ap, Aa, fs)

    def redesign(self, fp=50e3, fa=2*50e3, Ap=1, Aa=40, fs=1e6):
        self.fp = fp
        self.fa = fa
        self.Ap = Ap
        self.Aa = Aa
        self.fs = fs
        self.wp = fp / (fs/2)
        self.wa = fa / (fs/2)
        self.N, self.Wn = signal.cheb1ord(self.wp, self.wa, self.Ap, self.Aa)
        self.b, self.a = signal.cheby1(self.N, self.Ap, self.Wn, 'low')
        self.w, self.h = signal.freqz(self.b, self.a, fs=self.fs)
    
    def plot(self, title = 'Chebyshev Type I lowpass filter frequency response'):
        plt.figure()
        plt.semilogx(self.w, 20 * np.log10(abs(self.h)), 'b')
        plt.semilogx(self.Wn*self.fs/2, -self.Ap, 'ro')
        plt.title(title)
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude [dB]')
        plt.margins(0, 0.1)
        plt.grid(which='both', axis='both')
        plt.axvline(self.Wn*self.fs/2, color='green')
        plt.show()

    def apply(self, in_wave):
        out_wave = signal.lsim(self.b, self.a, in_wave)[1]
        return out_wave
    
class ZOH():
    def __init__(self, f_sample: float, sim: Sim):
        buf = 0
        self.zoh_mask = []
        for t in sim.T:
            buf += sim.dt
            if buf >= 1/f_sample:
                buf = 0
                self.zoh_mask.append(not self.zoh_mask[-1])
            else:
                if len(self.zoh_mask):
                    self.zoh_mask.append(self.zoh_mask[-1])
                else:
                    self.zoh_mask.append(True)

    def apply(self, in_wave):
        out_wave = []
        for i, v in enumerate(in_wave):
            if self.zoh_mask[i]:
                out_wave.append(v)
            else:
                hold_val = out_wave[-1]
                out_wave.append(hold_val)
        return out_wave
    
class Switch():
    def __init__(self, sim: Sim):
        # TODO: implement
        pass