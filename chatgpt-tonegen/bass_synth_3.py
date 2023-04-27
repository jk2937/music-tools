import math
import wave
import struct

# Envelope function
def envelope(t, a, d, s, r):
    if t < a:
        return t/a
    elif t < a+d:
        return 1 - (1-s)*(t-a)/d
    elif t < a+d+s:
        return s
    else:
        return s*math.exp(-(t-a-d-s)/r)

# FM Synth function
def fm_synth(note_freq, mod_ratio, mod_index, duration, attack, decay, sustain, release, sample_rate):
    num_samples = int(duration * sample_rate)

    # Generate the carrier wave
    carrier_wave = []
    for i in range(num_samples):
        t = float(i) / sample_rate
        carrier_wave.append(math.sin(2.0*math.pi*note_freq*t))

    # Generate the modulator wave
    modulator_wave = []
    for i in range(num_samples):
        t = float(i) / sample_rate
        modulator_wave.append(math.sin(2.0*math.pi*(note_freq*mod_ratio + mod_index*math.sin(2.0*math.pi*note_freq*t))*t))

    # Generate the final wave with amplitude envelope applied
    final_wave = []
    for i in range(num_samples):
        t = float(i) / sample_rate
        env = envelope(t, attack, decay, sustain, release)
        final_wave.append(env*carrier_wave[i]*modulator_wave[i])

    # Convert to bytes
    wave_bytes = b""
    for sample in final_wave:
        sample = max(min(sample, 1.0), -1.0)
        wave_bytes += struct.pack('h', int(sample * 32767.0))

    # Write to file
    with wave.open("bass_synth_3.wav", 'w') as output_file:
        output_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))
        output_file.writeframes(wave_bytes)
        

# Example usage
#carierfreq, modratio, modamp, duration, a, s, d, r, samplerate

fm_synth(55.0, 2.0, 10.0, 2.0, 0.1, 0.1, 0.8, 0.5, 44100)

print('Done.')
