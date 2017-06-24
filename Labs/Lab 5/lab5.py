####lab5.py###
####Arpan Patel###



##Question1###

class UnitError(Exception):
    pass

class Temperature():
    def __init__(self,t=0.0, unit='C'):
        self.t = float(t)
        if unit.upper() not in ['C','F']:
            raise UnitError ("Unrecognized temperature unit '{}'".format(unit))
        else:
            self.unit = unit.upper()

    def __repr__(self):
        return("Temperature({},'{}')").format(self.t,self.unit)

    def convert(self):
        if self.unit=='F':
            newt = Temperature((self.t-32)*(5/9), 'C')
        else:            
            newt= Temperature((self.t * (9/5))+32, 'F')
        return newt

    def __eq__(self,other):
        if self.unit != other.unit:
            newcon=self.convert()
            return newcon.t == other.t
        return self.unit == other.unit
    
    def __str__(self):
        return("{}°{}").format(self.t,self.unit)

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
## Question 2 ###
    
from tkinter import *
from tkinter.messagebox import showinfo

class TempConverter(Frame):

    #function#
    def clickonbutton(self):
        try:
            t = Temperature(float(self.temp.get()),self.unit.get()).convert()
        except ValueError:
            showinfo('Error:', 'Temperature must be a decimal or integer')
        except UnitError:
            showinfo('Error:','Unit should be either C or F')
        showinfo('Conversion', str(self.temp.get())+ '°' + self.unit.get().upper() + '=' + str(t))

    def __init__(self,parent=None):

        Frame.__init__(self,parent)

        # Label #
        labeltemp = Label(self, text = 'Temperature:')
        labeltemp.grid(row=0, column=1)
        labelunit = Label(self, text = 'Unit(C or F):')
        labelunit.grid(row=1, column=1)

        # Date Entry #
        self.temp = Entry(self)
        self.temp.grid(row=0, column=2)
        self.unit = Entry(self)
        self.unit.grid(row=1,column=2)

        # button #
        button = Button(self, text = 'Click to convert',command=self.clickonbutton)
        button.grid(row=2, column=1, columnspan=4)

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab5TEST.py') )    


 



    
