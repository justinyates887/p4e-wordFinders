from tkinter import *
from tkinter import filedialog

def init():
    file_opener()

base = Tk()
base.geometry('300x150')

def file_opener():
   try:
       fname = filedialog.askopenfilename(initialdir = "/", filetypes = (("Text Files" , "*.txt"), ("Markdown Files", "*.md")))
       print(fname)
       if fname is not None:
           fhand = open(fname.name)
           words(fhand)
   except:
        print('No file was selected, please try again...')

x = Button(base, text ='Please select a text file to open', command = lambda:file_opener())
x.pack()
base.mainloop()

def match(words, fhand):
    count = 0
    for word in words:
        for line in fhand:
            count += 1
            if any(word in line for word in words):
                print('Line ' + str(count) +': Text: ' + line.rstrip())

def words(fhand):
    words = []
    print('Please enter words or phrases you wish to search for. Once you are finished, type "STOP!"')
    word = input()
    while word not in ('STOP!'):
        words.append(word)
        word = input()
    match(words, fhand)

init()