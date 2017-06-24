###lab6.py###
###Arpan Patel##


class ScoreError(Exception):
    pass 

class ScoreList(list):

    
    def __init__(self, lst = []):
        for item in lst:
            self.add(item)

    def __repr__(self):
        return 'ScoreList({})'.format(list.__repr__(self))

    def add(self, number):
        if number > 100 or number < 0:
            raise ScoreError('score {} not between 0 and 100'.format(number))
        else:
            self.append(number)

    def avg(self):
        return (sum(self)/len(self))

    def passing(ScoreList):
        if ScoreList.avg() > 60:
            return True
        else:
            return False
#TEST
'''
>>> #constructors
>>> t1 = Temperature()
>>> t1
Temperature(0.0,'C')
>>> t2 = Temperature(100,'f')
>>> t2
Temperature(100.0,'F')
>>> t3 = Temperature('12.5','c')
>>> t3
Temperature(12.5,'C')

>>> #convert
>>> t1.convert()
Temperature(32.0,'F')
>>> t4 = t1.convert()
>>> t4
Temperature(32.0,'F')

>>> #__str__
>>> print(t1)
0.0°C
>>> print(t2)
100.0°F

>>> #==
>>> t1 == t2
False
>>> t4 == t1
True

>>> #raised errors
>>> Temperature('apple','c')
Traceback (most recent call last):
…
ValueError: could not convert string to float: 'apple'
>>> Temperature(21.4,'t')
Traceback (most recent call last):
…
UnitError: Unrecognized temperature unit 't'
'''
  
from tkinter import*
from tkinter.messagebox import showinfo
from random import*

class Scrambler(Frame):

    #function#
    def __init__(self,word, parent=None):
        self.word = word
        scramble = list(word)
        shuffle(scramble)
        scramble = "".join(scramble)
        self.numberguesses = 3

        def click():
            if self.guess.get() == self.word:
                showinfo("Correct", 'You got it!')
            else:
                self.numberguesses -=1
                if self.numberguesses == 0:
                    showinfo('Lose', 'Sorry you lose')
                else:
                    showinfo('Wrong', 'you have ' + str(self.numberguesses)+ ' guesses left.')

        Frame.__init__(self,parent)

        # Label #
        labelWord = Label(self, text = scramble)
        labelWord.grid(row=0, column=2, columnspan=4)
       
        # data entry##
        self.guess = Entry(self)
        self.guess.grid(row=1, column=1, columnspan=6)


        # button #
        button = Button(self, text = 'Guess',command=click, width = 18)
        button.grid(row=2, column=1, columnspan=4)
    
        
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab6TEST.py'))
    
