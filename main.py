import tkinter
from time import sleep
import pyautogui
from tkinter import *
from tkinter.ttk import *
import json
from pathlib import Path
import os
from os import path

data_direction = Path(path.expandvars(r"%APPDATA%\AmongUsHack\Data.json"))
data_direction2 = Path(path.expandvars(r"%APPDATA%\AmongUsHack"))

def hack():
    if Enable_Clicks_Value:
        pyautogui.click(1706, 66, duration = float(Click.get()))
        sleep(float(Time.get()))
        pyautogui.click(902, 836, duration = float(Click.get()))

    sleep(float(Time.get()))
    for i in range(int(Repe.get())):
        pyautogui.write(Text.get(1.0, END), Write.get() )
        sleep(float(Time.get()))
        pyautogui.press("enter")
        sleep(float(Time.get()))

def save_data():
    global data

    if not data_direction2.exists():
        os.mkdir(data_direction2)

    with open(data_direction, "w") as savefile:
        data = {
            "Text": Text.get(1.0, END),
            "Time_Sleep": Time.get(),
            "Repetitions": Repe.get(),
            "Write_Interval": Write.get(),
            "Click_Duration": Click.get(),
            "Enable_Click": Enable_Clicks_Value.get()
        }
        json.dump(data, savefile, indent=4, default=str)
    savefile.close()
    print("file are saved!!")

def load_data():
    global data
    
    if not data_direction.exists():
        save_data()
        return

    with open(data_direction, "r") as openfile:
        data = json.load(openfile)
        Text.delete('1.0', END)
        Time.delete(0, END)
        Repe.delete(0, END)
        Click.delete(0, END)
        Write.delete(0, END)
        Text.insert(END, data["Text"])
        Time.insert(END, data["Time_Sleep"])
        Repe.insert(END, data["Repetitions"])
        Click.insert(END, data["Click_Duration"])
        Write.insert(END, data["Write_Interval"])
        Enable_Clicks_Value.set(data["Enable_Click"])
    openfile.close()
    print("file are loaded!!")

def on_quit():
    save_data()
    root.destroy()

root = Tk()
root.geometry("400x400")
root.title("Among Us hack")
root.iconbitmap("x.ico")
root.protocol("WM_DELETE_WINDOW", on_quit)


Text = Text(width=20, height=10)
Text.pack()

time = Label(text="Time Sleep")
time.pack()

Time = Entry()
Time.pack()

repe = Label(text="Repetitions")
repe.pack()

Repe = Entry()
Repe.pack()

write = Label(text="Write Interval")
write.pack()

Write = Entry()
Write.pack()

click = Label(text="Click Duration")
click.pack()

Click = Entry()
Click.pack()

Enable_Clicks_Value = BooleanVar()
Enable_Clicks = Checkbutton(text="Enable Auto clicks", variable=Enable_Clicks_Value)
Enable_Clicks.pack()

Save = Button(text="Save", command=save_data)
Save.pack()

Load = Button(text="Load", command=load_data)
Load.pack()

Start = Button(text="Start", command=hack)
Start.pack()

load_data()

root.mainloop()