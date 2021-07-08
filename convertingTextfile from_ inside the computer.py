from gtts import gTTS
import os
fh = open("Test.txt","r")
myText =fh.read().replace("\n","")
language ='en'
output = gTTS(text=myText,lang = language,slow=False)
output.save("convertedoutput.mp3")
fh.close()
os.system("startoutput.mp3")
