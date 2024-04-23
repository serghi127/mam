import sounddevice as sd
import numpy as np
import array
import wave

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

def save_as_wav(buffer, sample_rate, output_file):
    with wave.open(output_file, "w") as wf:
        wf.setnchannels(1)  # mono
        wf.setsampwidth(2)  # 16-bit
        wf.setframerate(sample_rate)
        wf.writeframes(buffer.tobytes())

# Example usage
duration = 5  # Duration of recording in seconds
sample_rate = 16000  # Sample rate
output_file = "sound.wav"

# Record audio to buffer
print("Recording...")
b = record_to_buffer(duration, sample_rate)
print("Recording finished.")

# Play back the recorded audio
print("Playing back...")
play_buffer(b, sample_rate)
print("Playback finished.")

# Save played audio as WAV
print("Saving as WAV...")
save_as_wav(b, sample_rate, output_file)
print("WAV file saved as:", output_file)