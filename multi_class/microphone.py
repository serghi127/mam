# Write your code here :-)
import board
import array
import audiobusio
import digitalio
import time
import storage
import gc
import analogio
print(str(gc.mem_free())+"      ")

sample_rate = 16000
# Set up the microphone
mic_pin = board.GP28  # Adjust this pin according to your board's configuration
mic = analogio.AnalogIn(mic_pin)

#mic = audiobusio.PDMIn(clock_pin=mic_pin, data_pin=mic_pin, sample_rate=16000, bit_depth=16)

# Set up the recording parameters
record_duration = 3  # Record for 10 seconds

# Start recording
print("Recording...")
start_time = time.monotonic()

buffer = sample_rate * record_duration
# Create a buffer to store recorded audio
#buffer_size = 16000 * record_duration  # 16,000 samples per second * duration
#buffer = array.array('H', [0] * buffer_size)

print(mic.value)

# Read audio samples from the microphone and store them in the buffer
with open ("audio.wav", "w") as file:
    for i in range(buffer):
        #file.write(mic.value)
        #signed_int = (int)(mic.value-32768)
        #1082
        #file.write(array.array("h", [signed_int]).to_bytes(2, "big"))
        file.write(mic.value.to_bytes(2, "little"))
        time.sleep(1/sample_rate)
        gc.collect()

#for i in range(len(buffer)):
    #buffer[i] = mic.value

end_time = time.monotonic()
print("Recording finished.")

# Print the duration of the recorded audio
print("Duration:", end_time - start_time, "seconds")





# Write your code here :-)
import board
import array
import audiobusio
import digitalio
import time
import storage
import gc
import analogio
import adafruit_wave
print(str(gc.mem_free())+"      ")
import microcontroller
microcontroller.reset()

sample_rate = 16000
# Set up the microphone
mic_pin = board.GP28  # Adjust this pin according to your board's configuration
mic = analogio.AnalogIn(mic_pin)

#mic = audiobusio.PDMIn(clock_pin=mic_pin, data_pin=mic_pin, sample_rate=16000, bit_depth=16)

# Set up the recording parameters
record_duration = 3  # Record for 10 seconds

# Start recording
print("Recording...")
start_time = time.monotonic()

buffer = sample_rate * record_duration
# Create a buffer to store recorded audio
#buffer_size = 16000 * record_duration  # 6,000 samples per second * duration
#buffer = array.array('H', [0] * buffer_size)

print(mic.value)

with adafruit_wave.open("audio.wav", "wb") as file:
    file.setnchannels(1)
    file.setsampwidth(2)
    file.setframerate(sample_rate)
    #audio_buffer = bytearray()
    
    for i in range(buffer):
        #file.write(mic.value)
        #signed_int = mic.value if mic.value <= 32767 else mic.value - 65536
        #signed_int = max(-32768, min(32767, signed_int))
        
        #audio_buffer.extend(mic.value.to_bytes(2, 'little'))

        #signed_int = (int)(mic.value-32768)
        #1082
        #file.write(array.array("h", [signed_int]).to_bytes(2, "big"))
        #file.writeframesraw(bytes(signed_int))
        
        #try:
        #file.writeframes(bytes(mic.value))
        #file.writeframes(bytes(audio_buffer))
        #file.writeframesraw(bytes(audio_buffer))
        
        #except Exception as error:
        #    print("2 An exception occurred:", error)
        
        #file.write(signed_int.to_bytes(2, "little"))
        time.sleep(1/sample_rate)

# Read audio samples from the microphone and store them in the buffer

#for i in range(len(buffer)):
    #buffer[i] = mic.value

end_time = time.monotonic()
print("Recording finished.")

# Print the duration of the recorded audio
print("Duration:", end_time - start_time, "seconds")
