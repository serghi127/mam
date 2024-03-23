import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from tensorflow.python.keras.models import load_model
import base64
import requests
import json
import os
from time import sleep
#from keras import load_model

fs = 16000
seconds = 2
filename = "prediction.wav"
class_names = ["Tzentayay", "Wen intinawe", "ok"]

def text_to_speech(text, language, voice):
    url = "https://texttospeech.googleapis.com/v1/text:synthesize?key=" + api_key_stt
    headers = {"Content-Type": "application/json", "Accept": "audio/wav"}
    data = json.dumps({
        "input": {
            "text": text
        },
        "voice": {
            "languageCode": language,
            "name": voice  # Adjust voice parameters as needed
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16"  # Adjust audio encoding as needed
        }
    })
    
    response = requests.post(url, headers=headers, data=data)
    
    # Process the response
    if response.status_code == 200:
        audio_content_base64 = json.loads(response.text)["audioContent"]
        audio_content = base64.b64decode(audio_content_base64)
        with open("result.wav", "wb") as f:
            f.write(audio_content)

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
    if prediction[:, 0] > 0.99:
        print("tsentayay")
        print("Confidence:", prediction[:, 0])
        text_to_speech("Hola! Yo soy bien! Y tu?", "es-US", "es-ES-Standard-A")
        i += 1
    elif prediction[:, 1] > 0.99:
        print("Wen intinawe")
        print("Confidence: ", prediction[:, 1])
        text_to_speech("¡Qué bueno que te sientas bien!", "es-US", "es-ES-Standard-A")
    elif prediction[:, 2] > 0.99:
        print("Sik tintinawe")
        print("Confidence: ", prediction[:, 2])
        text_to_speech("Oh, lamento que te sientas cansado. ¿Quizás intentar ir a dormir?", "es-US", "es-ES-Standard-A")
    elif prediction[:, 3] > 0.99:
        print("Te jatey")
        print("Confidence: ", prediction[:, 3])
        text_to_speech("¡Mi clima favorito es cuando hace sol y hace calor! Pero también me encanta cuando nieva.", "es-US", "es-ES-Standard-A")
    else:
        print("None")
    os.system("C:/Users/sergh/OneDrive/Desktop/programming_files/python/mam/result.wav")
    input("Press enter to speak: ")
    print("\n")