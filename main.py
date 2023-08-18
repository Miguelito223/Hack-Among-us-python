import tkinter
from time import sleep
import pyautogui
from tkinter import *

def lol():
    for i in range(20):
        pyautogui.click(1706,66)
        sleep(0.5)
        pyautogui.click(902,836)
        sleep(0.5)
        pyautogui.write(text.get(1.0, END))
        sleep(0.5)
        pyautogui.press("enter")
        sleep(0.5)

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Among Us hack")
ventana.iconbitmap("descarga.ico")


text = Text(width=20, height=10)
text.pack()

label = Label(text="Hack Here")
label.pack()

button = Button(text="Press", command=lol)
button.pack()

ventana.mainloop()



while True:
    time.sleep(3)
    print(pyautogui.position())
