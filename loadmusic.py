from random import sample
from scipy.io import wavfile
import numpy as np
import os
import matplotlib.pyplot as plt

wav_fname = "./mottai.wav"
samplerate,data = wavfile.read(filename=wav_fname)

f = open('mottai_samplerate.txt','w',encoding="UTF-8")
f.write(str(samplerate))
f.close
plt.plot(data)
plt.show()
