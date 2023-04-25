#This module contains data and functions for getting midi values from various
#musical spellings.

basic_pitch_letters = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
    
    "C#": 1,
    "D#": 3,
    "E#": 5,
    "F#": 6,
    "G#": 8,
    "A#": 10,
    "B#": 12,
    
    "Cb": -1,
    "Db": 1,
    "Eb": 3,
    "Fb": 4,
    "Gb": 6,
    "Ab": 8,
    "Bb": 10,
}

scientific_pitch_letters = {}
for octave in range(0, 10):
    for letter in basic_pitch_letters:
        midi_val = basic_pitch_letters[letter] + 12 * (octave + 1)
        if midi_val >= 0 and midi_val < 128:
            scientific_pitch_letters[letter + str(octave)] = midi_val

pitch_class_letters = {}
for item in basic_pitch_letters:
    pitch_class_letters[item] = basic_pitch_letters[item] % 12

#This function returns a list of midi note values, given a string of musical
#pitches in scientific pitch notation seperated by spaces. For example, calling
#this function with the argument "Bb3 D4 F4" returns [58, 62, 65]
def m_vals_from_sp_letters(letters):
    letter_list = letters.split()
    midi_value_list = []
    for letter in letter_list:
        midi_value_list.append(scientific_pitch_letters[letter])
    return midi_value_list

def m_vals_from_pc_letters(letters):
    letter_list = letters.split()
    midi_value_list = []
    for letter in letter_list:
        midi_value_list.append(pitch_class_letters[letter])
    return midi_value_list