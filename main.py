import tkinter
from time import sleep
import pyautogui
from tkinter import *
from tkinter.filedialog import askopenfile
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
    if not data_direction.exists():
        os.mkdir(data_direction2)
    
    with open(data_direction, "w") as savefile:
        json.dump(data, savefile)

def load_data():
    if not data_direction.exists():
        save_data()
    
    with open(data_direction, "r") as openfile:
        data = json.load(openfile)


load_data()

Text_value = data["Text"]
Time_Sleep_value = data["Time_Sleep"]
Repetitions_value = data["Repetitions"]
Write_Interval_value = data["Write_Interval"]
Click_Duration_value = data["Click_Duration"]

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Among Us hack")
ventana.iconbitmap("x.ico")


text = Text(width=20, height=10)
text.insert(END, Text_value)
text.pack()

label = Label(text="Time Sleep")
label.pack()

text2 = Text(width=5, height=0)
text2.insert(END, Time_Sleep_value)
text2.pack()

label2 = Label(text="Repetitions")
label2.pack()

text3 = Text(width=5, height=0)
text3.insert(END, Repetitions_value)
text3.pack()

label3 = Label(text="Write Interval")
label3.pack()

text4 = Text(width=5, height=0)
text4.insert(END, Write_Interval_value)
text4.pack()

label4 = Label(text="Click Duration")
label4.pack()

text5 = Text(width=5, height=0)
text5.insert(END, Click_Duration_value)
text5.pack()

button = Button(text="Save", command=save_data)
button.pack()

button = Button(text="Start", command=hack)
button.pack()

ventana.mainloop()

while True:
    sleep(3)
    print(pyautogui.position())
