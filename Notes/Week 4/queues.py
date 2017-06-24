# queues.py - do NOT name this file queue.py

# hw2 is posted, due Friday

##### review #####

'''
Class
    - get/set methods called explicitly
    - some methods implicitly
        __init__ - constructor, initializes, add
                   data attributes
        __repr__ - called when str representation
                   is needed, str(obj), print(obj)
                   shell evaluation
    - operators are also called implicitly
       a=Point()
       b=Point()
       c=a+b -> c=Point.__add__(a,b)
       if (a==b):  ->  if ( Point.__eq__(a,b) ):

       many more

'''

##### Queue #####

'''
make this work:
>>> q = Queue()
>>> q.enqueue( 'Mary' )
>>> q.enqueue( 'Fred' )
>>> q.enqueue( 'Alice')
>>> q
Queue(['Mary','Fred','Alice'])
>>> nowserving=q.dequeue()
>>> nowserving   # FIFO - first in first out
'Mary'
>>> q[1]   # Queue.__getitem__
'Alice'
>>> q[1] = 'Sally' # not allowed
... causes Error/Exception of some sort ...
>>> qq = Queue( [1,2,3] )
>>> qq
Queue( [1,2,3] )
>>> len( qq )
3
>>> for item in qq:
    print( item )
1
2
3

we will make two versions:
    1) composition - Queue HAS A list
    2) inheritance - Queue IS A list


notes on indexing:
>>> q[1]

->

>>> Queue.__getitem__(q,1)
'''

##### Queue v1 uses composition #####
class Queue():

    # BAD: all defaults share the same list!!
    # because list is mutable
    def __init__(self,lst=list()):  # wrong!!
        # composition, self HAS A list attribute
        self.q = lst

    # GOOD: construct empty list in body
    # NO, this is still BAD
    def __init__(self,lst=None):
        if lst==None:
            self.q = list()   # self.q = []
        else:
            self.q = lst

    # GOOD, this is good and simpler
    def __init__(self,lst=list()):
        self.q = list( lst )
        # pizza:   self.toppings = set( tops )

    def __repr__(self):
        return 'Queue({})'.format(self.q)

    def enqueue(self,item):
        self.q.append( item )

    # remove from the front
    def dequeue(self):
        return self.q.pop(0)

    # when you write getitem, you get iteration
    # for free -> for item in q:
    def __getitem__(self,index):
        return self.q[index]

    # dont want item assignment, if you did
    # uncomment this
    # q[1]=88 -> Queue.__setitem__(q,1,88)
    ## def __setitem__(self,index,value):
    ##    self.q[index]=value
        

    def __len__(self):
        return len(self.q)

##### Queue v2 - inheritance #####

class CuttingError(Exception):
    pass


class Queue(list):

    # inherit __init__

    def __repr__(self):
        return "Queue({})".format( list.__repr__(self) )

    def enqueue(self,item):
        self.append(item)

    def dequeue(self):
        return self.pop(0)

    def __setitem__(self,index,item):
        raise CuttingError('no cutting in line jerk')

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'queuesTESt.py' ) )



##### try/except #####

'''
>>> # code can cause errors
>>> hello
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> 'a'*'c'
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    'a'*'c'
TypeError: can't multiply sequence by non-int of type 'str'
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> 
>>> x = 99
>>> try:
	print(1/x)
except:
	print( 'whoops, zero denominator
	       
SyntaxError: EOL while scanning string literal
>>> try:
	print(1/x)
except:
	print( 'whoops, zero denominator' )

	
0.010101010101010102
>>> try:
	print(1/x)
except:
	print( 'whoops, zero denominator' )

	
0.010101010101010102
>>> x = 0
>>> try:
	print(1/x)
except:
	print( 'whoops, zero denominator' )

	
whoops, zero denominator
>>> try:
	print(1/x)
except ZeroDivisionError:
	print( 'whoops, zero denominator' )

	
whoops, zero denominator
>>> try:
	print(1/x)
except NameError:
	print( 'whoops, zero denominator' )

	
Traceback (most recent call last):
  File "<pyshell#48>", line 2, in <module>
    print(1/x)
ZeroDivisionError: division by zero
>>> 
'''

    
    
    


























