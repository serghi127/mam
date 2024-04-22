import sounddevice as sd
from scipy.io.wavfile import write

def record_audio_and_save(save_path, n_times):
    """
    This function will run `n_times` and everytime you press Enter you have to speak the wake word

    Parameters
    ----------
    n_times: int, default=50
        The function will run n_times default is set to 50.

    save_path: str
        Where to save the wav file which is generated in every iteration.
    """

    input("To start recording Wake Word press Enter: ")
    for i in range(n_times):
        fs = 16000
        seconds = 2

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        write(save_path + "/s" + str(i+18) + ".wav", fs, myrecording)
        #input(f"Press to record next or two stop press ctrl + C ({i + 1}/{n_times}): ")
        print("next")

record_audio_and_save("mam_phrases/background",23)
