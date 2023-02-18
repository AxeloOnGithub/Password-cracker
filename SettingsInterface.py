import tkinter as tk
from tkinter import *
import json

window = Tk()
window.title("Settings")

VFvar = BooleanVar()
VAvar = BooleanVar()
Lengthvar = IntVar()
Passwordvar = StringVar()

frame = Frame(window)
frame.pack()

#Password Settings
password_info_frame = LabelFrame(frame, text="Password settings")
password_info_frame.grid(row= 0, column=0, padx=20, pady=10)

lengthslider_label = Label(password_info_frame, text="Length:")
lengthslider_label.grid(row=0, column=0)
lengthslider = Scale(password_info_frame, from_=4, to=7, orient=HORIZONTAL, variable=Lengthvar)
lengthslider.grid(row=0, column=1)

password_label = Label(password_info_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = Entry(password_info_frame, textvariable=Passwordvar, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

#Rendering Settings
rendering_info_frame = LabelFrame(frame, text="Rendering settings")
rendering_info_frame.grid(row=0, column=0, padx=20, pady=10)

VFbutton = Checkbutton(rendering_info_frame, text="Visual Feedback", variable=VFvar, onvalue=True, offvalue=False)
VFbutton.deselect()
lengthslider.grid(row=0, column=0)

VAbutton = Checkbutton(rendering_info_frame, text="Visual Analysis Feedback", variable=VAvar, onvalue=True, offvalue=False)
VAbutton.deselect()
lengthslider.grid(row=0, column=0)

window.mainloop()