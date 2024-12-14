from __future__ import division

import sys
import subprocess
################################################################################
"""

© CSL, Intelligente .Inc 2024

This python script was legally copyrighted in Cairo Governate, read the following agreements before editing and publishing edited versions of our scripts

1. Intelligente™ is not responsible for any copies made from this code for malicious purposes. If done, legal action will be taken.

2. Permission must be taken from Intelligente™ and accepted or legal action will be taken










"""
##################################################################################
with open(sys.argv[1].replace(".pe", ".cpe"), "w") as oooo:
    oooo.write("")

def bin_to_ascii(string):
    """Convert a string to a binary representation and then to ASCII characters."""
    rs = ""
    for i in string:
        chrord = ord(i)
        binchri = bin(chrord)[2:].zfill(8)  # Remove '0b' prefix and pad with zeros
        for i in binchri:
            if i == '0':
                rs += chr(15)  # ASCII value of 15
            elif i == '1':
                rs += chr(16)  # ASCII value of 16
    return rs+"\n"

def compile_file(input_file):
    """Compile the input file and write the output to a new file."""
    output_file = input_file.replace(".pe", ".cpe")
    with open(output_file, "a") as file:
        file.write(bin_to_ascii("""void setup() {\n"""))

        with open(input_file, "r") as input:
            for line in input:
                line = line.strip()  # Remove newline characters
                tokens = line.split(" ")
                is_setup = False
                is_loop = False

                if tokens[0] == "SETUP" and tokens[1] == "FUNC":
                    is_setup = True
                elif tokens[0] == "CONSOLE":
                    file.write(bin_to_ascii(f"\tSerial.begin({tokens[1]});\n"))
                elif tokens[0] == "END_SETUP":
                    file.write(bin_to_ascii("\n}\n"))
                    is_setup = False
                elif tokens[0] == "LOOP" and tokens[1] == "FUNC":
                    file.write(bin_to_ascii("void loop() {\n"))
                    is_loop = True
                elif tokens[0] == "END_LOOP":
                    file.write(bin_to_ascii("\n}\n"))
                    is_loop = False
                elif tokens[0] == "DIGITALPINC":
                    file.write(bin_to_ascii(f"\tdigitalWrite({tokens[1]}, {tokens[2]});\n"))
                elif tokens[0] == "DELAY":
                    file.write(bin_to_ascii(f"\tdelay({int(tokens[1]) * 1000});\n"))
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compiler.py <input_file>")
    else:
        compile_file(sys.argv[1])