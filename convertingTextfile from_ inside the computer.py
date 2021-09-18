from tkinter import*
from gtts import gTTS
import os
root=Tk()
root.title("Text to sound converter")
root.geometry("500x200")
root.iconbitmap("python_icon.ico")
def convert ():
    fh = open("Test.txt","r")#name of the txt file on your system
    myText =fh.read().replace("\n","")
    language ='en'
    output = gTTS(text=myText,lang = language,slow=True)
    output.save("convertedoutput1.mp3")#name of your Audio mp3 file after conversion
    fh.close()
    #os.system("startoutput.mp3")
convet_button=Button(root,text="Convert",font=("Helvetica",18),command=convert)
convet_button.pack(pady=20)
root.mainloop()