# Source - https://stackoverflow.com/a
# Posted by NPE
# Retrieved 2025-11-13, License - CC BY-SA 3.0

from tkinter import *
import tkinter as tk
import random

is_on = True # Define the Variable first before the Function. [UnboundLocalError]
punch = "" # variable storage

def get_joke():

    global is_on
    global punch # keep the value before heading for the next joke

    if is_on: # Find a joke and display it

        line = random.choice(open('_Resources/randomJokes.txt').readlines())
        joke, punch = line.split("?")[0], line.split("?")[1]

        tk_button.config(text="Punch!")
        joke_label.config(text=f"{joke}")
        punch_label.config(text=f"")
        is_on = False

        
        print (f"{joke}?")

    else: # Change to the next joke

        tk_button.config(text="Tell me another joke.")
        punch_label.config(text=f"{punch}")

        is_on = True

        print (punch)


# Main Window

root = tk.Tk()
root.title("Tell me a joke!")
root.geometry("500x200")

ohhi = tk.Label(root, text="The Jokenator 3000 Prototype")
ohhi.pack()

joke_label = tk.Label(root, text="",)
joke_label.pack()

punch_label = tk.Label(root, text="",)
punch_label.pack()

tk_button = tk.Button(root, text="Tell me a joke.", command=get_joke)
tk_button.pack(pady=5)

root.mainloop()