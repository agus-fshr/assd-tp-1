import scipy.signal as signal
import numpy as np

class AntiAliasingFilter:
    def __init__(self, cutoff, fs, order=5):
        self.cutoff = cutoff
        self.fs = fs
        self.order = order
        self.b, self.a = signal.butter(order, cutoff / (0.5 * fs), btype='low', analog=False)

    def process(self, input_signal):
        output_signal = signal.lfilter(self.b, self.a, input_signal)
        return np.array(output_signal)

class SampleAndHoldSystem:
    def __init__(self, sampling_period, analog_switch):
        self.sampling_period = sampling_period
        self.held_value = None
        self.time_since_last_sample = 0
        self.analog_switch = analog_switch
        self.dt = sampling_period / 10

    def process(self, input_signal):
        output_signal = []
        for sample in input_signal:
            if self.time_since_last_sample >= self.sampling_period:
                self.held_value = sample
                self.time_since_last_sample = 0
                self.analog_switch.enable()
            self.time_since_last_sample += self.dt
            output_signal.append(self.held_value)
        return np.array(output_signal)

class AnalogSwitch:
    def __init__(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def process(self, input_signal):
        if self.enabled:
            return np.array(input_signal)
        else:
            return np.zeros_like(input_signal)

class RecoveringFilter:
    def __init__(self, cutoff, fs, order=5):
        self.cutoff = cutoff
        self.fs = fs
        self.order = order
        self.b, self.a = signal.butter(order, cutoff / (0.5 * fs), btype='low', analog=False)

    def process(self, input_signal):
        return signal.lfilter(self.b, self.a, input_signal, axis=0)

class Circuit:
    def __init__(self):
        self.components = []  # This will hold the components

    def add_component(self, component):
        self.components.append(component)

    def simulate(self, input_signal):
        output_signals = {}
        for component in self.components:
            if self.components.index(component) == 0:
                out_signal = component.process(input_signal)
            else:
                out_signal = component.process(output_signals[self.components[self.components.index(component) - 1]])
            output_signals[component] = out_signal
        return output_signals
