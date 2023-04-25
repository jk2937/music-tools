import argparse
import struct

class xm_header:
    def __init__(self, data):
        
        ( self.id_text, self.module_name, self.escape_char, self.tracker_name,
        self.version_number, self.header_size, self.song_length,
        self.restart_position, self.number_of_channels,
        self.number_of_patterns, self.number_of_instruments, self.flags,
        self.default_tempo, self.default_bpm, 
          ) = struct.unpack("<17s20s1b20s2sIHHHHH2sHH", data[0:80])
        
        self.pattern_order_table = data[80:80 + self.song_length]
        
    def __str__(self):
        out_str = "XM header:\n"
        out_str += "Filename: " + args.filename + "\n"
        out_str += "ID Text: " + str(header.id_text) + "\n"
        out_str += "Module name: " + str(header.module_name) + "\n"
        out_str += "Escape char: " + str(header.escape_char) + "\n"
        out_str += "Tracker name: " + str(header.tracker_name) + "\n"
        out_str += "Version number: " + str(header.version_number) + "\n"
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

