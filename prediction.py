import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from tensorflow.python.keras.models import load_model

fs = 16000
seconds = 2
filename = "prediction.wav"
class_names = ["Tzentayay", "Wen intinawe"]

model = load_model("saved_model\\WWD.h5")
print("prediction started: \n")

i=0
while True:
    print("Say Now: ")
    myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, myrecording)

    audio, sample_rate = librosa.load(filename)
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfcc_processed = np.mean(mfcc.T, axis=0)

    prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))
    if prediction[:, 1] > 0.99:
        print(f"Wen intinawe")
        print("Confidence:", prediction[:, 1])
        i += 1
    else:
        print("Tsentayay")
        print("Confidence: ", prediction[:, 0])