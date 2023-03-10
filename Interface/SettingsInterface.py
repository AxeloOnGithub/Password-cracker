import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
from PIL import Image, ImageTk
from subprocess import call

window = Tk()
window.title("Settings")
window.resizable(False, False)

VAvar = BooleanVar()
CCvar = BooleanVar()
Lengthvar = IntVar()
Passwordvar = StringVar()
Methodvar = StringVar()


frame = Frame(window)
frame.pack(fill=X)

#! return to main
def return_main():
    window.destroy()
    call(["python", "interface/MainInterface.py"])
    

#!Load settings
with open("settings.json", "r") as f:
    json_object = json.loads(f.read())
    advanced = json_object["advanced_settings"]

#! advanced settings update
def advancedsettings(filename="settings.json"):
    with open(filename, "r") as info:
        data = json.load(info)

    if data["advanced_settings"] == False:
        data["advanced_settings"] = True
    else: 
        data["advanced_settings"] = False

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)

#! reset settings
def reset(filename="settings.json"):

    with open(filename, "r") as info:
        data = json.load(info)

    data["length"] = 4
    data["password"] = "1234"
    data["visual_analysis"] = True
    data["method"] = "bruteforce"
    data["max_gen"] = "5000000000"
    data["list"] = "list1"

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)


    tk.messagebox.showinfo(title= "Settings Reset!", message="Settings was Reset!")

#!Update Settings Function
def updatesettings(filename="settings.json"):

    global advanced

    #Erros
    if Passwordvar.get() == "":
            tk.messagebox.showwarning(title= "Error", message="You have not entered a password!")
            return

    if len(Passwordvar.get()) != Lengthvar.get():
        tk.messagebox.showwarning(title= "Error", message="Length slider and password length does not match!")
        return

    #Updating
    with open(filename, "r") as info:
        data = json.load(info)

    data["length"] = Lengthvar.get()
    data["password"] = Passwordvar.get()
    data["visual_analysis"] = VAvar.get()
    data["method"] = Methodvar.get().lower()
    data["max_gen"] = maxgen_spin.get()

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)


    tk.messagebox.showinfo(title= "Settings Updated", message="Settings was updated!")

#!Password Settings
password_info_frame = LabelFrame(frame, text="Password settings")
password_info_frame.grid(row= 0, column=0, padx=20, pady=10, sticky="ew")

password_label = Label(password_info_frame, text=f"Password: ")
password_label.grid(row=1, column=0)
password_entry = Entry(password_info_frame, textvariable=Passwordvar, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

#! Cracking methode
method_info_frame = LabelFrame(frame, text="Cracking method", width=100)
method_info_frame.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

options = ["Bruteforce","Random"]
Methodvar.set("Bruteforce")

method_optionmenu = OptionMenu(method_info_frame, Methodvar , *options )
method_optionmenu.grid(row=0,column=0)



#!Update Button
Updatebutton = Button(window, text="Update Settings", command=updatesettings).pack(side="top", fill="x")
Resetbutton = Button(window, text="Reset Settings", command=reset).pack(side="top", fill="x")
if not advanced:
    AdvancedButton = Button(window, text="Advanced Settings (Reload)", command=advancedsettings).pack(side="top", fill="x")

#! advanced settings
if advanced:

    #! Length slider
    lengthslider_label = Label(password_info_frame, text="Length:")
    lengthslider_label.grid(row=0, column=0)
    lengthslider = Scale(password_info_frame, from_=4, to=7, orient=HORIZONTAL, variable=Lengthvar)
    lengthslider.grid(row=0, column=1)

    #!Rendering Settings
    rendering_info_frame = LabelFrame(frame, text="Rendering settings", width=100)
    rendering_info_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

    max_width = max(rendering_info_frame.winfo_reqwidth(), password_info_frame.winfo_reqwidth())
    max_height = max(rendering_info_frame.winfo_reqheight(), password_info_frame.winfo_height())

    rendering_info_frame.config(width=max_width, height=max_height)
    password_info_frame.config(width=max_width, height=max_height)

    VAbutton = Checkbutton(rendering_info_frame, text="Visual Analysis Feedback", variable=VAvar, onvalue=True, offvalue=False)
    VAbutton.deselect()
    VAbutton.grid(row=0, column=0, sticky="W")

    #!spinbox
    maxgen_spin =Spinbox(method_info_frame, from_= 100000, to = 5000000000, increment=100000)
    maxgen_spin.grid(row=0,column=1)    

    #! normal settings
    NormalButton = Button(window, text="Normal Settings (Reload)", command=advancedsettings).pack(side="top", fill="x")


window.protocol("WM_DELETE_WINDOW", return_main)
window.mainloop()