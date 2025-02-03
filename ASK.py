//Python Code
import numpy as np
import matplotlib.pyplot as plt
# Parameters
data = [1, 0, 1, 0, 1, 1, 0, 1] # Binary data to be transmitted
bit_duration = 1 # Duration of each bit in seconds
fc = 10 # Carrier frequency in Hz
amplitude = 2 # Carrier amplitude
sampling_rate = 1000 # Number of samples per second
# Time vector
t = np.arange(0, bit_duration * len(data), 1/sampling_rate)
# Message signal
message_signal = np.repeat(data, sampling_rate * bit_duration)
# Carrier signal
carrier_signal = amplitude * np.sin(2 * np.pi * fc * t)
# ASK modulation
ask_signal = amplitude * message_signal * np.sin(2 * np.pi * fc * t)
# Plotting
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, message_signal)
plt.title('Message Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal)
plt.title('Carrier Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.plot(t, ask_signal)
plt.title('ASK Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
