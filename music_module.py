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
        self.data = [[Note(0, 0, 0, 0, 0) for i in range(length)] for j in range(channels)]

    def __str__(self):
        out = ''
        for step in range(len(self.data[0])):
            for channel in range(len(self.data)):
                #out += '(' + str(channel) + ', ' + str(step) + '):'
                out += str(self.data[channel][step].note)
            out += '\n'

        return out

    def AddNote(self, channel, step, note, instrument, volume, effect_type,
                effect_parameter):
        self.data[channel, step] = Note(note, instrument, volume,
                                         effect_type, effect_parameter)

class Note:
    def __init__(self, note, instrument, volume, effect_type, effect_parameter):
        self.note = note
        self.instrument = instrument
        self.volume = volume
        self.effect_type = effect_type
        self.effect_parameter = effect_parameter

    def __str__(self):
        return str(self.note)

m = Module()
m.AddPattern()
print(m.patterns[0])

p = m.patterns[0]
p.data[1][0] = Note(1, 0, 0, 0, 0)
print(p)

print('Done.')
