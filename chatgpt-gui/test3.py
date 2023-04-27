import tkinter as tk
import numpy as np
import simpleaudio as sa

# define some constants
SAMPLE_RATE = 44100
DURATION = 0.1
N_CHANNELS = 1
N_OSCILLATORS = 4
FREQ_RATIO = 1.5
A = 0.5

# create the oscillator frequencies
freqs = np.zeros(N_OSCILLATORS)
freqs[0] = 440.0
for i in range(1, N_OSCILLATORS):
    freqs[i] = freqs[i - 1] * FREQ_RATIO

# define the function that generates the audio data
def generate_audio_data(freqs, pattern):
    t = np.linspace(0, DURATION, int(DURATION * SAMPLE_RATE), False)
    data = np.zeros(len(t))
    for i in range(N_OSCILLATORS):
        if pattern[i]:
            data += A * np.sin(2.0 * np.pi * freqs[i] * t)
    return data

# create the GUI
class StepSequencerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Step Sequencer")
        self.pattern = np.zeros(N_OSCILLATORS, dtype=bool)
        self.buttons = []
        for i in range(N_OSCILLATORS):
            button_row = []
            for j in range(16):
                button = tk.Button(master, bg="white", height=1, width=2,
                                   command=lambda i=i, j=j: self.toggle_button(i, j))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)
        play_button = tk.Button(master, text="Play", command=self.play)
        play_button.grid(row=N_OSCILLATORS + 1, columnspan=16)
        
    def toggle_button(self, i, j):
        self.pattern[i] ^= True
        color = "white" if self.pattern[i] else "black"
        self.buttons[i][j].config(bg=color)
        
    def play(self):
        audio_data = generate_audio_data(freqs, self.pattern)
        audio_data *= 32767 / np.max(np.abs(audio_data))
        audio_data = audio_data.astype(np.int16)
        player = sa.play_buffer(audio_data, N_CHANNELS, 2, SAMPLE_RATE)
        player.wait_done()

# start the GUI
root = tk.Tk()
gui = StepSequencerGUI(root)
root.mainloop()

