import pyttsx3 as ts #import python text to speech module
import PyPDF2 as pdf #import pythn pdf reader module
import os

path = os.path.join("Desktop","Books","Do the Work.pdf")

open_pdf=open(path,'rb')

read_pdf=pdf.PdfFileReader(open_pdf)

#speak from page asssigned
speak=ts.init()
speak.setProperty("rate", 178)
#read first 10 pages
for start_read in range(10):
	starting_page=read_pdf.getPage(start_read)
	text=starting_page.extractText()
	speak.say(text)
	speak.runAndWait()
