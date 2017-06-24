# inherit.py

##### homework #####
'''
hw1 - grades posted later today
doctest - MUST run this
if you need help - email your .py and question

hw2 due tomorrow - use a set for toppings

'''

##### week 4 #####
'''
hw3 is posted, due Friday, start right away
   2nd problem requires inheritance,
   1st is your choice

midterm - in class on Thursday 2/11

composition - HAS A list
    self.q is the list, .q is an attribute of self
    self.q = list()
    self.q.append( item )

    get what you want, nothing more or less


inheritance - IS A list
    self is the list
    self = list()
    self.append( item)

    get stuff for free (might save time)
    might get more than you want
    (might have to remove/modify)

'''

##### set #####

'''

>>> s
{1, 2, 3, 6, 7}
>>> s.add( 'apple' )
>>> s.add( 7 )
>>> s.add( 3 )
>>> s
{1, 2, 3, 'apple', 6, 7}
>>> s.remove( 7 )
>>> s
{1, 2, 3, 'apple', 6}
>>> 
>>> 
>>> # create an empty set
>>> ss = {}
>>> ss
{}
>>> type(ss)
<class 'dict'>
>>> ss = set()
>>> type(ss)
<class 'set'>
>>> lst = [2,3,1,1,6]
>>> set( lst )
{1, 2, 3, 6}
>>> 

'''

##### simple example #####

# when inheriting from list
# self IS A list

class MyList(list):  # MyList is a list

    def apply(self,f):
        for i in range(len(self)):
            self[i] = f( self[i] )

'''

MyList is a list, with all the functionality of
a list, but with some additional functionality,
the method apply.

>>> ml = MyList()
>>> type(ml)
<class '__main__.MyList'>
>>> 
>>> ml.append( 4 )
>>> ml.append( 7)
>>> ml
[4, 7]
>>> ml[0]
4
>>> ml.extend( [2,-5,-5,-9,2,3,-11] )
>>> ml
[4, 7, 2, -5, -5, -9, 2, 3, -11]
>>> ml.apply( abs )
>>> ml
[4, 7, 2, 5, 5, 9, 2, 3, 11]
>>> ml.apply( range )
>>> ml
[range(0, 4), range(0, 7), range(0, 2), range(0, 5), range(0, 5), range(0, 9), range(0, 2), range(0, 3), range(0, 11)]
>>> 
'''


##### inheritance #####

'''
terminology:

MyList inherits from list
MyList subclasses list
MyList is a child class of list

list is the parent class of MyList
list is the super class of MyList

assume:

    class Sub(Super):   # Sub inherits from Super
        # implementation

and I create an object of the subclass

    obj = Sub()

when you say:

    obj.attr

we look for attr, in order:
    0) obj.attr - data
    1) Sub.attr - methods
    2) Super.attr - methods

'''

class Super():
    def __init__(self):
        self.var = 99
        print( 'Super.__init__')
    def a(self):
        print ('Super.a()')
    def b(self):
        print ('Super.b()')
    def c(self):
        print ('Super.c()')
'''
Sub class can:
a) inherit a method
b) override a method
c) extend a method
d) add a method
'''
class Sub(Super):
    # a) to inherit, do nothing
    # hint: sometimes you can get away without init

    # override the Super's method
    def b(self):
        print( 'Sub.b()')
    # extend a method, call the Super's and do more
    def c(self):
        Super.c(self) # call Super's method too
        print( 'Sub.c()')
    # add a method
    def d(self):
        print( 'Sub.d()')

'''
make this work:
>>> s = strlist()
>>> s.append('a')
>>> s
['a']
>>> s.append(3)
Error

in which ways can data to a list:
append
extend
__setitem__ (indexing),  s[3]=99, should cause an error
insert
constructor'''

# strlist is a list that only allows
# str's as items

class strlist(list):

    def __init__(self,lst=[]):
        # 1st call list constructor for empty list
        list.__init__(self)  # dont give 2nd argument
        # extend with contents if there
        self.extend( lst )

    def __repr__(self):
        # watchout for infinite recursion
        # return "strlist({})".format( self )
        return "strlist({})".format( list.__repr__(self) )
        

    def extend(self,lst):
        for item in lst:
            self.append( item )  # does validation
            
    def append(self,item):
        # an insert at the end
        self.insert( len(self), item)   # does validation

    def __setitem__(self,index,item):
        if type(item)==str:
            #list.insert(self,index,item)
            # self[index]=item # infinite recursion
            list.__setitem__(self,index,item)
        else:
            raise TypeError('item is not a str')
        
    def insert(self,index,item):
        if type(item)==str:
            list.insert(self,index,item)
        else:
            raise TypeError('item is not a str')


        

    


    

    

    
        






















