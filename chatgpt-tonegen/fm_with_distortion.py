import math
import struct
import wave

# define the note parameters
note_duration = 3  # duration in seconds
sample_rate = 44100  # samples per second
attack_time = 0.1  # time in seconds to reach maximum amplitude
decay_time = 0.1  # time in seconds to decay to sustain level
sustain_amplitude = 0.5  # amplitude during sustain phase
release_time = 0.5  # time in seconds to reach zero amplitude
modulation_index = 5  # FM synthesis parameter
carrier_freq = 440  # frequency of the carrier signal
modulator_freq = 220  # frequency of the modulating signal
distortion_gain = 10.0  # gain of the distortion effect
distortion_threshold = 0.6  # threshold for soft clipping distortion

# define the amplitude envelope function
def envelope(attack, decay, sustain, release, duration, sample_rate):
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    sustain_samples = int(sustain * sample_rate)
    release_samples = int(release * sample_rate)
    total_samples = int(duration * sample_rate)
    envelope = [0] * total_samples
    for i in range(total_samples):
        if i < attack_samples:
            envelope[i] = i / attack_samples
        elif i < attack_samples + decay_samples:
            envelope[i] = 1.0 - (1.0 - sustain_amplitude) * ((i - attack_samples) / decay_samples)
        elif i < total_samples - release_samples:
            envelope[i] = sustain_amplitude
        else:
            envelope[i] = sustain_amplitude * (1.0 - ((i - total_samples + release_samples) / release_samples))
    return envelope

# define the soft clipping distortion function
def soft_clip(x, threshold):
    if x < -threshold:
        return -1
    elif x > threshold:
        return 1
    else:
        return x - ((x ** 3) / 3)

# generate the waveform samples
num_samples = note_duration * sample_rate
samples = []
t = 0
envelope_values = envelope(attack_time, decay_time, sustain_amplitude, release_time, note_duration, sample_rate)
for i in range(num_samples):
    modulator_amp = math.sin(2 * math.pi * modulator_freq * t)
    carrier_freq_with_modulation = carrier_freq + modulation_index * modulator_amp
    carrier_signal = math.sin(2 * math.pi * carrier_freq_with_modulation * t)
    distorted_signal = soft_clip(carrier_signal * distortion_gain, distortion_threshold)
    sample = distorted_signal * envelope_values[i]
    samples.append(sample)
    t += 1 / float(sample_rate)

# convert the samples to 16-bit values for writing to a wav file
samples_normalized = [int(sample * 32767) for sample in samples]
samples_struct = struct.pack('<' + ('h' * len(samples_normalized)), *samples_normalized)

# write the wav file
wav_file = wave.open('fm_with_distortion.wav', 'wb')
wav_file.setnchannels(1)
wav_file.setsampwidth(2)
wav_file.setframerate(sample_rate)
wav_file.writeframes(samples_struct)
wav_file.close()

print('Done.')
