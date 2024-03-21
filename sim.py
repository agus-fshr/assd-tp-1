import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Create an array that represents time lasting one second with a resolution of 1us
SIM_RESOLUTION = 1e-6
time_array = np.arange(0, 1, SIM_RESOLUTION)

#   _____                   _   
#  |_   _|                 | |  
#    | |  _ __  _ __  _   _| |_ 
#    | | | '_ \| '_ \| | | | __|
#   _| |_| | | | |_) | |_| | |_ 
#  |_____|_| |_| .__/ \__,_|\__|
#              | |              
#              |_|              

def gen_square_wave(frequency, amplitude, duty_cycle, time_array):
    return amplitude * signal.square(2 * np.pi * frequency * time_array, duty=duty_cycle)

freq = 7.5e3
square_wave_in = gen_square_wave(freq, 1, 0.75, time_array)

# Plot the square wave
plt.plot(time_array, square_wave_in)
plt.xlim(0, 2 / freq)
plt.show()

#   ______ _ _ _            
#  |  ____(_) | |           
#  | |__   _| | |_ ___ _ __ 
#  |  __| | | | __/ _ \ '__|
#  | |    | | | ||  __/ |   
#  |_|    |_|_|\__\___|_|   
                          
                        
fp=50e3
fa=2*50e3
Ap=1
Aa=40
fs=1e6
wp = fp / (fs/2)
wa = fa / (fs/2)

# Design Chebyshev Type I filter
N, Wn = signal.cheb1ord(wp, wa, Ap, Aa)
b, a = signal.cheby1(N, Ap, Wn, 'low')

w, h = signal.freqz(b, a, fs=fs)

# Plot magnitude response
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

# Apply the filter to the square wave
filtered_square_wave = signal.lfilter(b, a, square_wave_in)

# Plot the original signal in blue
plt.plot(time_array, square_wave_in, 'b', label='Original signal')

# Plot the filtered signal in red
plt.plot(time_array, filtered_square_wave, 'r', label='Filtered signal')

# Add a legend
plt.legend()

# Add title and labels
plt.title('Original and Filtered Signals')
plt.xlabel('Time [s]')
plt.xlim(0, 0.4e-3)
plt.ylabel('Amplitude')

# Display the plot
plt.show()

#   __________  _    _ 
#  |___  / __ \| |  | |
#     / / |  | | |__| |
#    / /| |  | |  __  |
#   / /_| |__| | |  | |
#  /_____\____/|_|  |_|

# create an array of boolean values that alternates every 1/f_sample seconds from time_array
f_sample = 100e3
buf = 0
zoh_mask = []
for t in time_array:
    buf += SIM_RESOLUTION
    if buf >= 1/f_sample:
        buf = 0
        zoh_mask.append(not zoh_mask[-1])
    else:
        if len(zoh_mask):
            zoh_mask.append(zoh_mask[-1])
        else:
            zoh_mask.append(True)

zoh_filtered_square_wave = []
for i, c in enumerate(filtered_square_wave):
    if zoh_mask[i]:
        zoh_filtered_square_wave.append(c)
    else:
        hold_val = zoh_filtered_square_wave[-1]
        zoh_filtered_square_wave.append(hold_val)

# Plot the zoh_filtered_square_wave, filtered_square_wave and zoh_mask all on top of each other
plt.plot(time_array, filtered_square_wave, 'b', label='Filtered signal')
plt.plot(time_array, zoh_filtered_square_wave, 'r', label='ZOH filtered signal')
# plt.plot(time_array, zoh_mask, 'g', label='ZOH mask')
plt.legend()
plt.xlim(0, 2 / freq)
plt.show()
