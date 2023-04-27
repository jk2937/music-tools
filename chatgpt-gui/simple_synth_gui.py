import tkinter as tk
import pyaudio
import numpy as np

# Define the audio parameters
SAMPLE_RATE = 44100
BUFFER_SIZE = 1024

# Define the synthesizer parameters
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
envelope = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Create the audio stream object
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=SAMPLE_RATE,
                output=True,
                frames_per_buffer=BUFFER_SIZE)

# Create the GUI
root = tk.Tk()
root.title("Simple Synthesizer")

# Define the widget callbacks
def play_sound():
    # Get the current slider values
    volume = volume_slider.get()
    frequency = frequencies[frequency_slider.get()]

    # Generate the waveform
    t = np.linspace(0, BUFFER_SIZE/SAMPLE_RATE, BUFFER_SIZE, False)
    waveform = envelope[0]*np.sin(2*np.pi*frequency*t)
    for i in range(1, len(envelope)):
        sustain_time = BUFFER_SIZE/SAMPLE_RATE - (len(envelope)-i)*BUFFER_SIZE/SAMPLE_RATE/5
        sustain_samples = int(sustain_time*SAMPLE_RATE)
        waveform[sustain_samples:] = envelope[i]*np.sin(2*np.pi*frequency*t[sustain_samples:])
    waveform *= volume

    # Apply the distortion effect
    waveform = np.tanh(waveform)

    # Play the audio
    stream.write(waveform.astype(np.float32).tobytes())

# Create the volume slider
volume_label = tk.Label(root, text="Volume")
volume_label.grid(row=0, column=0)
volume_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.01, orient=tk.HORIZONTAL)
volume_slider.set(0.5)
volume_slider.grid(row=0, column=1)

# Create the frequency slider
frequency_label = tk.Label(root, text="Frequency")
frequency_label.grid(row=1, column=0)
frequency_slider = tk.Scale(root, from_=0, to=len(frequencies)-1, orient=tk.HORIZONTAL)
frequency_slider.set(0)
frequency_slider.grid(row=1, column=1)

# Create the play button
play_button = tk.Button(root, text="Play", command=play_sound)
play_button.grid(row=2, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()

# Clean up the audio stream object
stream.stop_stream()
stream.close()
p.terminate()
