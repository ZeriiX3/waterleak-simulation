# features.py
import numpy as np
import pandas as pd
from scipy import signal

SAMPLING_RATE = 25600
FREQ_BANDS = [(0,1500),(1500,3000),(3000,5000),(5000,9000),(9000,12800)]
FEATURE_COLS = ['rms','variance','crest_factor','kurtosis'] + [f'energy_{a}_{b}' for a,b in FREQ_BANDS]

def extract_features_from_window(window: np.ndarray, fs: float) -> list:
    rms = np.sqrt(np.mean(window**2))
    variance = np.var(window)
    peak = np.max(np.abs(window))
    crest_factor = peak/rms if rms > 0 else 0
    kurtosis = pd.Series(window).kurtosis()
    freqs, psd = signal.welch(window, fs=fs, nperseg=min(1024, len(window)))
    bands = [np.sum(psd[np.where((freqs>=a)&(freqs<b))]) for a,b in FREQ_BANDS]
    return [rms, variance, crest_factor, kurtosis] + bands