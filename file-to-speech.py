from gtts import gTTS
import os

text=open('demo_mal.txt','r',encoding='utf-8').read()
output=gTTS(text=text,lang='ml',slow=False)
output.save('file-to-speech.mp3')
os.system('start file-to-speech.mp3')

