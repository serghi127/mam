import sounddevice as sd
import numpy as np
import array

def record_to_buffer(duration, sample_rate=44100):
    # Record sound
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Wait until recording is finished
    
    # Convert NumPy array to array.array
    buffer = array.array("h", recording.flatten())
    return buffer

def play_buffer(buffer, sample_rate=44100):
    sd.play(buffer, samplerate=sample_rate)
    sd.wait()  # Wait until playback is finished

# Example usage
duration = 5  # Duration of recording in seconds
sample_rate = 44100  # Sample rate

# Record audio to buffer
print("Recording...")
b = record_to_buffer(duration, sample_rate)
print("Recording finished.")

# Play back the recorded audio
print("Playing back...")
play_buffer(b, sample_rate)
print("Playback finished.")
