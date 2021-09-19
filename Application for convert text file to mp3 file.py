from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
import pyttsx3

root=Tk()
root.title("Text to Voice App")
root.geometry('275x260')
root.resizable(0,0)
root.configure(bg='yellow')
# create function for text to speech
def speak():
    engine=pyttsx3.init()
    audio_string=text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate',125)# Speech speed
        voices=engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)# female voice
        #engine.setProperty('voice', voices[0].id)# male voice
        engine.say(audio_string)
        engine.runAndWait()
        engine.stop()
# function for save text to mp3 audio
def save():
    engine=pyttsx3.init()
    audio_string=text.get('0.0',END)
    if audio_string:
        engine.setProperty('rate', 125)  # Speech speed
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # female voice
        # engine.setProperty('voice', voices[0].id)# male voice
        engine.save_to_file(audio_string,'sound.mp3')# Converted audio file name
        engine.runAndWait()
        engine.stop()
        #showinfo('Text File Converted and saved')#pop up message box to show file saved
        l1=Label(root,fg='red',font=("arial",12),text="File Converted and Saved")
        l1.grid(row=2,columnspan=3,pady=4)
text=ScrolledText(root,bg="yellow",width=30,height=10,wrap=WORD,padx=10,pady=10,bd=5,relief=RIDGE)
text.grid(row=0,columnspan=3)
#button for listen the text you entered on the scrolltext area
ttk.Button(root,text='Listen',width=7,command=speak).grid(row=1,column=0,ipadx=2)
#button for Clear the text you entered on the scrolltext area
ttk.Button(root,text='Clear',width=7,command=lambda :text.delete('0.0',END)).grid(row=1,column=1,ipadx=2)
#button for Convert the text to mp3 and Save
ttk.Button(root,text='Save',width=7,command=save).grid(row=1,column=2,ipadx=2)
root.mainloop()
