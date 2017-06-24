# guis.py

# midterm next Thurs
# guis/tkinter will be on the midterm

##### GUIs/tkinter #####

'''
GUI - graphical user interface, allows user
      to interact with a program, using mouse,
      screen, other graphical elements

API - application programming interface
      (programming environment, library of classes
      functions, methods)

tkinter is a Python GUI API - includes many "widgets"
      (buttons, frames, labels, windows ... )
      but you can customize to create your own

will be using inheritance

tkinter widgets:

    first argument is always the parent object
    dont forget about this

    Frame - non-root window, customizable
       good for subclassing to create widgets

    Label - displays text

    Button - what it sounds like
       text =
       command = eventhandler, will run eventhandler
                 when button is clicked (no arguments)
       bind() - we dont use this, but, you can also
                bind eventhandlers (code that executes
                when specified events occur)

    Entry - text box user can type in
       get() - method retrieves text currently in Entry
       insert(END,stuff) - will append to the Entry box
       delete(0,END) - deletes everything

widget layout - there are two basic ways to layout widgets.
   dont mix up these methods within a particular container
   
   pack() - pack it in, not a lot of control

   grid(row= number, column = number, columnspan = number)
      row, column are 0 based positions
      columnspan optional (defaults to 1) and specifies
         how many columns (cells) wide you want the cell
         to be
      rowspan ? - should similar

dialogs - separate windows that can be displayed

    showinfo - displays a message

'''

##### import reminder #####
'''
>>> import math
>>> math.pi
3.141592653589793
>>> 'math' in vars()
True
>>> math.cos
<built-in function cos>
>>> 
>>> from math import *
>>> 'pi' in vars()
True
>>> pi
3.141592653589793
>>> 'cos' in vars()
True
>>> cos
<built-in function cos>
>>> 
'''

##### tkinter #####

'''
>>> # tkinter
>>> from tkinter import Tk, Label
>>> root = Tk()
>>> hello = Label(master=root,text='hello, world!')
>>> # didnt appear, not on stage yet
>>> # make it visible
>>> hello.pack()
>>> hello2 = Label(root,text='another label')
>>> hello2.pack()
>>> hello2.pack()
>>> # many times, Labels dont need var names
>>> # if text will be static
>>> Label(root, 'even more text').pack()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    Label(root, 'even more text').pack()
  File "C:\Python\lib\tkinter\__init__.py", line 2604, in __init__
    Widget.__init__(self, master, 'label', cnf, kw)
  File "C:\Python\lib\tkinter\__init__.py", line 2118, in __init__
    classes = [(k, v) for k, v in cnf.items() if isinstance(k, type)]
AttributeError: 'str' object has no attribute 'items'
>>> Label(root, text='even more text').pack()
>>> # you are always supposed to do this
>>> root.mainloop()  # makes root block
>>> 

'''


##### pigLatin translator #####

from tkinter import *
from pigLatin import *
from tkinter.messagebox import showinfo


# ok, but not usable as a widget
def pigLatinTranslator():

    # event handler
    def onClickTranslate():
        print( 'clicked')
        # retrive input, translate and report results
        showinfo('Pig Latin', 'Pig Latin Translation: '+pigLatin(enter.get()) )
    

    # make the interface
    root = Tk()
    root.title('Pig Latin Translator')
    Label(root,text="Please enter a phrase in English").pack()
    enter = Entry(root)  #named, so can get text later
    enter.pack()
    # Button(root,text='click to translate').pack()   - no event handler
    # add an event handler to button, will run when button is clicked
    Button(root,text='click to translate',command=onClickTranslate).pack()


# should do more interesting grid layout

   
# pigLatinTranslator()

    





























      
