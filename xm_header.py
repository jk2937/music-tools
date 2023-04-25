import argparse

class xm_header:
    def __init__(self, data):
        self.id_text = data[:17].decode("ASCII")
        self.module_name = data[17:37].decode("ASCII")
        
        self.escape_char = data[37:38]
        
        self.tracker_name = data[38:58].decode("ASCII")
        
        self.version_number = str(data[59]) + "." + str(data[58])

        self.header_size = int.from_bytes(
            data[60:64], byteorder="little")
        self.song_length = int.from_bytes(
            data[64:66], byteorder="little")
        self.restart_position = int.from_bytes(
            data[66:68], byteorder="little")
        self.number_of_channels = int.from_bytes(
            data[68:70], byteorder="little")
        self.number_of_patterns = int.from_bytes(
            data[70:72], byteorder="little")
        self.number_of_instruments = int.from_bytes(
            data[72:74], byteorder="little")
            
        self.flags = data[74:76]
        
        self.default_tempo = int.from_bytes(data[76:78], byteorder="little")
        self.default_bpm = int.from_bytes(data[78:80], byteorder="little")
            
        self.pattern_order_table = data[80:80 + self.song_length]
        
    def __str__(self):
        out_str = "XM header:\n"
        out_str += "Filename: " + args.filename + "\n"
        out_str += "ID Text: " + header.id_text + "\n"
        out_str += "Module name: " + header.module_name + "\n"
        out_str += "Escape char: " + str(header.escape_char.hex()) + "\n"
        out_str += "Tracker name: " + header.tracker_name + "\n"
        out_str += "Version number: " + header.version_number + "\n"
        out_str += "Header size: " + str(header.header_size) + "\n"
        out_str += "Song length: " + str(header.song_length) + "\n"
        out_str += "Restart position: " + str(header.restart_position) + "\n"
        out_str += "Number of channels: " + str(header.number_of_channels) + "\n"
        out_str += "Number of patterns: " + str(header.number_of_patterns) + "\n"
        out_str += "Number of instruments: " + str(header.number_of_instruments) + "\n"
        out_str += "Flags: " + str(header.flags[:1].hex()) + " " + str(header.flags[1:3].hex()) + "\n"
        out_str += "Default tempo: " + str(header.default_tempo) + "\n"
        out_str += "Default BPM: " + str(header.default_bpm) + "\n"

        hex_str = str(header.pattern_order_table.hex()) + "\n"
        space_n = 2
        ot_out_str = ""
        
        for i in range(len(hex_str)):
            if i % space_n == space_n - 1:
                ot_out_str += hex_str[i - space_n:i] + " "

        out_str += "Pattern order table: " + ot_out_str + "\n"
        
        return out_str
        
    def print_info(self):
        print(self.__str__())

parser = argparse.ArgumentParser(
    prog="Display XM Header",
    description="Displays the header information from an .xm file.",
    epilog="Todo: Disclaimer and copyright.")
parser.add_argument("filename")
args = parser.parse_args()

in_file_data = open(args.filename, "rb").read()
header = xm_header(in_file_data)
header.print_info()

print("Done.")
