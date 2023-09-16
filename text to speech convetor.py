from tkinter import *
from gtts import gTTS
import os
root = Tk()
def play():
    language = "en"
    convert = gTTS(text = entry.get(),
                   lang = language,
                   slow = False)
    convert.save("convert.wav")
    os.system("convert.wav")
ibl = Label(text = "Text to speech Convertor",
                   font = "Boulder,30",
                   bg = "red")
ibl.grid(row = 1,
        column = 1)
entry = Entry(width = 45,
              bd = 4,
              font = 14)
entry.grid(row = 3,
           column = 1)
btn = Button(text = "CONVERT",
             width = "15",
             pady = 10,
             font = "Arial,15",
             command = play,
             bg = "yellow")
btn.grid(row = 4,
         column = 1)
root.title("Text to Speech Convertor")
root.geometry("500x200")
root.mainloop()

    
