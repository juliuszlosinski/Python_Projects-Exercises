"""
Juliusz Łosiński ~ 24.03.2023
"""

import numpy as np
import pandas as pd
import scipy as scp


def add_noise(serie):
    (serie_fft, serie_freq) = get_FFT(serie)
    fs = 6666
    amp = max(serie_freq)
    noise = np.random.normal(-amp, amp, len(serie))
    serie += noise
    fnyquist = fs / 2
    low = min(serie_freq) / fnyquist
    high = max(serie_freq) / fnyquist
    b, a = scp.signal.butter(1000, [low, high], btype='band')
    serie = scp.signal.lfilter(b, a, serie)
    return serie


def get_FFT(serie) -> tuple:
    fs = 6666
    window = np.hamming(len(serie))
    fft = np.abs(np.fft.rfft(serie * window))
    freq = np.fft.rfftfreq(len(serie), 1 / fs)
    return fft, freq


data_frame = pd.read_csv('data.csv')
ax = data_frame["ax"].values.tolist()
ay = data_frame["ay"].values.tolist()
az = data_frame["az"].values.tolist()

(ax_fft, ax_freq) = get_FFT(ax)
(ay_fft, ay_freq) = get_FFT(ay)
(az_fft, az_freq) = get_FFT(az)

maximum_frequency = max(
    list([max(ax_fft), max(ay_fft), max(az_fft)])
)

print(f"Maximum frequency: {maximum_frequency}")