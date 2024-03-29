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
            'square_wave': self.square_wave,
            'aaf': self.aaf,
            'zoh': self.zoh,
            'switch': self.switch,
            'recovery_filter': self.recovery_filter
        }
        self.traces = {}

    def gen_square_wave(self, frequency: float, amplitude: float, duty_cycle: float):
        self.square_wave = amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
        return amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
    
    def plot_square_wave(self, square_wave):
        plt.plot(self.time_array, square_wave)
        plt.xlim(0, 2 / square_wave.frequency)
        plt.show()

    # Put the self.attrs in a map if they are True in the components map
    def makeCircuit(self, components):
        self.components = components

    # Propagate the wave through the circuit
    # TODO: I think there is a bug here where the waves are not propagated correctly
    def simulate(self):
        curr_in_wave = []
        curr_out_wave = []
        self.traces = {}
        for k,v in self.components.items():
            if k == 'square_wave':
                curr_in_wave = self.square_wave
                self.traces[k] = curr_in_wave
                continue
            if v:
                curr_out_wave = v.apply(curr_in_wave)
                self.traces[k] = curr_out_wave
                curr_in_wave = curr_out_wave
            
        return self.traces

                

    
class Filter():
    def __init__(self, fp=50e3, fa=2*50e3, Ap=1, Aa=40, fs=1e6):
        self.redesign(fp, fa, Ap, Aa, fs)

    # Reinstantiate
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

    # TODO: Make sure lfilter/lsim are doing their thing here
    def apply(self, in_wave):
        out_wave = signal.lsim(self.b, self.a, in_wave)[1]
        return out_wave
    
class ZOH():
    def __init__(self, f_sample: float, sim: Sim):
        buf = 0
        self.zoh_mask = []
        for t in sim.time_array:
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
    def __init__(self, f_sample: float, sim: Sim):
        self.f_sample = f_sample
        self.T = sim.T
        self.dt = sim.dt

    def apply(self, in_wave):
        buf = 0
        out_wave = []
        switch_open = False
        for i, v in enumerate(in_wave):
            buf += self.dt
            if buf >= 1/self.f_sample:
                buf = 0
                switch_open = not switch_open
                if switch_open:
                    out_wave.append(0)
                else:
                    out_wave.append(v)
            else:
                if switch_open:
                    out_wave.append(0)
                else:
                    out_wave.append(v)
        return out_wave
