class Module:
    def __init__(self, channels=4):
        self.channels = channels
        self.pattern_order = []
        self.patterns = []

    def AddPattern(self, length=16):
        p = Pattern(length, self.channels)
        self.patterns.append(p)
        self.pattern_order.append(len(self.patterns))

class Pattern:
    def __init__(self, length, channels):
        self.length = length
        self.channels = channels
        self.data = [
            [Note() for i in range(self.length)] for j in range(self.channels)
        ]

    def __str__(self):
        out = ''
        for step in range(self.length):
            for channel in range(self.channels):
                out += '(' + str(channel) + ', ' + str(step) + '): '
                out += str(self.data[channel][step].note) + '	'
            out += '\n'

        return out

    def AddNote(self, channel, step, note, instrument, volume, effect_type,
                effect_parameter):
        self.data[channel, step] = Note(note, instrument, volume,
                                         effect_type, effect_parameter)

class Note:
    def __init__(self, note=0, instrument=0, volume=0, effect_type=0,
                 effect_parameter=0):
        self.note = note
        self.instrument = instrument
        self.volume = volume
        self.effect_type = effect_type
        self.effect_parameter = effect_parameter

    def __str__(self):
        return str(self.note)
        
class NoteIntegerList:
	pass
	
class PitchClassIntegerList:
	pass
	
class OrderedNoteSet(NoteIntegerList):
	pass
	
class UnorderedNoteSet(NoteIntegerList):
	pass	
	
class OrderedPitchClassSet(PitchClassIntegerList):
	pass
	
class UnorderedPitchClassSet(PitchClassIntegerList):
	pass

def listToBasicPattern(list):
	'''Takes a list of notes (int) and creates a Pattern with the notes
	using one channel and the length of the list.'''
	return Pattern
	
def rhythmToBasicPattern(list):
	'''Takes a list with 1 representing a note on, 0 representing a rest
	or note continuation, and -1 representing a note off and create a
	pattern with one channel and the length of the list playing the
	chromatic scale using that rhythm.'''
	return Pattern
	
def expandPattern(PatternA, multiplier):
	'''Takes creates a new pattern whose length is equal to the input
	pattern's length times the multiplier and copies the input to it,
	interpolating or removing data as needed.'''
	return PatternB
	
def firstNoteOnZero(Pattern):
	'''Transposes the pattern so the first note is 0'''
	return Pattern
	
def bottomNoteOnZero(Pattern):
	'''Transposes the pattern so the bottom note is 0'''
	return Pattern
	
def firstNoteOnZero(list):
	'''Transposes the list so the first note is 0'''
	return Pattern
	
def bottomNoteOnZero(list):
	'''Transposes the list so the bottom note is 0'''
	return Pattern
	
def indexToTransposition(PatternA, PatternB):
	'''Replaces the notes in PatternA with the notes of PatternB using
	the notes of PatternA as an index velue to choose notes from 
	PatternB'''
	pass
	
def noteToToneLoop(PatternA, PatternB):
	'''Replaces the notes in PatternA with the notes of PatternB by 
	choosing the next note in PatternB each time a new note is played in
	PatternA and replacing the note in PatternA with it.'''
	pass
	
def duplicateAndTranspose(PatternA, PatternB):
	'''Transposes and duplicates pattern A for every note in pattern B.
	'''
	pass
	
def copyPattern(PatternA, PatternB, step_offset=0, channel_offset=0):
	'''Copies pattern B to pattern A. If pattern B is longer than A it
	is cut off'''
	pass

m = Module()
m.AddPattern()
print(m.patterns[0])

p = m.patterns[0]
p.data[2][0] = Note(1)
print(p)

print('Done.')
