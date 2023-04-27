import wave
import struct
import math

# Set the sample rate and duration
sample_rate = 44100
duration = 5.0

# Set the carrier and modulator frequencies and ratios
carrier_freq = 440
modulator_freq = 220
modulation_index = 5

# Create the byte stream for the wave file
wave_bytes = bytearray()

# Iterate over each sample
for i in range(int(duration * sample_rate)):
    # Calculate the phase for the carrier and modulator waves
    carrier_phase = 2 * math.pi * i * carrier_freq / sample_rate
    modulator_phase = 2 * math.pi * i * modulator_freq / sample_rate

    # Calculate the modulating amplitude and the frequency of the carrier wave
    modulating_amplitude = math.sin(modulator_phase) * modulation_index
    carrier_wave_freq = carrier_freq + modulating_amplitude

    # Calculate the amplitude of the carrier wave
    amplitude = 32767 * math.sin(carrier_phase)

    # Pack the amplitude into a short int
    packed_amplitude = struct.pack("<h", int(amplitude))

    # Add the packed amplitude to the byte stream
    wave_bytes.extend(packed_amplitude)

# Create the wave file
wave_file = wave.open("fm_sound_2.wav", "wb")

# Set the parameters for the wave file
wave_file.setnchannels(1)
wave_file.setsampwidth(2)
wave_file.setframerate(sample_rate)

# Write the byte stream to the wave file
wave_file.writeframes(wave_bytes)

# Close the wave file
wave_file.close()

print('Done.')