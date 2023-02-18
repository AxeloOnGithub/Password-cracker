import tkinter as tk
from tkinter import *
import json
from subprocess import call
from test import *

root = tk.Tk()

#settings
VFvar = BooleanVar()
VAvar = BooleanVar()
Lengthvar = IntVar()
Passwordvar = StringVar()

def update(filename="settings.json"):
    with open(filename, "r") as info:
        data = json.load(info)

    data["length"] = Lengthvar.get()
    data["password"] = Passwordvar.get()
    data["visual_feedback"] = VFvar.get()
    data["visual_analysis"] = VAvar.get()

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)

def launch():
    LoadingLabel = Label(root, text="Craking Password...").pack()
    time.sleep(0.5)
    crack()

root.geometry("300x300")
root.title("Test GUI")
root.config(bg="#575757")

window = Tk()
window.title("Data Entry Form")

frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)


LenghtLabel = Label(root, text="Password lenght:", bg="#575757").pack()
LenghtSlider = Scale(root, from_=4, to=7, orient=HORIZONTAL, variable=Lengthvar, bg="#575757").pack()

PasswordLabel = Label(root, text="Password:", bg="#575757").pack()
PasswordField = Entry(root, textvariable=Passwordvar, show="*").pack()

Checkboxheader = Label(root, text="Hello World!", font=("Arial", 15), bg="grey", width=100).pack()
VFbutton = Checkbutton(root, text="Visual Feedback", variable=VFvar, onvalue=True, offvalue=False)
VFbutton.deselect()
VFbutton.pack()

VAbutton = Checkbutton(root, text="Visual Analysis", variable=VAvar, onvalue=True, offvalue=False)
VAbutton.deselect()
VAbutton.pack()

Updatebutton = Button(root, text="Update Settings", command=update).pack()
Launchbutton = Button(root, text="Crack Password", command=launch).pack()


root.mainloop()
