import tkinter as tk
from tkinter import *
from tkinter import messagebox
import json
import time
from PIL import Image, ImageTk
from subprocess import call
import random
import itertools

break_flag = False
password_found = False
limit = False
max_length = 1

cracked = ""

var_dict = {}
v_dict = {}
num = {}

#! import settings
with open("settings.json", "r") as f:
    json_object = json.loads(f.read())
    length = json_object["length"]
    password = json_object["password"]
    visual_analysis = json_object["visual_analysis"]
    active_list = json_object["list"]
    method = json_object["method"]
    max_gen = int(json_object["max_gen"])

with open("lists.json", "r") as f:
    json_object = json.loads(f.read())
    list_data = json_object[active_list].split(",")

#! Update Dict
def update_dict():

    global cracked
    global var_dict
    global num

    for i in range(0, len(var_dict)):
       var_dict[i] = list_data[num[i]]

    for i in range(0, len(var_dict) ):
        cracked += var_dict[i]

    print(cracked)

#! Create dictionary
for x in range(length):  
    var_dict[x]="1"



#! handle visual feedback
if visual_analysis:

    analysis_window = tk.Tk()
    analysis_window.title("Visual Analysis")

st = time.time()
gen = 0

if method == "random":

    st = time.time()
    while password_found != True:
        if cracked == password:
            et = time.time()
            total_time = str(et-st)
            print("password found: " + cracked + "\nCracked in: " + total_time + "s\nFound after " + str(gen) + " generations")
            password_found = True
            break_flag = True

        if break_flag == True:
            break

        cracked = ""
                    
        for i in range(length):
            random_selection = random.randint(0, len(list_data)-1)
            var_dict[i] = list_data[random_selection]
                    
        for var in range(0,length):
            cracked += var_dict[var]

        gen += 1

        if gen == max_gen:
            limit = True
            break

et = time.time()

if limit:
    try:
        analysis_window.destroy()
    except:
        print("no window found")
        
    messagebox.showwarning(title= "Limit reached", message="Maximum amount of generations")
    

elif visual_analysis:

    Header_label = Label(analysis_window, text="Visual Analysis").grid(row=0, column=0, padx=20, pady=(0, 10), sticky="NEWS")

    password_info_label = Label(analysis_window, text=cracked).grid(row=1, column=1, sticky="w")
    password_length_info_label = Label(analysis_window, text=len(password)).grid(row=2, column=1, sticky="w")
    time_info_label = Label(analysis_window, text=str(et-st)).grid(row=3, column=1, sticky="w")
    generations_info_label = Label(analysis_window, text=gen).grid(row=4, column=1, sticky="w")

    password_label = Label(analysis_window, text="Password:").grid(row=1, column=0, sticky="w")
    password_length_label = Label(analysis_window, text="length").grid(row=2, column=0, sticky="w")
    time_label = Label(analysis_window, text="Time:").grid(row=3, column=0, sticky="w")
    generations_label = Label(analysis_window, text="genenerations:").grid(row=4, column=0, sticky="w")

try:
    analysis_window.mainloop()
except:
    pass
