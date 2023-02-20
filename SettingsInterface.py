import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json

window = Tk()
window.title("Settings")
window.resizable(False, False)

VFvar = BooleanVar()
VAvar = BooleanVar()
CCvar = BooleanVar()
Lengthvar = IntVar()
Passwordvar = StringVar()

frame = Frame(window)
frame.pack(fill=X)


#!Update Settings Function
def update(filename="settings.json"):

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
    data["visual_feedback"] = VFvar.get()
    data["visual_analysis"] = VAvar.get()

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)


    tk.messagebox.showinfo(title= "Settings Updated", message="Settings was updated!")

#!Password Settings
password_info_frame = LabelFrame(frame, text="Password settings")
password_info_frame.grid(row= 0, column=0, padx=20, pady=10, sticky="ew")

lengthslider_label = Label(password_info_frame, text="Length:")
lengthslider_label.grid(row=0, column=0)
lengthslider = Scale(password_info_frame, from_=4, to=7, orient=HORIZONTAL, variable=Lengthvar)
lengthslider.grid(row=0, column=1)

password_label = Label(password_info_frame, text=f"Password: ")
password_label.grid(row=1, column=0)
password_entry = Entry(password_info_frame, textvariable=Passwordvar, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

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

VFbutton = Checkbutton(rendering_info_frame, text="Visual Feedback (Very slow!)", variable=VFvar, onvalue=True, offvalue=False)
VFbutton.deselect()
VFbutton.grid(row=1, column=0, sticky="W")

#!Update Button
Updatebutton = Button(window, text="Update Settings", command=update).pack(pady=(0,10))


window.mainloop()