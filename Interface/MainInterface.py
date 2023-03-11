import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
from subprocess import call

with open("settings.json", "r") as f:
        json_object = json.loads(f.read())
        method = json_object["method"]


window = Tk()
window.title("Main Menu")
window.geometry("300x117")
window.resizable(False, False)

#! Anchor button functions
def settings():
    window.destroy()
    call(["python", "interface/SettingsInterface.py"])
def list():
    window.destroy()
    call(["python", "interface/ListInterface.py"])
def run():
    window.destroy()
    if method == "bruteforce":
        call(["python", "bruteforce_method.py"])
    elif method == "random":
        call(["python", "random_method.py"])

#! Anchor buttons

settings_button = Button(text="Settings", command=settings, width=10)
settings_button.grid(sticky="W", row=0, column=0, padx=(20,0), pady=(20,0))
list_button = Button(text="List Settings", command=list, width=10)
list_button.grid(sticky="W", row=1, column=0, padx=(20,0))
run_button = Button(text="Crack!", command=run, width=10)
run_button.grid(sticky="W", row=2, column=0, padx=(20,0))

title_label = Label(text="PASSWORD CRACKER", font=("times", 12, "bold"))
title_label.grid(sticky="W", row=1, column=1, padx=16)

window.mainloop()