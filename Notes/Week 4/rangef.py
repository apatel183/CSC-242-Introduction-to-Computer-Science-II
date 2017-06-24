# rangef.py
# like a range, but represents floats

'''
# constructors
>>> r = rangef(0.0,10.2,.4)
>>> r[0]
0.0
>>> r[3]
1.2
>>> for x in r:
    print( x )
0.0
0.4
0.8
...
???
>>> len( r )
???

# other constructors
>>> rangef(9.7)
rangef(0,9.7,1.0)
>>> rangef(9.7,22.3)
rangef(9.7,22.3,1.0)

>>> rangef(9.7,22.3,1.0)[-3]
???

'''

# rangef will not inherit
import math
class rangef():

    def __init__(self,a,b=None,c=1.0):
        '''
        can be called 3 ways:
        rangef(stop)
        rangef(start,stop)
        rangef(start,stop,step)
        '''
        # only one argument given
        # it is stop 
        if  b==None:
            self.start = 0.0
            self.stop = a
            self.step = 1.0
        # a,b,c are start,stop,step
        else:
            self.start = a
            self.stop = b
            self.step = c

        # compute the number of items
        self.n = math.ceil( abs(self.stop-self.start)/self.step )

    def __repr__(self):
        return 'rangef({},{},{})'.format(self.start,self.stop,self.step)

    def __len__(self):
        return self.n
    
    def __getitem__(self,index):
        print('gi')
        if 0<=index<self.n:  # positive indices
            return self.start+self.step*index
        elif -self.n <= index <= -1:   # negative indices
            return self.start+self.step*(self.n+index)
        else:
            raise IndexError('rangef index out of range')
            

# Scott Myers, Effective C++, More Effective C++


        
        

    















