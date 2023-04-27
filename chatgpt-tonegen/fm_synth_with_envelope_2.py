import math
import struct
import wave
import numpy as np

def generate_envelope(a, d, s, r, length, sample_rate):
    attack_samples = int(a * sample_rate)
    decay_samples = int(d * sample_rate)
    sustain_level = s
    release_samples = int(r * sample_rate)
    
    envelope = np.zeros(length)
    
    for i in range(attack_samples):
        envelope[i] = i / attack_samples
    
    for i in range(attack_samples, attack_samples + decay_samples):
        envelope[i] = 1 - (1 - sustain_level) * (i - attack_samples) / decay_samples
    
    for i in range(attack_samples + decay_samples, length - release_samples):
        envelope[i] = sustain_level
    
    for i in range(length - release_samples, length):
        envelope[i] = sustain_level * (1 - (i - (length - release_samples)) / release_samples)
    
    return envelope

# Define the output wave file parameters
SAMPLE_WIDTH = 2  # bytes per sample
NUM_CHANNELS = 1  # mono
FRAME_RATE = 44100  # samples per second
DURATION = 5  # seconds

# Define the carrier wave frequency
CARRIER_FREQ = 21.83  # Hz

# Define the modulator wave parameters
MOD_FREQ = 174.61  # Hz
MOD_INDEX = 10  # modulation index (depth)
MOD_ENVELOPE = generate_envelope(0.1, 0.5, 0.5, 0.2, DURATION * FRAME_RATE, FRAME_RATE)  # amplitude envelope

# Calculate the number of frames and samples
num_frames = DURATION * FRAME_RATE
num_samples = num_frames * NUM_CHANNELS

# Generate the modulator wave
mod_wave = []
for i in range(num_frames):
    # Calculate the phase of the modulator wave
    mod_phase = 2 * math.pi * MOD_FREQ * i / FRAME_RATE
    
    # Calculate the amplitude of the modulator wave using the envelope
    mod_amp = MOD_ENVELOPE[i // (num_frames // len(MOD_ENVELOPE))]
    
    # Calculate the sample value of the modulator wave
    mod_sample = mod_amp * math.sin(mod_phase)
    
    mod_wave.append(mod_sample)

# Generate the carrier wave
carrier_wave = []
for i in range(num_frames):
    # Calculate the phase of the carrier wave
    carrier_phase = 2 * math.pi * CARRIER_FREQ * i / FRAME_RATE
    
    # Calculate the frequency deviation caused by the modulator wave
    freq_deviation = MOD_INDEX * mod_wave[i]
    
    # Calculate the sample value of the carrier wave
    carrier_sample = math.sin(carrier_phase + freq_deviation)
    
    carrier_wave.append(carrier_sample)

# Combine the modulator and carrier waves
output_wave = []
for i in range(num_frames):
    output_sample = carrier_wave[i] * mod_wave[i]
    output_wave.append(output_sample)

# Normalize the output wave to the range [-1, 1]
output_wave_max = max(output_wave)
output_wave_min = min(output_wave)
output_wave_range = max(abs(output_wave_max), abs(output_wave_min))
output_wave_normalized = [sample / output_wave_range for sample in output_wave]
output_wave_normalized = output_wave
# Convert the output wave to bytes
output_bytes = b''
for sample in output_wave_normalized:
    # Convert the sample value from float to integer in the range [-32768, 32767]
    sample_int = int(sample * 32767)
    
    # Pack the sample value as a 2-byte integer in little-endian byte order
    sample_bytes = struct.pack('<h', sample_int)
    
    # Append the sample bytes to the output byte string
    output_bytes += sample_bytes

# Write the output wave to a .wav file
with wave.open('fm_synth_with_envelope_2.wav', 'wb') as wave_file:
    wave_file.setparams((NUM_CHANNELS, SAMPLE_WIDTH, FRAME_RATE, num_samples, 'NONE', 'not compressed'))
    wave_file.writeframes(output_bytes)

print('Done.')
