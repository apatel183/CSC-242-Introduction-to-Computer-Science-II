12
23
99.9
4.5
77
0
23.2
-9.5
-99

above lines are user inputs to be used for code
that requires user input

code below directs input to be received from above
should not cause an error

>>> from lab1 import *
>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('lab1TEST.py')


##### printTwoLargest ######

>>> printTwoLargest()
Please enter a number: Please enter a number: Please enter a number: Please enter a number: Please enter a number: Please enter a number: The largest is 99.9
The second largest is 77
>>> printTwoLargest()
Please enter a number: Please enter a number: The largest is 23.2
>>> printTwoLargest()
Please enter a number: No positive numbers were entered
>>>

put stdin back to original, again, shouldnt cause error
>>> sys.stdin = si  # return stdin

##### printWordsLines ######

>>> printWordsLines('test1.txt')
The file test1.txt contains 17 words and 3 lines.
>>> printWordsLines('test2.txt')
The file test2.txt contains 38 words and 5 lines.
>>> 


##### reverseDict ######

>>> reverseDict( {'a':1,'b':2,'c':3})=={1: 'a', 2: 'b', 3: 'c'}
True
>>> reverseDict( {1:'apple', 2:'pear', 3:'orange'} )=={'orange': 3, 'apple': 1, 'pear': 2}
True
>>> d=dict( zip('abcdefghijklmnopqrstuvwxyz',range(26)))
>>> reverseDict(d)=={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
True


