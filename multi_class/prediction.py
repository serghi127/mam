import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from tensorflow.python.keras.models import load_model
from tensorflow import keras
#from keras import load_model

fs = 16000
seconds = 2
filename = "prediction.wav"
class_names = ["Tzentayay", "Wen intinawe", "ok"]

model = load_model("multi_class/saved_model/WWD.h5")
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
    print("Tsentayay: " + str(prediction[:, 0]))
    print("Wen intinawe: " + str(prediction[:, 1]))
    print("Sik tintinawe: " + str(prediction[:, 2]))
    print("Te jatey: " + str(prediction[:, 3]))
    if prediction[:, 0] > 0.99:
        print(f"Tsentayay")
        print("Confidence:", prediction[:, 0])
        i += 1
    elif prediction[:, 1] > 0.99:
        print("Wen intinawe")
        print("Confidence: ", prediction[:, 1])
    elif prediction[:, 2] > 0.99:
        print("Sik tintinawe")
        print("Confidence: ", prediction[:, 2])
    elif prediction[:, 3] > 0.99:
        print("Te jatey")
        print("Confidence: ", prediction[:, 3])
    else:
        print("None")
    print("\n")