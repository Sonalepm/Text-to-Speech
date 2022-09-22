from gtts import gTTS
import os
from tkinter import *

root = Tk()


def convert():
    text = entry.get()
    output = gTTS(text=text, lang='en')
    output.save('input-speech.mp3')
    os.system('start input-speech.mp3')

canvas = Canvas(root, width=500, height=300)
canvas.pack()
entry = Entry(root)
canvas.create_window(200, 150, window=entry)
button = Button(text="Enter", command=convert)
canvas.create_window(300, 150, window=button)

root.mainloop()
