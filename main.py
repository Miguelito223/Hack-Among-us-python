import tkinter
from time import sleep
import pyautogui
from tkinter import *
from tkinter.filedialog import askopenfile
import json

data = {
    "Text":"", 
    "Time_Sleep":0, 
    "Repetitions":0, 
    "Write_Interval":0, 
    "Click_Duration":0

}
data_direction = "lol.json"

def lol():
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
    with open(data_direction, "w") as savefile:
        json.dumps(data, savefile)

def load_data():
    with open(data_direction, "r") as openfile:
        data = json.load(openfile)
load_data()

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Among Us hack")
ventana.iconbitmap("x.ico")


text = Text(width=20, height=10)
text.insert(END, data.get(0))
text.pack()

label = Label(text="Time Sleep")
label.pack()

text2 = Text(width=5, height=0)
text2.insert(END, data.get(1))
text2.pack()

label2 = Label(text="Repetitions")
label2.pack()

text3 = Text(width=5, height=0)
text3.insert(END, data.get(2))
text3.pack()

label3 = Label(text="Write Interval")
label3.pack()

text4 = Text(width=5, height=0)
text4.insert(END, data.get(3))
text4.pack()

label4 = Label(text="Click Duration")
label4.pack()

text5 = Text(width=5, height=0)
text5.insert(END, data.get(4))
text5.pack()

button = Button(text="Save", command=save_data)
button.pack()

button = Button(text="Start", command=lol)
button.pack()

ventana.mainloop()

while True:
    sleep(3)
    print(pyautogui.position())
