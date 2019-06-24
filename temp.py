import datetime

print("enter time to wake u up ! in %H:%M:%S in 24 hours format")
while(1):
    s=input()
    l=s.split(":")
    if( int(l[0]) >23 or ((int(l[1]) or int(l[2]))>59 )):
        print("please dont test me ! \n Enter valid time")
    else:
        break


from gtts import gTTS 
import os 
mytext = 'Hello your alarm is set \n Please Wake up quickly !!'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("alarm1.mp3")

while(1):
    if(datetime.datetime.now().strftime("%H:%M:%S") == s):
         os.system("alarm1.mp3")
         break
 
            
        

        
