import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import json
from PIL import Image, ImageTk

has_run = False

#!Update Settings Function
def update(filename="settings.json"):

    #Updating
    with open(filename, "r") as info:
        data = json.load(info)

        active_list = ""

    count = int(L1var.get()) + int(L2var.get()) + int(L3var.get()) + int(L4var.get()) + int(CLvar.get())

    if count == 1:
        if L1var.get():
            active_list = "List1"
        elif L2var.get():
            active_list = "List2"
        elif L3var.get():
            active_list = "List3"
        elif L4var.get():
            active_list = "List4"
        elif CLvar.get():
            active_list = "customlist"

            with open("lists.json", "r") as info:
                custom_data = json.load(info)

            custom_data["customlist"] = customlistbox.get(1.0, END).replace('"', '').replace("[", "").replace("]", "").replace(",", "").replace(" ",",").strip()

            with open("lists.json", "w") as f:
                json.dump(custom_data, f, indent=1)


    else:
        messagebox.showwarning(title="Error", message="You have selected more / less than one list!")
        return
    
    data["list"] = active_list

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)


    tk.messagebox.showinfo(title= "Settings Updated", message="Settings was updated!")

window = Tk()
window.title("Lists")
window.resizable(False, False)
window.geometry("1795x400")

L1var = BooleanVar()
L2var = BooleanVar()
L3var = BooleanVar()
L4var = BooleanVar()
CLvar = BooleanVar()

#! TETS

frame = Frame(window)
frame.pack(fill=X)

button_frame = Frame(window)
button_frame.pack(fill=X)

#!Standart lists
buildin_lists_frame = LabelFrame(frame, text="Build-In Lists")
buildin_lists_frame.grid(row= 0, column=0, padx=20, pady=(10,0), sticky="ew")

list1selector = Checkbutton(buildin_lists_frame, onvalue=True, offvalue=False, variable=L1var)
list1selector.deselect()
list1selector.grid(row=0, column=0, sticky="W")
list1box = Text(buildin_lists_frame, width=228, height=1, font=("arial",9))
list1box.insert(END, '["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", "^", "_", "`", "!", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]')
list1box.grid(row=0, column=1, sticky="W", padx=(0,5))

list2selector = Checkbutton(buildin_lists_frame, onvalue=True, offvalue=False, variable=L2var)
list2selector.deselect()
list2selector.grid(row=1, column=0, sticky="W")
list2box = Text(buildin_lists_frame, width=228, height=1, font=("arial",9))
list2box.insert(END, '["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]')
list2box.grid(row=1, column=1, sticky="W", padx=(0,5))

list3selector = Checkbutton(buildin_lists_frame, onvalue=True, offvalue=False, variable=L3var)
list3selector.deselect()
list3selector.grid(row=2, column=0, sticky="W")
list3box = Text(buildin_lists_frame, width=228, height=1, font=("arial",9))
list3box.insert(END, '["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]')
list3box.grid(row=2, column=1, sticky="W", padx=(0,5))

list4selector = Checkbutton(buildin_lists_frame, onvalue=True, offvalue=False, variable=L4var)
list4selector.deselect()
list4selector.grid(row=3, column=0, sticky="W")
list4box = Text(buildin_lists_frame, width=228, height=1, font=("arial",9))
list4box.insert(END, '["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]')
list4box.grid(row=3, column=1, sticky="W", padx=(0,5))

#! Custom Lists
custom_lists_frame = LabelFrame(frame, text="Custom Lists")
custom_lists_frame.grid(row= 1, column=0, padx=20, pady=10, sticky="ew")

customlistbox = Text(custom_lists_frame, height=1, width=200)
customlistbox.grid(row=0,column=1)
customlistbox.grid_remove()

no_lists_label = Label(custom_lists_frame, text="You have no custom Lists")
no_lists_label.grid(row=0, column=0)

#! Upload File Function
def upload_file():
    
    global has_run

    #find the file
    f_types = [('.txt Files', '*.txt')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    text_file = open(filename, "r") 

    #process the data
    raw_data = text_file.read()
    datalist = raw_data.split(" ")
    print(datalist)
    datastring = "[{}]".format(", ".join(f'"{item}"' for item in datalist))
    print(datastring)

    #Create the box
    no_lists_label.destroy()

    customlistselector = Checkbutton(custom_lists_frame, onvalue=True, offvalue=False, variable=CLvar)
    customlistselector.deselect()
    customlistselector.grid(row=0, column=0, sticky="W")

    customlistbox.grid()

    #create save button
    savebutton = Button(custom_lists_frame, text="Save", command=save_file)
    savebutton.grid(row=0,column=2, padx=5, pady=(0,5))

    #output the data
    customlistbox.delete(1.0, END)
    customlistbox.insert(INSERT, datastring)
    text_file.close()

    has_run = True

#! save file function
def save_file():

    global customlistbox

    f_types = [('.txt Files', '*.txt')]
    file_name = filedialog.asksaveasfilename(filetypes=f_types, defaultextension=".txt", title="Save list", initialfile="customlist.txt")
    text_file = open(file_name, "w")
    processed_data = customlistbox.get(1.0, END).replace('"', '')
    print(processed_data)
    text_file.write(processed_data.replace("[", "").replace("]", "").replace(",", "").strip())
    print(processed_data)

#! create list function
def create_list():

    global has_run

    if has_run == True:
        messagebox.showwarning(title="Error", message="You have already created / uploaded a custom list!")
    else:
        no_lists_label.destroy()

        customlistselector = Checkbutton(custom_lists_frame, onvalue=True, offvalue=False, variable=CLvar)
        customlistselector.deselect()
        customlistselector.grid(row=0, column=0, sticky="W")

        customlistbox = Text(custom_lists_frame, height=1, width=200)
        customlistbox.grid(row=0,column=1)

        savebutton = Button(custom_lists_frame, text="Save", command=save_file)
        savebutton.grid(row=0,column=2, padx=5, pady=(0,5))

        has_run = True

#! Update List
importbutton = Button(button_frame, text="import List", command=upload_file)
importbutton.grid(row=0, column=0, padx=5)

createbutton = Button(button_frame, text="create List", command=create_list)
createbutton.grid(row=0, column=1, padx=5)

updatebutton = Button(button_frame, text="Update List Settings", command=update)
updatebutton.grid(row=0, column=2, padx=5)

window.mainloop()
