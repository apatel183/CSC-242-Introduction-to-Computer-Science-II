# myset.py

##### midterm #####
'''
2 weeks from today:
    in class on lab computers
    here usual time
    HARDCOPY notes: (print before you get here,
    2 double-sided or 4 single sided pages, will
    be collected)
'''


##### Pizza #####
'''
class Pizza:

    def __init__(self,size='M',toppings=set()):
        # make sure you call set()
        self.size = size.upper()
        self.toppings = set(toppings)

    def price(self):

        # options are mutually exclusive
        # so use elif (and else, maybe)
        if self.size in 'sS':
            return 5 + len(self.toppings)*.75
        elif self.size in 'mM':
            return 5 + len(self.toppings)*.75
        elif self.size in 'lL':
            return 5 + len(self.toppings)*.75
        
    def __repr__(self):

        return "blajh{}".format()

        ret = "Pizza("
            + self.size
            + ")"
        return ret

# not so great version
def orderPizza():

    toppings = set()
    size = input ()
    while:
            topp = input()
            set.add( topp )

    return "Pizza({}.{})".format(size,toppings)

# much better
def orderPizza()
    p = Pizza()
    size = input()
    p.setSize(size)
    while
        topp = input()
        p.addTopping( topp)

    return p
'''
    
##### hw #####
'''
# dont do this, do both inhertiance and composition

# looks like inheritance
# self IS A list
class intlist(list):  # inherits from list

    def __init__(self,iterable=[]):
        # looks like composition
        # self HAS A list
        self.lst = list( iterable )
'''

class EmptyStatError(Exception):
    pass

##### myset #####

# myset will inherit from list
# NOT a complete implementation -
# for example, dont bother to turn off append and many other things
class myset(list):
    
    def __init__(self, iterable=[]):
        for item in iterable:
            self.add( item )

    def __repr__(self):
        return "myset({})".format(list.__repr__(self))

    def add(self,item):
        if item not in self:
            self.append( item )

    # get remove for free
    # list has a remove method

    # really should turn off
    # indexing, __setitem__, __getitem__
    '''
    def __getitem__(self,index):
        pass
    '''

    # comparisions
    # easiest to write <= first
    # a <= b, means if and only every element
    # of a is also in b
    def __le__(self,other):
        print('le')
        # search for an item of self that is not in
        # other
        for item in self:
            if item not in other:
                return False
        # every item was found
        return True

    def __lt__(self,other):
        print('lt')
        '''
        if self<=other and len(self)<len(other):
            return True
        else:
            return False
        '''
        return self<=other and len(self)<len(other)

    def __eq__(self,other):
        return self<=other and len(self)==len(other)

    
    def __ge__(self,other):
        return other<=self

    def __gt__(self,other):
        return other<self

    def __ne__(self,other):
        return not self==other
    
    
























