import math
import wave
import struct

# Set the sample rate and duration of the sound
sample_rate = 44100
duration = 5  # seconds

# Set the frequency and modulation index of the carrier wave
carrier_freq = 440
mod_index = 10

# Set the frequency and modulation index of the modulating wave
mod_freq = 220
mod_amp = 2

# Calculate the number of samples in the sound
num_samples = duration * sample_rate

# Calculate the angular frequency of the carrier wave
carrier_angular_freq = 2 * math.pi * carrier_freq

# Create a list to hold the samples of the sound
samples = []

# Generate each sample of the sound
for i in range(num_samples):
    # Calculate the current time in seconds
    time = i / sample_rate
    
    # Calculate the value of the modulating wave at the current time
    mod_value = mod_amp * math.sin(2 * math.pi * mod_freq * time)
    
    # Calculate the instantaneous frequency of the carrier wave
    inst_freq = carrier_freq + mod_index * mod_value
    
    # Calculate the value of the carrier wave at the current time
    carrier_value = math.sin(carrier_angular_freq * time)
    
    # Calculate the value of the FM synthesis sound at the current time
    sample = carrier_value * math.sin(2 * math.pi * inst_freq * time)
    
    # Add the sample to the list of samples
    samples.append(sample)

# Convert the list of samples to a bytes object
sample_bytes = bytearray()
for sample in samples:
    sample_bytes.extend(struct.pack('<h', int(sample * 32767)))

# Create a wave file and write the samples to it
with wave.open('fm_synth_sound.wav', 'wb') as wave_file:
    wave_file.setnchannels(1)
    wave_file.setsampwidth(2)
    wave_file.setframerate(sample_rate)
    wave_file.writeframes(sample_bytes)

print('Done.')