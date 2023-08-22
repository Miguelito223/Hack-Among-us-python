import tkinter
from time import sleep
import pyautogui
from tkinter import *
import json
from pathlib import Path
import os
from os import path

data = {
    "Text":"Put Text Here", 
    "Time_Sleep":0, 
    "Repetitions":0, 
    "Write_Interval":0, 
    "Click_Duration":0
}

data_direction = Path(path.expandvars(r"%APPDATA%\AmongUsHack\Data.json"))
data_direction2 = Path(path.expandvars(r"%APPDATA%\AmongUsHack"))

def hack():
    pyautogui.click(1706, 66, duration = float(text5.get(1.0, END)))
    sleep(float(text2.get(1.0, END)))
    pyautogui.click(902, 836, duration = float(text5.get(1.0, END)))

    sleep(float(text2.get(1.0, END)))

    for i in range(int(text3.get(1.0, END))):
        pyautogui.write(text.get(1.0, END), text4.get(1.0, END) )
        sleep(float(text2.get(1.0, END)))
        pyautogui.press("enter")
        sleep(float(text2.get(1.0, END)))

def save_data():
    global data

    if not data_direction2.exists():
        os.mkdir(data_direction2)

    with open(data_direction, "w") as savefile:
        data["Text"] = text.get(1.0,END)
        data["Time_Sleep"] = text2.get(1.0,END)
        data["Repetitions"] = text3.get(1.0,END)
        data["Write_Interval"] = text4.get(1.0,END)
        data["Click_Duration"] = text5.get(1.0,END)
        json.dump(data, savefile, indent=4)
    savefile.close()
    print("file are saved!!")

def load_data():
    global data

    if not data_direction.exists():
        save_data()
        return

    with open(data_direction, "r") as openfile:
        data = json.load(openfile)
    openfile.close()
    print("file are loaded!!")

load_data()

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Among Us hack")
ventana.iconbitmap("x.ico")

text = Text(width=20, height=10)
text.insert(END, data["Text"])
text.pack()

label = Label(text="Time Sleep")
label.pack()

text2 = Text(width=5, height=0)
text2.insert(END, data["Time_Sleep"])
text2.pack()

label2 = Label(text="Repetitions")
label2.pack()

text3 = Text(width=5, height=0)
text3.insert(END, data["Repetitions"])
text3.pack()

label3 = Label(text="Write Interval")
label3.pack()

text4 = Text(width=5, height=0)
text4.insert(END, data["Write_Interval"])
text4.pack()

label4 = Label(text="Click Duration")
label4.pack()

text5 = Text(width=5, height=0)
text5.insert(END, data["Click_Duration"])
text5.pack()

button = Button(text="Save", command=save_data)
button.pack()

button2 = Button(text="Load", command=load_data)
button2.pack()

button3 = Button(text="Start", command=hack)
button3.pack()

ventana.mainloop()