# lab6TEST.py

>>> from lab6 import *

##### ScoreList #####

>>> s = ScoreList()
>>> s.add(57)
>>> s.passing()
False
>>> s.add(83)
>>> s.add(80.2)
>>> s.add(104)  #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ScoreError: score 104 not between 0 and 100
>>> s
ScoreList([57, 83, 80.2])
>>> s.avg()
73.39999999999999
>>> s.passing()
True
>>> max( s )
83
>>> min( s )
57
>>> len( s )
3
>>> s[1]
83
>>> s.sort()
>>> s
ScoreList([57, 80.2, 83])
>>>

>>> s = ScoreList( [80,30,100] )
>>> s == eval(repr(s))  # test, init, repr, ==
True
>>> s = ScoreList( [80,-10,100]) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
ScoreError: score -10 not between 0 and 100
>>> s = ScoreList( [80,10,110]) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):   
...
ScoreError: score 110 not between 0 and 100
>>> 



##### Scrambler #####

>>> from random import *
>>> seed(0)
>>> Scrambler("apple").pack()
>>> seed(1)
>>> root = Tk()
>>> Scrambler("orange",root).pack()
>>> 

