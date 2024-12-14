import sys
import time
import os
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
    # upload_code("COM1", f.replace(".cpe", ".decompiled"))
    decompile_file(f)
    os.remove(f.replace(".cpe", ".decompiled"))
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decompiler.py <input_file>")
    else:
        run(sys.argv[1])