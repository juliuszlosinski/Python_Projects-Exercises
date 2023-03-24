"""
Juliusz Łosiński ~ 24.03.2023
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_FFT(serie: list) -> tuple:
    """
    Calculate FFT and frequency values based on passed serie.
    :param serie: Data from axis.
    :return: Tuple value, that contains FFT and frequency value.
    """
    fs = 6666
    window = np.hamming(len(serie))
    fft = np.abs(np.fft.rfft(serie * window))
    freq = np.fft.rfftfreq(len(serie), 1 / fs)
    return fft, freq


# 1. Reading axis data from "data.csv" file.
data_frame = pd.read_csv('data.csv')
ax = data_frame["ax"].values.tolist()
ay = data_frame["ay"].values.tolist()
az = data_frame["az"].values.tolist()

# 2. Calculate FFT and frequency values by using get_FFT function.
(ax_fft, ax_freq) = get_FFT(ax)
(ay_fft, ay_freq) = get_FFT(ay)
(az_fft, az_freq) = get_FFT(az)

# 3. Saving results to pandas data frame/ file.
data_frame = {
    'ax_fft': list(ax_fft),
    'ax_freq': list(ax_freq),
    'ay_fft': list(ay_fft),
    'ay_freq': list(ay_freq),
    'az_fft': list(az_fft),
    'az_freq': list(az_freq)
}

df = pd.DataFrame(data_frame)

df.to_csv("fft_results.csv", index=False)

# 4. Creating first chart.
plt.plot(ax_freq, ax_fft, "-r", label="ax")
plt.plot(ay_freq, ay_fft, "-g", label="ay")
plt.plot(az_freq, az_fft, "-b", label="az")
plt.title("Wartość FFT (częstotliwość)")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Wartość FFT ~ Amplituda")
plt.legend(loc="upper right")
plt.grid()
plt.show()

# 5. Creating second chart.
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Wartość FFT (częstotliwość)')
ax1.plot(ax_freq, ax_fft)
ax2.plot(ax_freq, ay_fft)
ax3.plot(ax_freq, az_fft)
plt.show()

# 6. Finding the maximum frequency.
maximum_frequency = max(
    list([max(ax_fft), max(ay_fft), max(az_fft)])
)

# 7. Printing the result.
print(f"Maximum frequency: {maximum_frequency}")
