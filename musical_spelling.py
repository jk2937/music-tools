#This module contains data and functions for getting midi values from various
#musical spellings.

import math as m

intervals = {
	# First Species Consonances (Shoenberg) 
	"prime": [0, 0],

	"octave_above": [0, 12],
	"octave_below": [0, -12],

	"fifth_above": [0, 7],
	"fifth_below": [0, -7],

	"major_third_above": [0, 4],
	"major_thid_below": [0, -4],

	"minor_third_above": [0, 3],
	"minor_third_below": [0, -3],

	"major_sixth_above": [0, 9],
	"major_sixth_below": [0, -9],

	"minor_sixth_above": [0, 8],
	"minor_sixth_below": [0, -8],
}

ranges = {
	# First Species Consonances (Shoenberg)
	"treble": [57, 74],
	
	"soprano": [57, 73],
	"soprano_compass": [60, 71],
	"soprano_middle": [72, 77],

	"alto": [53, 69],
	"alto_compass": [55, 67],
	"alto_middle": [59, 64]
}

basic_pitch_letters = {
    "C": 0,
    "D": 2,
    "E": 4,
    "F": 5,
    "G": 7,
    "A": 9,
    "B": 11,
    
    "Cb": -1,
    "Db": 1,
    "Eb": 3,
    "Fb": 4,
    "Gb": 6,
    "Ab": 8,
    "Bb": 10,
    
    "C#": 1,
    "D#": 3,
    "E#": 5,
    "F#": 6,
    "G#": 8,
    "A#": 10,
    "B#": 12
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
def sp_to_int(letters):
    letter_list = letters.split()
    midi_value_list = []
    for letter in letter_list:
        midi_value_list.append(scientific_pitch_letters[letter])
    return midi_value_list

def int_to_sp(ints):
    letters = ""
    for i in range(0, len(ints)):
        letters += [key for key, value in scientific_pitch_letters.items() if value == ints[i]][-1]
        if i < len(ints) - 1:
            letters += " "
    return letters

wk_1 = " ____ "
wk_2 = "|    |"
wk_3 = "|____|"

bk_1 = "_____"
bk_2 = "|  | "
bk_3 = "|__| "

k_0 = '''\
 ____
|   |
|   |
|   |
|   |
|    
| a  
|____\
'''
k_1 = '''\
_____
  | |
  | |
a | |
__| |
|    
| b  
|____\
'''
k_2 = '''\
_____
  |  
  |  
a |  
__|  
|    
| b  
|____\
'''
k_3 = '''\
_____
|   |
|   |
|   |
|   |
|    
| a  
|____\
'''
k_4 = '''\
_____
|    |
|    |
|    |
|    |
|    |
| a  |
|____|\
'''

out_str = '\n' * len(k_0.splitlines())
for i in range(2): # octaves
	#print("i:", i)
	for j in range(7): # keys
		#print("j:", j)
		out_str_split = out_str.splitlines()
		if(j == 0): key = k_0
		if(j == 1): key = k_1
		if(j == 2): key = k_2
		if(j == 3): key = k_3
		if(j == 4): key = k_1
		if(j == 5): key = k_1
		if(j == 6): key = k_2
		if(j == 7): key = k_4
		key_split = key.splitlines()
		for k in range(len(key_split)):
			out_str_split[k] += key_split[k]
		out_str = '\n'.join(out_str_split)
# print(out_str)
		
'''
 __________________________________ 
|   |  | |  |  |   |  | |  | |  |  |
|   |  | |  |  |   |  | |  | |  |  |
|   |1 | |3 |  |   |g | |b | |d |  |
|   |__| |__|  |   |__| |__| |__|  |
|    |    |    |    |    |    |    |
| 0  | 2  | 4  | f  | a  | c  | e  |
|____|____|____|____|____|____|____|
'''

def to_unordered_pc_set(list_):
	list_ = to_list(list_)
	list_ = [x % 12 for x in list_]
	return list(set(list_))

def to_list(in_):
	if type(in_) == type(""):
		in_ = sp_to_int(in_)
	return in_

def to_keys(ints):
	ints = to_list(ints)
	lenth = max(ints) - min(ints)
	start = 12 * (min(ints) // 12)
	stop = 12 * m.ceil(max(ints) / 12)
	print("start:", start)
	print("stop:", stop)
	length = stop - start
	octaves = length // 12
	if(octaves == 0):
		octaves = 1
	print("octaves:", octaves)
	
