import numpy as np
import tkinter as tk
import threading
import time
import pyaudio


# Constants
SAMPLE_RATE = 44100
CHANNELS = 1
DTYPE = np.float32
BLOCK_SIZE = 2048

# Synth parameters
num_steps = 16
num_tracks = 8
step_duration = 0.2
attack = 0.01
decay = 0.1
sustain = 0.5
release = 0.5
notes = [440, 494, 523, 587, 659, 698, 784, 880]

# Synth state
pattern = np.zeros((num_steps, num_tracks), dtype=np.int)
note_lengths = np.zeros((num_steps, num_tracks), dtype=np.float32)
time_index = 0


# Audio callback function
def audio_callback(in_data, frame_count, time_info, status):
    global time_index
    
    # Generate audio data
    t = np.arange(time_index, time_index + frame_count) / SAMPLE_RATE
    time_index += frame_count
    
    data = np.zeros(frame_count, dtype=DTYPE)
    
    for i in range(num_tracks):
        track_data = np.zeros(frame_count, dtype=DTYPE)
        
        for j in range(num_steps):
            if pattern[j][i] == 1:
                length = note_lengths[j][i]
                if length > 0:
                    note_data = np.sin(2 * np.pi * notes[i] * t[:int(length * SAMPLE_RATE)])
                    envelope = np.ones_like(note_data)
                    envelope[:int(attack * SAMPLE_RATE)] = np.linspace(0, 1, int(attack * SAMPLE_RATE))
                    envelope[int(attack * SAMPLE_RATE):int((attack + decay) * SAMPLE_RATE)] = np.linspace(1, sustain, int(decay * SAMPLE_RATE))
                    envelope[int((length - release) * SAMPLE_RATE):int(length * SAMPLE_RATE)] = np.linspace(sustain, 0, int(release * SAMPLE_RATE))
                    track_data[:int(length * SAMPLE_RATE)] += note_data * envelope
        
        data += track_data
    
    # Clip data to prevent distortion
    data = np.clip(data, -1.0, 1.0)
    
    return (data.tobytes(), pyaudio.paContinue)


# GUI callback function
def on_button_click(i, j):
    if pattern[j][i] == 0:
        pattern[j][i] = 1
    else:
        pattern[j][i] = 0


# GUI setup
root = tk.Tk()
root.title("Step Sequencer")
root.geometry("800x400")

buttons = []

for i in range(num_tracks):
    row = []
    for j in range(num_steps):
        button = tk.Button(root, text="", width=2, height=1, command=lambda i=i, j=j: on_button_click(i, j))
        button.grid(row=i, column=j, padx=2, pady=2)
        row.append(button)
    buttons.append(row)

# Audio setup
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=SAMPLE_RATE, frames_per_buffer=BLOCK_SIZE, output=True, stream_callback=audio_callback)

# Start audio stream
stream.start_stream()


# Main loop
while True:
    root.update_idletasks()
    root.update()
    time.sleep(step_duration)

