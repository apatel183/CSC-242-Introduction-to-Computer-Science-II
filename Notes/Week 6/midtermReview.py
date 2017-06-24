# midtermReview.py

'''
midterm in class this Thursday 2/11
usual class time
exam on computer, will provide doctest
BE ON TIME
Notes: you are allowed 2 double sided
or 4 single sided pages of notes
    print BEFORE you get here
    will be collected
use your time well
'''

##### Chapter 7 - namespaces #####

'''
vars() - returns namespace, a dictionary

object attributes:

obj.attr
self.q -   a list, #1
lst.append( 4 )   #2 
hangman("apple").pack()   #3

.attr is looked up in namespace of
1) object,  .q is namespace of self
2) class,   .append is a method in list class
3) super/parent class - i.e., pack is a method of Frame
   and hangman inherits from Frame

'''

##### Chapter 8 - OO programming #####

'''

class MyClass():

    def __init__(self,....):
       # create and assign data attributes
       # likely to see constructor calls
       self.x = ...
       self.y = list( iterable )

    def set(self,...):
       self.x  = ....

    def get(self,...):
       return self.x

    def __repr__(self):
       return "MyClass({})".format(...self.x )

    # m1 == m2
    def __eq__(self,other):
       return .... boolean expression ....

    other operators:
       x+y  -> MyClass.__add__(x,y)
       x>y  -> MyClass.__gt__(x,y)
       item in m -> MyClass.__contains__(m,item)

       may get operators for free

Container classes:   Queue based on list

    # v1 - composition, HAS A list
    class Queue():

       def __init__(self,iterable=[]):
          self.q = list(iterable)

       def enqueue(self,item):
          self.q.append(item)

    #v2 - inheritance, IS A list
    class Queue(list):

        # inherit __init__
        # self is a list

        def enqueue(self,item):
            self.append(item)

        def __repr__(self):
            return "Queue({})".format( list.__repr__(self) )

q = Queue([1,2,3])
print(q[1]) # Queue.__getitem__(q,1)
q[1]=7 # Queue.__setitem__(q,1,7)

class SubClass(SuperClass):

when inheriting: methods can be
1) inherited - method in SuperClass
2) extended - user SuperClass method in overridden method
3) overriden
4) added - new method in SuperClass

# easiest to inherit are Exceptions
class MyError(Exception):
   pass
# somewhere you can do this
raise MyError('optional message')

will be caught by this type of code:

try:
   code which may cause errors
except MyError:
   deal with it, whatever is appropriate
except ValueError:
   deal with that type of error
except NameError:
   ...
except:
   ...

'''

##### Chapter 9 #####

'''
remember imports:

from tkinter import *
from tkinter.messagebox import showinfo

widgets:
    Tk
    Frame
    Label
    Entry
       .get()
       .insert()
       .delete()
    Button
        command = cmd
    showinfo

layouts:
    pack
    grid, use columnspan

'''

##### hangman #####

'''
>>> hangman("APPLE").pack()
>>>
>>> # or
>>> root = Tk()
>>> hangman("APPLE",root).pack()

'''

class hangman(Frame):

    def __init__(self,word,parent=None):

        self.word = word.upper() # remember the word!!!!

        # main, responsibility is to build interface
        Label().grid(...)

        # must use multiple steps for entries
        self.entryWord = Entry(...)
        self.entryWord.grid(...)
        self.entryWord.insert(  mask(self.word,'') )

        btns = "ABCDE..."
        for i in range ... :
            def cmd(key=btn[i]):
                self.click(key)
            Button(   ,command=cmd).grid()

    def click(self,key):

        # if key is already there (either right or wrong)
        # do nothing

        # if in the word,
        # add to the list rights
        # remask the word using right
        # and, rewrite the the masked word and the rights
        # check whete you won

        # not in the word
        # add to the wrong list
        # check whether you lost
        

        
        


            
          
       

       
       





















































