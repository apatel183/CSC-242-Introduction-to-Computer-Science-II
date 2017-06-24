# reviewNamespaces.py

##### today #####

# admin
# review
# doctest
# namespaces ?


##### review #####

'''
want this to work:   ? matches any single character

>>> allMatches( 'b?b', 'bob bad apple_djsfkj bib')
['bob','b b','bib']
'''

# would be very helpful to have this

'''
>>> match('bob','bob')
True
>>> match('b?b','bob')
True
>>> match('b?b','Bob')
False
>>> match('b?b','bad')
False
>>> match('b?b','bobby')
False
>>> match('??','xy')
True
>>> match('??','xyz')
False
'''

def match(pattern,s):
    ''' return True if s matches patter, that is
char for char match except ? in pattern matches
any single character '''

    # answer is no if words have different lengths
    if len(s)!=len(pattern):
        return False
    
    for i in range(len(s)):
        # print( i, pattern[i], s[i] )
        if pattern[i]!=s[i] and  pattern[i]!='?': #n=mismatch
            return False
    return True



'''
>>> # iteration
>>> # "standard" iteration, uses iterator
>>> s = 'apple'
>>> for c in s:
	print( c )

	
a
p
p
l
e
>>> # indexed iteration
>>> for i in range(len(s)):
	print( i, s[i] )

	
0 a
1 p
2 p
3 l
4 e
>>> 
'''

def allMatches( pattern, s):
    ''' return a list of all substrings of s
that match pattern '''

    lst = []
    # iterate over all substrings
    # of s with length same as pattern
    for i in range(len(s)):
        if match(pattern,s[i:i+len(pattern)]): # a match
            #print( i, s[i:i+len(pattern)] )
            lst.append( s[i:i+len(pattern)] )
    return lst


##### dict #####

'''
>>> d = {}
>>> d['x']=99
>>> d
{'x': 99}
>>> d['x']
99
>>> 
'''


##### namespaces #####


lst = [1,2,3,4,5]
def f(target,lst):
    print( vars())
    2+3 # wasted expression
    for item in lst:
        if item==target:
            print(item)

'''
>>> f(2,lst)
{'lst': [1, 2, 3, 4, 5], 'target': 2}
2
>>>
'''

'''
syntax highlighting:

orange - def, for, in - reserved words, core Python
purple - print - built in
black and blue -
    [1,2,..5] - literals, values
    f, target, lst - variables, names
green - comments, str's


names
    names refer to objects
    names are evaluated to the objects they refer to

namespace
    dictionary mapping names to objects
    exist in many different contexts

vars()
    vars() - returns local (current) dictionary
    vars( object ) - return object's dictionary
    
look up a name in namespaces:
    1) local namespace (function)
    2) global/module namespace
    3) builtins
    

'''

##### importing #####

'''
import math - import module math into current namespace
from math import pi
from math import *
    puts names from math into current space

>>> import math
>>> 
>>> 
>>> math
<module 'math' (built-in)>
>>> math.pi
3.141592653589793
>>> pi
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> 
>>> from math import pi
>>> pi
3.141592653589793
>>> 

'''

##### constructors #####

'''
constructors are the function
that build objects, you have probably
used them to convert objects from one
type to another

>>> i = 99
>>> i
99
>>> type(i)
<class 'int'>
>>> i = int(9.3)
>>> i
9
>>> i = int('99')
>>> i
99
>>> d = {}
d
>>> 
>>> d = dict()
>>> s = set()  # calls set constructor
>>> s
set()
>>> range(10)
range(0, 10)
>>> list( range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(99999999)
range(0, 99999999)
>>> range(3,20,2)
range(3, 20, 2)
>>> range(3,20,2)[0]
3
>>> range(3,20,2)[4]
11
>>> 

>>> list('apple')
['a', 'p', 'p', 'l', 'e']
>>> 
'''


##### look ups 2 #####

'''

x.y - y is an attribute of x

look up in order

1) in the object x's namespace, vars(x)
    generally data found here
2) if x has type MyClass
    then also look
       a) MyClass namespace, i.e. vars(MyClass)
          methods typically found here
       b) namespace of parent/super class

lst = list()
lst.append() - append in list namespace (2a)

'''

##### IMPORTANT #####
'''
suppose

obj = MyClass()

then, if you say

obj.method( a,b,c)

then Python translates this to

MyClass.method(obj,a,b,c)

examples:


>>> s = 'hello'
>>> s.upper()
'HELLO'
>>> s
'hello'
>>> vars(s)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    vars(s)
TypeError: vars() argument must have __dict__ attribute
>>> str.upper(s)
'HELLO'
>>> 
>>> 
>>> lst = list()
>>> lst.append( 7 )
>>> 
>>> list.append(lst,7)
>>> lst
[7, 7]
>>> 
>>> 
>>> x = lst.pop()
>>> x
7
>>> x = list.pop( lst )
>>> x
7
>>> lst
[]
>>> 

'''        


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'rnTEST.py' ))






















