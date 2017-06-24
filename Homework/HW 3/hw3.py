###hw3.py###
###Arpan Patel## 

###Question 1###
class EmptyStatError(Exception):
    pass

class Stat():

    def __init__(self, numbers=list()):
        self.s= list(numbers)

    def __repr__(self):
        return 'Stat({})'.format(self.s)

    def add(self,numbers):
        self.s.append(numbers)

    def min(self):

        try:
           return min(self.s)
        except:
            raise EmptyStatError ('empty Stat deos not have a min')

    def max(self):

        try:
            return max(self.s)
        except:
            raise EmptyStatError ('empty Stat deos not have a max')

    def sum(self):

        try:
            return sum(self.s)
        except:
            raise EmptyStatError ('empty Stat deos not have a sum')

    def mean(self):

        try:
            return float(sum(self.s)/len(self.s))
        except:
            raise EmptyStatError ('empty Stat deos not have a mean')
        
    def clear(self):
        self.s= []
    

    def __len__(self):
        return len(self.s)
#TEST
'''
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
If a Stat is empty, several (but not all) methods raise errors.  Note that you won’t literally see “…”.   You will instead see more information on the error. 
>>> s = Stat()
>>> 
>>> len(s)
0
>>> s.min()
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a min
>>> s.max()
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a max
>>> s.mean()
Traceback (most recent call last):
...
EmptyStatError: empty Stat does not have a mean
>>> s.sum()
0
''''
###Question 2 ##

class NotIntError(Exception):
    pass

class intlist(list):

    def __init__(self,lst=[]):
        list.__init__(self)
        self.extend(lst)
    

    def __repr__(self):
        return 'intlist({})'.format(list.__repr__(self))

    def extend(self,lst):
        for item in lst:
            self.append(item)

    def append(self,item):
        self.insert(len(self),item)

    def __setitem__(self,index,item):
        if type(item)==int:
            list.__setitem__(self,index,item)
        else:
            raise NotIntError ('item is not an int')

    def insert(self,index,item):
        if type(item)==int:
            list.insert(self,index,item)
        else:
            raise NotIntError ('item is not an int')
        
    def odds(self):
        oddnumbers=intlist()
        for number in self:
            if number%2!=0:
                oddnumbers.append(number)
        return oddnumbers
               
    def evens(self):
        evennumbers=intlist()
        for number in self:
            if number%2==0:
                evennumbers.append(number)
        return evennumbers

#TEST
'''
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
Trying to put anything except for an int into an intlist will always raise an NotIntError.  Note that there 5 different ways this could be attempted:
>>> il.append(33.4)
Traceback (most recent call last):
...
NotIntError: 33.4 not an int
>>> il.insert(2,True)
Traceback (most recent call last):
...
NotIntError: True not an int
>>> il = intlist([2,3,4,"apple"])
Traceback (most recent call last):
...
NotIntError: apple not an int
>>> il.extend( [2,3,'hello'])
Traceback (most recent call last):
...
NotIntError: hello not an int
>>> il[2] = 22.3
Traceback (most recent call last):
...
NotIntError: 22.3 not an int
'''
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw3TEST.py'))
        
    
    
    
        
