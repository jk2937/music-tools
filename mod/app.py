# Copyright 2024 Jonathan Kaschak
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

class Sample:
    def __init__(self, header_data):
        self.header_data = header_data
        self.name = self.header_data[:22].decode("ASCII")
        self.length = int.from_bytes(self.header_data[22:24]) * 2
        #self.finetune = int.from_bytes(self.header_data[24:25], signed=True) 
        #self.finetune = int.from_bytes((bytearray(self.header_data[24:25])[0] >> 4) & 0x0f, signed=True)
        '''finetune_bytes = self.header_data[24:25]
        print("type(finetune_bytes): " + str(type(finetune_bytes)) + " (should be <class 'bytes'>)")
        print("finetune_bytes: " + str(finetune_bytes))
        finetune_nibble = bytearray(finetune_bytes)[0] & 0xf
        print("finetune_nibble: " + str(finetune_nibble))
        finetune_int = int.from_bytes(finetune_nibble, signed=True)
        print("finetune_int: " + str(finetune_int))'''
        self.finetune = self.header_data[24:25]
        self.volume = int.from_bytes(self.header_data[25:26])
        self.repeat_offset = int.from_bytes(self.header_data[26:28])
        self.repeat_length = int.from_bytes(self.header_data[28:30])

class Mod:
    def __init__(self, data, sample_blocks=31):
        self.data = data
        self.sample_blocks = sample_blocks
        self.song_name = data[:20].decode("ASCII")
        self.samples = []
        for i in range(self.sample_blocks):
            self.samples.append(Sample(self.data[20 + i * 30:50 + i * 30]))
        self.number_of_patterns = int.from_bytes(data[950:951])
        self.song_end_jump_position = int.from_bytes(data[951:952])
        self.pattern_table = data[952:1080]
        self.file_format_tag = data[1080:1084].decode("ASCII")
        self.pattern_and_sample_data = data[1084:]

    def print_info(self):
        #print(f"song_name: {self.song_name}")
        for sample in self.samples:
            '''print(f"sample name: {sample.name}")
            print(f"sample length: {sample.length}")'''
            print(f"sample funetune: {sample.finetune}")
            '''print(f"sample volume: {sample.volume}")
            print(f"sample repeat_offset: {sample.repeat_offset}")
            print(f"sample repeat_length: {sample.repeat_length}")'''
        '''print(f"number_of_patterns: {self.number_of_patterns}")
        print(f"song_end_jump_position: {self.song_end_jump_position}")
        print(f"pattern_table: {self.pattern_table}")
        print(f"file_format_tag: {self.file_format_tag}")'''
        #print(f"pattern_and_sample_data: {self.pattern_and_sample_data}")

if __name__ == "__main__":
    data = open("addicti_milkytracker_modified.mod", "rb").read()
    testmod = Mod(data)
    testmod.print_info()
