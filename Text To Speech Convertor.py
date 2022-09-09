
""" Text To Speech Convertor App Using Python GUI Tkinter """ 

import tkinter as tk 
from tkinter import *
import pyttsx3

# Button Speak Function that convert text to speech 

engine = pyttsx3.init()

def Speak():
    
    engine.say(text_variable.get())
    engine.runAndWait()
    engine.stop()

root = Tk()

text_variable = StringVar()

label_frame = LabelFrame(root , text="Text To Speech" , font=("Raleway",10) , bd = 2 , bg = "#ccddff")
label_frame.pack(fill = "both", expand = "yes", padx = 10 , pady = 10)

label = Label(label_frame , text = "Text" , font = ("Raleway",10) , bg = "black" , fg = "white")
label.pack(side = tk.LEFT , padx = 5)

text_entry = Entry(label_frame , textvariable = text_variable , font = ("Raleway",10) , width = 25 , bd = 5)
text_entry.pack(side = tk.LEFT , padx = 10)

button = Button(label_frame , text = " Speak " , font = ("Raleway",10) , bg = "#20bebe" , fg = "white" , command = Speak)
button.pack(side = tk.LEFT , padx = 10)


root.title("Text To Speech Convertor")
root.geometry("350x150")
root.config(bg= "#ccddff")
root.resizable(False,False)

root.mainloop()