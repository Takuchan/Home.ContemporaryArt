from scipy.io import wavfile
import numpy as np
import os
import matplotlib.pyplot as plt

wav_fname = "./loop100601.wav"
samplerate,data = wavfile.read(filename=wav_fname)

np.savetxt("music.txt",data)

