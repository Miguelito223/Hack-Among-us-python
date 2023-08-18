import tkinter
from time import sleep
import pyautogui
from tkinter import *

def lol():
    for i in range(20):
        pyautogui.click(1706,66)
        sleep(float(text2.get(1.0, END)))
        pyautogui.click(902,836)
        sleep(float(text2.get(1.0, END)))
        pyautogui.write(text.get(1.0, END))
        sleep(float(text2.get(1.0, END)))
        pyautogui.press("enter")
        sleep(float(text2.get(1.0, END)))

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Among Us hack")
ventana.iconbitmap("x.ico")


text = Text(width=20, height=10)
text.pack()

label = Label(text="Time")
label.pack()

text2 = Text(width=5, height=0)
text2.pack()

label2 = Label(text="Hack Here")
label2.pack()

button = Button(text="Press", command=lol)
button.pack()

ventana.mainloop()



while True:
    time.sleep(3)
    print(pyautogui.position())
