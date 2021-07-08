from gtts import gTTS
import os
fh = open("Test.txt","r")#file name of the text in your system
myText =fh.read().replace("\n","")
language ='en'
output = gTTS(text=myText,lang = language,slow=False)
output.save("convertedoutput.mp3")# file name of your mp3 audiofile after conversion.
fh.close()
os.system("startoutput.mp3")
