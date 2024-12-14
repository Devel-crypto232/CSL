import tkinter as tk
from tkinter import *
import os
import shutil
from shared import run_exec
import multiprocessing
import datetime
################################################################################
"""

© CSL, Intelligente .Inc 2024

This python script was legally copyrighted in Cairo Governate, read the following agreements before editing and publishing edited versions of our scripts

1. Intelligente™ is not responsible for any copies made from this code for malicious purposes. If done, legal action will be taken.

2. Permission must be taken from Intelligente™ and accepted or legal action will be taken










"""
##################################################################################
root = tk.Tk()
root.attributes("-fullscreen", True)
smo = False
hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
second = datetime.datetime.now().second
def make_app(x, y, icono, text, python_script):
    try:
        multiprocessing.freeze_support()
        icon = tk.PhotoImage(file=icono)
        label = tk.Button(root, image=icon, command=python_script)
        label.image = icon  # Keep a reference to the image
        label.place(x=x, y=y)
        ll = tk.Button(root, text=text, background=None, command=python_script)
        ll.place(x=x-10, y=y+40)
        
    except tk.TclError:
        print(f"Error: Unable to load image {icono}")


def desktop():
    image = tk.PhotoImage(file="background.png")
    background_label = tk.Label(root, image=image)
    background_label.image = image  # Keep a reference to the image
    background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the image


    make_app(50, 50, "terminal.png", "Terminal", lambda: os.system("python TERM.py"))
    make_app(150, 50, "shutdown.png", "Shutdown", lambda: exit())
    label_frame = tk.LabelFrame(root, width=1920, height=50)
    label_frame.place(x=0, y=1030)
    smi = tk.PhotoImage(file="supermenu.png")
    supermenuicon = tk.Button(root, image=smi, border=None, borderwidth=0, background="#ffffff", command=lambda: right_click())
    supermenuicon.image = smi  # Keep a reference to the image
    supermenuicon.place(x=10, y=1030)  # Center the image
    global smo
    smo = False
desktop()

def toggle(d):
    if d:
        return False
    else:
        return True
def right_click():
    global smo
    smo = toggle(smo)
    if smo:
        tk.LabelFrame(root, width=500, height=400, background="#596367").place(x=0, y=1030-400)
        icon = tk.PhotoImage(file="terminal.png")
        label = tk.Button(root, image=icon, command=lambda: os.system("python TERM.py"), border=None, borderwidth=0)
        label.image = icon  # Keep a reference to the image
        label.place(x=10, y=1030-380)
        ll = tk.Button(root, text="Terminal", background="#596367", foreground="white", command=lambda: os.system("python TERM.py"), border=None, borderwidth=0)
        ll.place(x=60, y=1030-375)
        icon = tk.PhotoImage(file="shutdown.png")
        label = tk.Button(root, image=icon, command=lambda: exit(), border=None, borderwidth=0)
        label.image = icon  # Keep a reference to the image
        label.place(x=460, y=990)
    else:
        desktop()
root.mainloop()