import pyttsx3
import PyPDF2
book = open('multimedia_systems.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# print(pages)
person = pyttsx3.init()
# person.say('Welcome to our project presentation')
# page = pdfReader.getPage(5)
# text = page.extractText()
# person.say(text)
# person.runAndWait()
for num in range(6, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    person.say(text)
    person.runAndWait()