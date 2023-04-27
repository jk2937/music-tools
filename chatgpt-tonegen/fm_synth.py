import numpy as np
import soundfile as sf

# set parameters
fs = 44100
dur = 5
f_carrier = 440
f_modulator = 110
mod_index = 3
amp_env = np.linspace(1, 0, int(fs*dur))

# generate modulator and carrier signals
t = np.linspace(0, dur, int(fs*dur), False)
modulator = np.sin(2*np.pi*f_modulator*t) * mod_index
carrier = np.sin(2*np.pi*f_carrier*(t + modulator))

# apply amplitude envelope
carrier *= amp_env

# write to file
sf.write('fm_synth.wav', carrier, fs)

print('Done.')
