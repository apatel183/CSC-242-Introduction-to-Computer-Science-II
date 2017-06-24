
>>> from hw3 import *

##### Stat ####

>>> s = Stat()
>>> s.add(2.5)
>>> s.add(4.7)
>>> s.add(78.2)
>>> s
Stat([2.5, 4.7, 78.2])
>>> len(s)
3
>>> s.min()
2.5
>>> s.max()
78.2
>>> s.sum()
85.4
>>> s.mean()
28.46666666666667
>>> s.clear()
>>> s
Stat([])


what happens if the stat is empty?
most methods give errors


>>> s = Stat()
>>> 
>>> len(s)
0
>>> s.min() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a min
>>> s.max() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a max
>>> s.mean() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a mean
>>> s.sum()
0


make sure empty Stats are distinct
(using None for default argument in init)

>>> s = Stat()
>>> s.add(33)
>>> t = Stat()
>>> t  # make sure using None as default in init
Stat([])

##### intlist #####

>>> il = intlist()
>>> il
intlist([])
>>> il = intlist([1,2,3])
>>> il
intlist([1, 2, 3])
>>> il.append( 5 )
>>> il
intlist([1, 2, 3, 5])
>>> il.insert(1,99)
>>> il
intlist([1, 99, 2, 3, 5])
>>> il.extend( [22,44,66] )
>>> il
intlist([1, 99, 2, 3, 5, 22, 44, 66])
>>> odds = il.odds()
>>> odds
intlist([1, 99, 3, 5])
>>> evens = il.evens()
>>> evens
intlist([2, 22, 44, 66])
>>> il
intlist([1, 99, 2, 3, 5, 22, 44, 66])
>>> il[2] = -12   # calls __setitem__
>>> il
intlist([1, 99, -12, 3, 5, 22, 44, 66])
>>> il[4]   # calls __getitem__
5


trying to get non ints into an intlist
will always raise an error

>>> il.append(33.4) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
NotIntError: 33.4 not an int
>>> il.insert(2,True) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
NotIntError: True not an int
>>> il = intlist([2,3,4,"apple"]) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
NotIntError: apple not an int
>>> il.extend( [2,3,'hello']) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
NotIntError: hello not an int
>>> il[2] = 22.3 #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
...
NotIntError: 22.3 not an int



make sure using None as default argument

>>> lst1 = intlist()
>>> lst1.append( 99 )
>>> lst2 = intlist()
>>> lst2
intlist([])

make sure that code really subclasses list
actually check that self has no attributes

>>> vars(lst1)  # check that subclasses list
{}




