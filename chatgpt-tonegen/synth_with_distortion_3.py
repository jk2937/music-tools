import struct
import math
import wave

# Define the parameters
duration = 2  # seconds
sample_rate = 44100  # samples per second

# Envelope parameters
attack = 0.1  # seconds
decay = 0.2  # seconds
sustain = 0.7
release = 0.3  # seconds

# FM synth parameters
carrier_freq = 43.65  # Hz
modulator_freq = 174.61  # Hz
modulation_index = 4
distortion_gain = 0.5

# Distortion parameters
distortion_threshold = 0.7

# Define the amplitude envelope function
def envelope(t):
    if t < attack:
        return t / attack
    elif t < attack + decay:
        return 1.0 - (1.0 - sustain) * ((t - attack) / decay)
    elif t < duration - release:
        return sustain
    else:
        return sustain * (1.0 - (t - duration + release) / release)

# Generate the raw audio data
num_samples = duration * sample_rate
data = b''
for i in range(num_samples):
    t = float(i) / sample_rate
    carrier_phase = 2.0 * math.pi * carrier_freq * t
    modulator_phase = 2.0 * math.pi * modulator_freq * t
    modulator_amplitude = envelope(t) * modulation_index * math.sin(modulator_phase)
    distortion_factor = distortion_gain * modulator_amplitude / sustain
    carrier_amplitude = math.sin(carrier_phase + distortion_factor)
    if abs(carrier_amplitude) > distortion_threshold:
        carrier_amplitude = math.copysign(1.0, carrier_amplitude)
    data += struct.pack('<h', int(32767 * carrier_amplitude))

# Write the raw audio data to a file
with wave.open('synth_with_distortion_3.wav', 'wb') as wav_file:
    wav_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))
    wav_file.writeframes(data)

print('Done.')
