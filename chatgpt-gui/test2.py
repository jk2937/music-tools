import tkinter as tk
from functools import partial
import numpy as np
import sounddevice as sd

# Step sequencer pattern
sequencer_pattern = [[1, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]]

# FM Synthesis parameters
carrier_freq = 440.0
modulator_freq = 220.0
index = 5
duration = 0.25
sample_rate = 44100


# Generate FM synthesis waveform
def generate_fm_waveform(carrier_freq, modulator_freq, index, duration, sample_rate):
    # Calculate time array
    t = np.linspace(0, duration, int(duration * sample_rate), False)

    # Calculate modulation waveform
    modulator_waveform = np.sin(2 * np.pi * modulator_freq * t)

    # Calculate carrier waveform
    carrier_waveform = np.sin(2 * np.pi * (carrier_freq + index * modulator_waveform) * t)

    # Combine modulator and carrier waveform
    waveform = 0.5 * carrier_waveform + 0.5 * modulator_waveform

    # Normalize waveform
    waveform /= np.max(np.abs(waveform))

    return waveform


# Generate audio from step sequencer pattern
def generate_audio_from_pattern(pattern):
    # Initialize audio buffer
    audio = np.zeros(len(pattern) * int(duration * sample_rate))

    # Iterate through each step in pattern
    for i, step in enumerate(pattern):
        # Check if step is active
        if step:
            # Calculate frequency based on step index
            frequency = carrier_freq * (2 ** (i / 12))

            # Generate waveform
            waveform = generate_fm_waveform(frequency, modulator_freq, index, duration, sample_rate)

            # Add waveform to audio buffer
            audio[i * int(duration * sample_rate):(i + 1) * int(duration * sample_rate)] = waveform

    return audio


# Play audio
def play_audio(audio):
    sd.play(audio, sample_rate, blocking=True)


# GUI
def on_button_click():
    # Get pattern from sequencer grid
    pattern = [[button_var.get() for button_var in row] for row in button_vars]

    # Generate audio from pattern
    audio = generate_audio_from_pattern(pattern)

    # Play audio
    play_audio(audio)


# Initialize GUI
root = tk.Tk()

# Create button variables
button_vars = [[tk.IntVar() for j in range(len(sequencer_pattern[0]))] for i in range(len(sequencer_pattern))]

# Create sequencer grid
for i, row in enumerate(button_vars):
    for j, button_var in enumerate(row):
        button = tk.Checkbutton(root, variable=button_var, onvalue=1, offvalue=0, width=2, height=1)
        button.grid(row=i, column=j)

# Create play button
play_button = tk.Button(root, text="Play", command=on_button_click)
play_button.grid(row=len(button_vars), columnspan=len(button_vars[0]))

# Start GUI event loop
root.mainloop()

