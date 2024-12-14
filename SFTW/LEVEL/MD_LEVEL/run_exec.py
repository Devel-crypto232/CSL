from __future__ import division
import pyfirmata

import sys
import os

################################################################################
"""

© CSL, Intelligente .Inc 2024

This python script was legally copyrighted in Cairo Governate, read the following agreements before editing and publishing edited versions of our scripts

1. Intelligente™ is not responsible for any copies made from this code for malicious purposes. If done, legal action will be taken.

2. Permission must be taken from Intelligente™ and accepted or legal action will be taken










"""
##################################################################################

def upload_code(port, filename):
        """Upload code to an Arduino board."""

        # Create a new board object
        board = pyfirmata.Arduino(port)

        # Upload the code
        with open(filename, 'r') as file:
            code = file.read()
        board.send_sysex(0x01, code)

        # Close the board
        board.exit()


def ascii_to_bin(string):
    """Convert a string of ASCII characters to a binary representation."""
    rs = ""
    for i in string:
        if ord(i) == 15:
            rs += '0'
        elif ord(i) == 16:
            rs += '1'
    return rs


def bin_to_string(binary_string):
    """Convert a binary string to a regular string."""
    result = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        result += chr(int(byte, 2))
    return result


def decompile_file(input_file):
    """Decompile the input file and write the output to a new file."""
    output_file = input_file.replace(".cpe", ".decompiled")
    with open(input_file, "r") as file:
        binary_string = file.read()

    ascii_string = ascii_to_bin(binary_string)
    decompiled_string = bin_to_string(ascii_string)

    with open(output_file, "w") as output:
        output.write(decompiled_string)


def run(f):
    import serial.tools.list_ports
    import time
    ports = list(serial.tools.list_ports.comports())
    com = None
    for port, desc, hwid in ports:
        if "Arduino" in desc or "CH340" in desc:  # adjust to your Arduino's description
            com = port
            break
    decompile_file(f)
    upload_code(com, f.replace(".cpe", ".decompiled"))
    os.system(f"del {f.replace(".cpe", ".decompiled")}")
    time.sleep(5)
    decompile_file("..\\..\\HDD\\C\\CSL\\end.cpe")
    upload_code(com, "..\\..\\HDD\\C\\CSL\\end.decompiled")
    os.system("del ..\\..\\HDD\\C\\CSL\\end.decompiled")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompiler.py <input_file>")
    else:
        run(sys.argv[1])