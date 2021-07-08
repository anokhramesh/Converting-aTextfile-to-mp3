from gtts import gTTS
import os
fh = open("Test.txt","r")#using file handler function to open a text file name Test.txt in your system.
myText =fh.read().replace("\n","")# function to read the file
language ='en'# language selection 
output = gTTS(text=myText,lang = language,slow=False) # format of the output file
output.save("convertedoutput.mp3")# file name of your mp3 audiofile after conversion.
fh.close()
os.system("startoutput.mp3")
