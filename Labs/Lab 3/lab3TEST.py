# lab3TEST.py

>>> from lab3 import *

##### Stack #####            

>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s.push('pear')
>>> s.push('kiwi')
>>> s
Stack(['apple', 'pear', 'kiwi'])
>>> top = s.pop()
>>> top
'kiwi'
>>> s
Stack(['apple', 'pear'])
>>> len(s)
2
>>> s.isEmpty()
False
>>> s.pop()
'pear'
>>> s.pop()
'apple'
>>> s.isEmpty()
True
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s[0]
'apple'
>>> 

check that Stacks constructed without a list remain distinct
if you receive an error on s2 then you probably need to use a
default argument of None in __init__
(see the Queue class developed in class for an example)

>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s2 = Stack()
>>> s2.push('pear')
>>> s2  # if this fails - see the TEST file for explanation
Stack(['pear'])


##### parenthesesMatch #####


>>> parenthesesMatch('(){}[]')
True
>>> parenthesesMatch('{[()]}')
True
>>> parenthesesMatch('((())){[()]}')
True
>>> parenthesesMatch('(}')
False
>>> parenthesesMatch('({])')
False
>>> parenthesesMatch('((())')
False
>>> parenthesesMatch('(()))')
False
