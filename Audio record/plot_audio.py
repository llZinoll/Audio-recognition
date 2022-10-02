import wave
import matplotlib.pyplot as plt
import numpy as np

obj  = wave.open("output.wav", "rb")

sample_freq = obj.getframerate()
number_sample = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close

time_audio = number_sample / sample_freq

print(time_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, time_audio, num = number_sample)

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.title("Audio signal")
plt.ylabel("Signal wave")
plt.xlabel("Time(s)")
plt.xlim(0, time_audio)
plt.show()