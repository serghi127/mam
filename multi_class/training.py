import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report 
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

#from plot_cm import plot_confusion_matrix

num_phrases = 4 #number of phrases
list_phrases = ["tsentaya", "wen intinawe", "sen intinawe", "te jatey"]

df = pd.read_pickle("multi_class/final_audio_data_csv/audio_data.csv")
X = df["feature"].values
X = np.concatenate(X, axis=0).reshape(len(X),40)

y = np.array(df["class_label"].tolist())
y = to_categorical(y, num_phrases)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
model = Sequential([
    Dense(256, input_shape=X_train[0].shape),
    Activation('relu'),
    Dropout(0.5),
    Dense(256),
    Activation('relu'),
    Dropout(0.5),
    Dense(num_phrases, activation='softmax')
])

print(model.summary())

model.compile(
    loss="categorical_crossentropy",
    optimizer='adam',
    metrics=['accuracy','categorical_accuracy']
)

print("Model Score: \n")
history = model.fit(X_train, y_train, epochs=1000)
model.save("multi_class/saved_model/WWD.h5")
score = model.evaluate(X_test, y_test)
print(score)

#### Evaluating our model ###########
print("Model Classification Report: \n")
y_pred = np.argmax(model.predict(X_test), axis = 1)
y_test_c = np.argmax(y_test, axis = 1)
#y_test_c = to_categorical(y_test, num_classes=num_phrases)


cm = confusion_matrix(y_test_c, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=list_phrases)
disp.plot()
plt.title("My confusion matrix")
plt.show()