import struct

sample_finetune_dictionary = {
    b'\x00': 0,
    b'\x01': 1,
    b'\x02': 2,
    b'\x03': 3,
    b'\x04': 4,
    b'\x05': 5,
    b'\x06': 6,
    b'\x07': 7,
    b'\x08': -8,
    b'\x09': -7,
    b'\x0a': -6,
    b'\x0b': -5,
    b'\x0c': -4,
    b'\x0d': -3,
    b'\x0e': -2,
    b'\x0f': -1
}

class Mod:
    def __init__(self, path):
        file_data = open(path, 'rb').read()
        self.data = bytearray(file_data)

    def get_song_name(self):
        data = self.data[0:20]
        data_tuple = struct.unpack('c' * 20, data)
        song_name = b''.join(data_tuple).decode()
        return song_name

    def get_sample_name(self, num=0):
        offset = num * 30
        data = self.data[20 + offset:42 + offset]
        data_tuple = struct.unpack('c' * 22, data)
        sample_name = b''.join(data_tuple).decode()
        return sample_name

    def get_sample_length(self, num=0):
        data = self.data[42:44]
        data_unpack = struct.unpack('>H', data)[0]
        return data_unpack

    def get_sample_finetune(self, num=1):
        offset = num * 30
        data = self.data[44 + offset:45 + offset]
        unpack = struct.unpack('>c', data)[0]
        return sample_finetune_dictionary[unpack]


my_mod = Mod('addicti_milkytracker_modified.mod')
print(my_mod.get_song_name())

for i in range(31):
    print(my_mod.get_sample_name(i))

print(my_mod.get_sample_length())
print(my_mod.get_sample_finetune())
