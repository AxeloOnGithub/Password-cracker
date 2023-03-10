import itertools
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time


#! Load Settings
with open("settings.json", "r") as f:
    json_object = json.loads(f.read())
    password = json_object["password"]
    visual_analysis = json_object["visual_analysis"]
    active_list = json_object["list"]
    method = json_object["method"]
    max_gen = int(json_object["max_gen"])

with open("lists.json", "r") as f:
    json_object = json.loads(f.read())
    list_data = json_object[active_list].split(",")

#! handle visual Analysis
if visual_analysis:

    analysis_window = tk.Tk()
    analysis_window.title("Visual Analysis")

#!variables
charset = list_data  
cracked = ""
max_length = 1
limit = False
gen = 0


def crack():

    break_flag = False

    global password
    global max_length
    global gen

    combinations = itertools.product(charset, repeat=max_length)

    for combination in combinations:
        cracked = ''.join(combination)
         
        gen += 1

        if cracked == password:
            break_flag = True
            break
    
    if break_flag == True:
        return
    else:
        max_length += 1
        crack()

st = time.time()

crack()

et = time.time()

if limit:
    try:
        analysis_window.destroy()
    except:
        print("no window found")
        
    messagebox.showwarning(title= "Limit reached", message="Maximum amount of generations")
    

elif visual_analysis:

    Header_label = Label(analysis_window, text="Visual Analysis").grid(row=0, column=0, padx=20, pady=(0, 10), sticky="NEWS")

    password_info_label = Label(analysis_window, text=password).grid(row=1, column=1, sticky="w")
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
