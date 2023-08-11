# PyPDF2 version: 3.0.1

import PyPDF2 as ppdf
from gtts import gTTS
import os


def get_text_from_pdf(path):
    #open file
    file = open(rf"{path}", "rb", )
    read = ppdf.PdfReader(file)

    #write text
    text = []
    for i in range(len(read.pages)):
        text.append(read.pages[i].extract_text())
    return text
    
def voice_text(text):
    voiced_text = gTTS(text[0], lang='en', slow=False)
    
    voiced_file = 'voiced_text.mp3'
    voiced_text.save(voiced_file)

    os.system(f'start {voiced_file}')
    
def pdf_read_aloud():
    print("Hello! This program wiil read your pdf-file aloud.")
    path = input("Please, provide a path to your file here: ")
    text = get_text_from_pdf(path)
    print("Your results are here!")
    voice_text(text)








<<<<<<< HEAD
=======

>>>>>>> 48999e5 (read aloud for 1 page)
