# PyPDF2 version: 3.0.1

import PyPDF2 as ppdf
from TTS.api import TTS 
'''
def get_text_from_pdf(path):
    #open file
    file = open(f"{path}", "rb", )
    read = ppdf.PdfReader(file)

    #write text
    text = []
    for i in range(len(read.pages)):
        text.append(read.pages[i].extract_text())
    return text '''

# initialize Text-To-Speech (TTS)
tts = TTS(TTS.list_models()[0])

# run tts
sound = tts.TTS("Testing!!", speaker= tts.speakers[0], language= tts.languages[0])









# TESTS
path = "/home/vladk/Downloads/rin.pdf"
#print(get_text_from_pdf(path))






