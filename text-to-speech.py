# 1) Generating audio from text data
# 2) Generating audio from file
# 3) Generating audio from input
#### gtts library
# pip install gtts on cmd prompt

from gtts import gTTS
import os

text="Hi, Good morning"
output=gTTS(text=text,lang='en',slow=False)
output.save('test.mp3')
os.system('start test.mp3')

# for mac 'afplay'




