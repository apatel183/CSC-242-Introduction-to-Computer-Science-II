# lab5TEST.py

>>> from lab5 import *

##### Temperature #####

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
>>> Temperature('apple','c') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ValueError: could not convert string to float: 'apple'
>>> Temperature(21.4,'t') #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
UnitError: Unrecognized temperature unit 't'


##### TempConverter #####

>>> root = Tk()
>>> TempConverter(root).pack()
>>> TempConverter(root).pack()
>>> root.destroy()
>>> t = TempConverter().pack()
>>>
