###### IMPORTS ################
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random 

num_images = 2

for i in range(num_images):
    walley_sample = "mam_phrases/p1/s" + str(random.randint(4, 120)) + ".wav"
    data, sample_rate = librosa.load(walley_sample)
    librosa.display.waveshow(data, sr=sample_rate)
    plt.show()

for i in range(num_images):
    walley_sample = "mam_phrases/p2/s" + str(random.randint(0, 120)) + ".wav"
    data, sample_rate = librosa.load(walley_sample)
    librosa.display.waveshow(data, sr=sample_rate)
    plt.show()

for i in range(num_images):
    walley_sample = "mam_phrases/p3/s" + str(random.randint(0, 50)) + ".wav"
    data, sample_rate = librosa.load(walley_sample)
    librosa.display.waveshow(data, sr=sample_rate)
    plt.show()