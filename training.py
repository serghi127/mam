import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, classification_report 
#from plot_cm import plot_confusion_matrix

df = pd.read_pickle("final_audio_data_csv/audio_data.csv")
X = df["feature"].values
X = np.concatenate(X, axis=0).reshape(len(X),40)

y = np.array(df["class_label"].tolist())
y = to_categorical(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
model = Sequential([
    Dense(256, input_shape=X_train[0].shape),
    Activation('relu'),
    Dropout(0.5),
    Dense(256),
    Activation('relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')
])

print(model.summary())

model.compile(
    loss="categorical_crossentropy",
    optimizer='adam',
    metrics=['accuracy']
)

print("Model Score: \n")
history = model.fit(X_train, y_train, epochs=1000)
model.save("saved_model/WWD.h5")
score = model.evaluate(X_test, y_test)
print(score)

#### Evaluating our model ###########
print("Model Classification Report: \n")
y_pred = np.argmax(model.predict(X_test), axis=1)
y_test = np.argmax(y_test, axis = 1)
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
cm_display.plot()
plt.show()

# cm = confusion_matrix(np.argmax(y_test, axis=1), y_pred)
# print(classification_report(np.argmax(y_test, axis=1), y_pred))
# plot_confusion_matrix(cm, classes=["Tzentayay", "Wen intinawe"])