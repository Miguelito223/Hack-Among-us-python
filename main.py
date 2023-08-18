import tkinter
from time import sleep
import pyautogui
from tkinter import *

def lol():
    pyautogui.click(1706, 66, interval=float(text5.get(1.0, END)))
    sleep(float(text2.get(1.0, END)))
    pyautogui.click(902, 836, interval=float(text5.get(1.0, END)))

    sleep(float(text2.get(1.0, END)))

    for i in range(int(text3.get(1.0, END))):
        pyautogui.write(text.get(1.0, END), text4.get(1.0, END) )
        sleep(float(text2.get(1.0, END)))
        pyautogui.press("enter")
        sleep(float(text2.get(1.0, END)))

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Among Us hack")
ventana.iconbitmap("x.ico")


text = Text(width=20, height=10)
text.pack()

label = Label(text="Time Sleep")
label.pack()

text2 = Text(width=5, height=0)
text2.pack()

label2 = Label(text="Repetitions")
label2.pack()

text3 = Text(width=5, height=0)
text3.pack()

label3 = Label(text="Write Interval")
label3.pack()

text4 = Text(width=5, height=0)
text4.pack()

label4 = Label(text="Click Interval")
label4.pack()

text5 = Text(width=5, height=0)
text5.pack()



label3 = Label(text="Hack Here")
label3.pack()

button = Button(text="Press", command=lol)
button.pack()

ventana.mainloop()



while True:
    time.sleep(3)
    print(pyautogui.position())
