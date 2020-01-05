import pytesseract	 

# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
import pyttsx3		 

#translates into the mentioned language 
#from googletrans import Translator	 

# opening an image from the source path 
img = Image.open('1.png')	 

# describes image format in the output 
print(img)						 
# path where the tesseract module is installed 
result = pytesseract.image_to_string(img) 
# write text in a text file and save it to source path 
'''with open('abc.txt',mode ='w') as file:	 
	file.write(result) '''
print(result) 
				
p = Translator()					 
engine = pyttsx3.init() 

# an audio will be played which speaks the test if pyttsx3 recognizes it 
engine.say(result)							 
engine.runAndWait() 
