# Point.py - our first class

'''
Remember last time:

>>> "how are you?".split()
['how', 'are', 'you?']

- Python translates ->

>>> str.split("how are you?")
['how', 'are', 'you?']
>>>
'''

##### Point - v1 #####

'''
make this work:

>>> p = Point()  # constructor
>>> p.setx(3)  # -> Point.setx(p,3)
>>> p.sety(-5.4)
>>> p.get()
(3,-5.4)
>>> p.move(-1,1)  # delta, move by this amount
>>> p.get()
(2,-4.4)

>>> p
Point(2,-4.4)
... add more later ...
'''

# declare a class, our own data type
'''
general setup:
    Class gets methods (functions/defs)
    objects get data attributes
'''

class Point():

    # method - function defined inside a class
    def setx(self,xcoord):
        self.x = xcoord    # self records x attribute

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return ( self.x,self.y )

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
'''
>>> p = Point()
>>> p.setx(3)
>>> p.sety(-5)
>>> p.move(1,-1)
>>> p.get()
(4, -6)
>>> p
<__main__.Point object at 0x02BBA610>
>>> 
>>> p = Point()
>>> p.setx(10)
>>> p.get()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    p.get()
  File "C:/Users/cdminstructor/Documents/csc242Sedgwick/s1010/Point.py", line 52, in get
    return ( self.x,self.y )
AttributeError: 'Point' object has no attribute 'y'
>>> 
'''

##### Point - v2 #####
'''
1st fix error that occurred above

>>> p = Point()  # calls constructor
>>> p.get()  # shouldnt cause an error
(0,0)
>>> p.setx(3)
>>> p.get()
(3,0)
>>> p = Point(3,4)
>>> p.get()
(3,4)
>>> p
Point(3,4)

Add some implicit things:

__init__ is the constructor
it is responsible for building the object
initially, primarily adding any data
attributes that will be accessed by
later methods

Python translates:

p=Point() ---> Point.__init__(p)

>>> p = Point(3,4)  # __init__
>>> p # Python calls __repr__
Point(3,4)
>>> p = Point()   # __init__ with defaults 0,0
>>> print( p ) # calls __repr__

__repr__: Python calls the method __repr__  (or __str__)
when a str representation of the object is
required

Note:

>>> # default arguments
>>> def f(x=7):
	return 2*x

>>> f(4)
8
>>> f()
14
>>> 


'''

class Point():

    # constructor is called automatically
    # when you say Point()
    # creates necessary data attributes
    def __init__(self,xcoord=0,ycoord=0):
        # print('__init__')
        # creates data attributes
        self.x = xcoord
        self.y = ycoord

    def __repr__(self):
        ''' returns str version of self
called whenever a str is needed '''
        #print( '__repr__')
        return "Point({},{})".format(self.x,self.y)

    # method - function defined inside a class
    def setx(self,xcoord):
        self.x = xcoord    # self records x attribute

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return ( self.x,self.y )

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay


##### Point v3 - operator overloading #####

'''
want this to work:
>>> p = Point(1,-1)
>>> q = Point(2,3)
>>> p+q
Point(3,2)
>>> p == Point(1,-1)
True
>>> p!=q
True


operator overloading:  making operators
apply to different data types

Python translates:

mathematical operators:

+ -> __add__
- -> __sub__
* -> __mul__

boolean operators:

default behavior of == is to see
whether the objects are the same (ie. same mem location)

== -> __eq__
!= -> __ne__
<  -> __lt__
<= -> __le__
>  -> __gt__
>= -> __ge__

note: you may not need to implement all of these,
you may be able to implement some and get the
others for free

'''


class Point():

    # constructor is called automatically
    # when you say Point()
    # creates necessary data attributes
    def __init__(self,xcoord=0,ycoord=0):
        # print('__init__')
        # creates data attributes
        self.x = xcoord
        self.y = ycoord

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

    def __eq__(self,other):
        print( 'eq')
        '''
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
        '''
        return (self.x==other.x and self.y==other.y)
        #return (self.x,self.y)==(other.x,other.y)

    def __repr__(self):
        ''' returns str version of self
called whenever a str is needed '''
        #print( '__repr__')
        return "Point({},{})".format(self.x,self.y)

    # method - function defined inside a class
    def setx(self,xcoord):
        self.x = xcoord    # self records x attribute

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return ( self.x,self.y )

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay

##### Point client ####
'''
make this work:

>>> p = movePointAround()
Enter a point: 2,3
Move how?: 1,1
Point(3,4)
Move how?: -1,5
Point(2,9)
Move how?:
>>> p
Point(2,9)
'''

##### Point client #####

def movePointAround():

    t = eval(input('Enter a point: '))
    p = Point(t[0],t[1])
    while True:
        ans = input('Move how?: ')
        if ans=='':
            return p
        t = eval(ans)
        p += Point(t[0],t[1])
        # or, p.move(t[0],t[1])

'''
>>> p = movePointAround()
Enter a point: 2,3
Move how?: 1,-1
Move how?: 1,1
Move how?: 1,3
Move how?: 
>>> p
Point(5,6)
>>> 
'''











