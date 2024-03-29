###### IMPORTS ################
import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

##### Doing this for every sample ##

all_data = []

data_path_dict = {
    0: ["mam_phrases/p1/" + file_path for file_path in os.listdir("mam_phrases/p1/")], #label tsentayay
    1: ["mam_phrases/p2/" + file_path for file_path in os.listdir("mam_phrases/p2/")], #label wen intinawe 
    2: ["mam_phrases/p3/" + file_path for file_path in os.listdir("mam_phrases/p3/")], #sik intinawe
    3: ["mam_phrases/p4/" + file_path for file_path in os.listdir("mam_phrases/p4/")] #te jatey
    #add more numbers to dictionary 
}

for class_label, list_of_files in data_path_dict.items():
    for single_file in list_of_files:
        audio, sample_rate = librosa.load(single_file) ## Loading file
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40) ## Apllying mfcc
        mfcc_processed = np.mean(mfcc.T, axis=0) ## some pre-processing
        all_data.append([mfcc_processed, class_label])
    print(f"Info: Succesfully Preprocessed Class Label {class_label}")

df = pd.DataFrame(all_data, columns=["feature", "class_label"])

###### SAVING FOR FUTURE USE ###
df.to_pickle("multi_class/final_audio_data_csv/audio_data.csv")