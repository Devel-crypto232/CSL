from __future__ import division

import os
import shutil
from tkinter import *
from shared import run_exec
import ctypes
import time
################################################################################
"""

© CSL, Intelligente .Inc 2024

This python script was legally copyrighted in Cairo Governate, read the following agreements before editing and publishing edited versions of our scripts

1. Intelligente™ is not responsible for any copies made from this code for malicious purposes. If done, legal action will be taken.

2. Permission must be taken from Intelligente™ and accepted or legal action will be taken










"""
##################################################################################
var = {"delaytime": 5}
def run():
    h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)  # Get taskbar handle
    ctypes.windll.user32.ShowWindow(h, 0)  # Hide taskbar
    class CLI:
        def __init__(self, root):
            self.root = root
            self.path = "C\\"
            self.root.geometry("900x500")
            self.root.title("Terminal")
            self.text_area = Text(root, font=("Arial", 10), background="black", foreground="white", border=None, borderwidth=0)
            self.text_area.pack(fill=BOTH, expand=True)
            self.entry_widget = Entry(root, font=("Arial", 10), background="white", foreground="black", border=None, borderwidth=0)
            self.entry_widget.pack(fill=X)
            self.entry_widget.focus_set()
            self.text_area.insert(END, f"CSL {self.path}< \n")
            self.text_area.config(state=DISABLED)
            self.root.bind("<Return>", self.run_command)

        def run_command(self, event):
            command = self.entry_widget.get()
            self.text_area.config(state=NORMAL)
            self.text_area.insert(END, f"CSL {self.path}< {command}\n")
            self.text_area.see(END)
            commands = command.replace(f"CSL {self.path}< ", "").split(" ")
            if commands[0] != "exit" and commands[0] != "cd" and commands[0] != "dir" and commands[0] != "mkdir" and commands[0] != "rmdir" and commands[0] != "set" and commands[0] != "echo" and commands[0] != "file" and commands[0] != "read" and commands[0] != "poweroff":
                if not ".cpe" in commands[0]:
                    try:
                        run_exec.run("..\\..\\HDD\\"+self.path+commands[0]+".cpe")
                        time.sleep(var["delaytime"])
                        run_exec.run("..\\..\\HDD\\C\\CSL\\end.cpe")
                        self.text_area.insert(END, self.path + commands[0] + ".cpe ran successfully!\n")
                    except FileNotFoundError:
                        self.text_area.insert(END, f"{self.path}{commands[0]}.cpe was not found\n")
                else:
                    try:
                        run_exec.run("..\\..\\HDD\\"+self.path+commands[0])
                        time.sleep(var["delaytime"])
                        run_exec.run("..\\..\\HDD\\C\\CSL\\end.cpe")
                        self.text_area.insert(END, self.path+commands[0] + " ran successfully!\n")
                    except FileNotFoundError:
                        self.text_area.insert(END, self.path+commands[0] + " was not found\n")
            
            elif commands[0] == "exit":
                h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)  # Get taskbar handle
                ctypes.windll.user32.ShowWindow(h, 1)  # Hide taskbar
                exit()
            elif commands[0] == "cd":
                if os.path.exists("..\\..\\HDD\\"+self.path+commands[1]) and commands[1] != "..\\" and commands[1] != "../":
                    self.path += commands[1]+"\\"
                    self.text_area.insert(END, f"Directory changed to {self.path}\n")
                elif not os.path.exists("..\\..\\HDD\\"+self.path+commands[1]):
                    self.text_area.insert(END, f"{commands[1]} does not exist\n")
                elif commands[1] == "..\\" or commands[1] == "../":
                    ps = self.path.split("\\")
                    self.path = self.path.replace(ps[-2]+"\\", "")
                    self.text_area.insert(END, f"Directory changed to {self.path}\n")
            elif commands[0] == "dir":
                output = os.popen(f"dir {'..\\..\\HDD\\'+self.path}").read()
                self.text_area.insert(END, output)
            elif commands[0] == "mkdir":
                os.mkdir(f"..\\..\\HDD\\{self.path}{commands[1]}")
                self.text_area.insert(END, f"Directory {commands[1]} created\n")
            elif commands[0] == "rmdir":
                shutil.rmtree(f"..\\..\\HDD\\{self.path}{commands[1]}")
                self.text_area.insert(END, f"Directory {commands[1]} removed\n")
            elif commands[0] == "set":
                if commands[3] == "int":
                    var[commands[1]] = int(commands[2])
                elif commands[3] == "str":
                    var[commands[1]] = commands[2]
                self.text_area.insert(END, f"{commands[1]} set to {commands[2]}\n")
            elif commands[0] == "echo":
                if commands[1][0] != "%" and commands[1][-1] != "%":
                    self.text_area.insert(END, f"{commands[1]}\n")
                else:
                    self.text_area.insert(END, f"{var[commands[1].replace("%", "")]}\n")
            elif commands[0] == "file":
                try:
                    with open("..\\..\\HDD\\" + self.path + commands[1], "w") as file:
                        file.write(commands[2])
                except IndexError:
                    self.text_area.insert(END, f"Usage: file <file name> <contents>\n")
            elif commands[0] == "read":
                try:
                    string = ""
                    for i in open("..\\..\\HDD\\" + self.path + commands[1]).readlines():
                        string += i
                    self.text_area.insert(END, f"{string}\n")
                except IndexError:
                    self.text_area.insert(END, f"Usage: read <file name>\n")
            elif commands[0] == "poweroff":
                h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)  # Get taskbar handle
                ctypes.windll.user32.ShowWindow(h, 1)  # Hide taskbar
                os.system("taskkill /F /IM python.exe")
            self.text_area.insert(END, f"CSL {self.path}< \n")
            self.entry_widget.delete(0, END)
            self.text_area.config(state=DISABLED)
            self.entry_widget.focus_set()

    root = Tk()
    cli = CLI(root)
    root.mainloop()
    h = ctypes.windll.user32.FindWindowA(b'Shell_TrayWnd', None)  # Get taskbar handle
    ctypes.windll.user32.ShowWindow(h, 1)  # Hide taskbar
run()