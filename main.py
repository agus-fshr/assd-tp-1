import components as c
import numpy as np
import matplotlib.pyplot as plt

aa_filter = c.AntiAliasingFilter(cutoff=0.1, fs=1, order=5)
a_switch = c.AnalogSwitch()
sah_system = c.SampleAndHoldSystem(sampling_period=0.1, analog_switch=a_switch)
r_filter = c.RecoveringFilter(cutoff=0.1, fs=1, order=5)

# Create circuit and connect components
circuit = c.Circuit()
circuit.add_component(aa_filter)
circuit.add_component(sah_system)
circuit.add_component(a_switch)
circuit.add_component(r_filter)

# Create input wave
t = np.linspace(0, 1, 1000, endpoint=False)
freq = 50
input_signal = np.sin(2 * np.pi * freq * t)

# Run simulation
sim = circuit.simulate(input_signal)

# Plot the simulation result
plt.figure()
plt.plot(t, sim)
plt.title('Simulation Result')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()