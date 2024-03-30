import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

class Sim():
    def __init__(self, T, dt):
        self.T = T
        self.dt = dt
        self.time_array = np.arange(0, T, dt)
        self.wave = None
        self.aaf = None
        self.zoh = None
        self.switch = None
        self.recovery_filter = None
        self.output = None
        self.components = {
            'wave': self.wave,
            'aaf': self.aaf,
            'zoh': self.zoh,
            'switch': self.switch,
            'recovery_filter': self.recovery_filter
        }
        self.traces = {}

    def gen_square_wave(self, frequency: float, amplitude: float, duty_cycle: float):
        self.wave = amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)
        self.output = self.wave
        return amplitude * signal.square(2 * np.pi * frequency * self.time_array, duty=duty_cycle)

    def gen_sine_wave(self, frequency: float, amplitude: float):
        self.wave = amplitude * np.sin(2 * np.pi * frequency * self.time_array)
        self.output = self.wave
        return amplitude * np.sin(2 * np.pi * frequency * self.time_array)

    # Put the self.attrs in a map if they are True in the components map
    def makeCircuit(self, components):
        self.components = components

    # Propagate the wave through the circuit
    def simulate(self):
        curr_in_wave = []
        curr_out_wave = []
        self.traces = {}
        for k,v in self.components.items():
            if k == 'wave':
                curr_in_wave = self.wave
                self.traces[k] = curr_in_wave
                continue
            if v:
                curr_out_wave = v.apply(curr_in_wave, self.time_array)
                self.traces[k] = curr_out_wave
                curr_in_wave = curr_out_wave

        self.output = curr_out_wave
            
        return self.traces

                
# CHEVYSHEV TYPE I LOW PASS FILTER
class Chevy1_LPF:
    def __init__(self, fp=50e3, fa=2*50e3, Ap=1, Aa=40, maxord=10):
        self.enabled = False
        self.redesign(fp, fa, Ap, Aa, maxord)

    def redesign(self, fp=50e3, fa=2*50e3, Ap=1, Aa=40, maxord=10):
        self.Ap = Ap
        self.Aa = Aa
        self.fp = fp
        self.fa = fa

        self.ord = min(signal.cheb1ord(2*np.pi*fp, 2*np.pi*fa, Ap, Aa, analog=True)[0], maxord)
        self.b, self.a = signal.cheby1(self.ord, Ap, 2*np.pi*fp, btype='low', analog=True, output='ba')
        self.tf = signal.TransferFunction(self.b, self.a)
        self.lti = signal.lti(self.b, self.a)

    def plotPZMap(self):
        # Plot the poles and zeros of the filter
        z, p, k = signal.tf2zpk(self.b, self.a)
        plt.plot(np.real(z), np.imag(z), 'bo', label='Zeros')
        plt.plot(np.real(p), np.imag(p), 'rx', label='Poles')
        plt.title('Poles and Zeros')
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.grid(which='both', axis='both')
        plt.legend()
        plt.show()

    def plotResponse(self, f0, f1, ylim=[-50, 5]):
        # Plot the frequency response
        f_log = np.logspace(f0, f1, 1000)
        w_log = 2 * np.pi * f_log
        w, mag, phase = signal.bode(self.tf, w_log)
        f = w / (2 * np.pi)
        print("Filter order: ", self.ord)
        plt.semilogx(f, mag)
        plt.title('Chebyshev Type I frequency response')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Amplitude [dB]')
        plt.margins(0, 0.1)
        plt.grid(which='both', axis='both')
        plt.ylim(ylim)
        plt.show()

    def apply(self, wave, time):
        if not self.enabled:
            return wave
        # Filter the continuous signal doing the convolution of the input signal with the impulse response
        _, y, _ = signal.lsim(self.lti, wave, time)
        return y
    
    
class ZOH():
    def __init__(self, f_sample: float, sim: Sim):
        self.enabled = False
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

    def apply(self, in_wave, time):
        if not self.enabled:
            return in_wave
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
        self.enabled = False
        self.f_sample = f_sample
        self.T = sim.T
        self.dt = sim.dt

    def apply(self, in_wave, time):
        if not self.enabled:
            return in_wave
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
