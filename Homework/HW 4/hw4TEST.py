
>>> from hw4 import *



>>> mask('APPLE','AE')
'A???E'
>>> mask('APPLE','')
'?????'
>>> mask('APPLE','PLEASE')
'APPLE'
>>>


>>> root = Tk()
>>> hangman("APPLE",root).pack()
>>> root.destroy()
>>> 
>>> 
>>> hangman("ORANGE").pack()
>>> 
