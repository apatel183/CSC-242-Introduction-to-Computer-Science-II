# recursion.py

# midterm - will be graded
# tkinter - done with this, wont be on final

##### recursive function #####
'''

recursive function is a function
that calls itself

generally, 2 parts:

    1) bases case(s) - deal with "smallest" cases
       directly
    2) recursive case - general cases, function
       calls itself with "smaller" input(s)

advice: write base case(s) first  

'''

##### "review" #####

def f(n):
    print( 'start f',vars())
    g(n-1)
    print( 'end f',vars())

def g(n):
    print( 'start g',vars())
    h(n-1)
    print( 'end g',vars())

def h(n):
    print( 'start h',vars())
    print( n )
    print( 'end h',vars())

'''
like russian dolls:
notice that n exists simultaneously
with different values in different
namespaces (and that is ok)


>>> f(5)  # what is the output?
start f {'n': 5}
start g {'n': 4}
start h {'n': 3}
3
end h {'n': 3}
end g {'n': 4}
end f {'n': 5}
>>> 
'''

##### recursive functions that print #####

def countdown(n):

    print(n)
    if n<=0: # base case, doesnt call itself
        print('blast off')
    else: # recursive case, calls itself
        countdown(n-1)
        
'''
>>> countdown(3) # what is output
3
2
1
0
blast off
>>> 

>>> countdown(3) # what is output
3  print(3)

2
1   countdown(2)
0
blast off
>>> 

i.e.

countdown(3)= print(3), countdown(2)

'''

# remark, dont ever do this
# infinite recursion
# 
def f(n):
    f(n-1)

    

'''
make this work, print digits of a number vertically:
no loops, no str's

looks like a loop?  => use peel off one strategy

>>> vertical(3124)
3
1  vertical(312) , vertical (3124//10)
2

4  print(4)        print(3124%10)
>>> vertical(567)
5
6  vertical(56)   56=567//10

7   print(7)
>>> vertical(7) # base case, just print it
7
>>> vertical(n)  # at least two digits
vertical(n//10)  - all but last digit
print(n%10)   - last digit


'''

def vertical(n):  # assume n>=0

    # base case, single digit, print it
    if n<10:
        print( n )
    # recursive case
    else:
        vertical(n//10)
        print(n%10)

'''
make this work:  print numbers digits in reverse order
no loops, strs

>>> reverse(3124)
4 213
print(4)
reverse(312)
>>> reverse(12345)
5 4321
print(5)
reverse(1234)
>>> reverse(9)
9
>>> reverse(n)
print( 1's digit of n)
reverse( all digits of n except 1's digit)

'''


def reverse(n):

    # base case, single digit, print it
    if n<10:
        print(n,end='')
    # recursive case, peel of 1's digit
    else:
        print(n%10,end='')  # 1's digit
        reverse(n//10)  # all other digits

'''
make thsi work, no loops:
>>> cheers(0)
Hooray!
>>> cheers(1)
Hip Hooray!
>>> cheers(2)
Hip Hip Hooray!
>>> cheers(3)
Hip Hip Hip Hooray!
Hip cheers(2)
>>> cheers(77)
Hip   cheers(76)
>>> cheers(n)
Hip   cheers(n-1)
'''

def cheers(n):

    if n<=0:
        print('Hooray!')
    else:
        print('Hip',end=' ')
        cheers(n-1)

# not so easy with loops
'''
make this work:

>>> pattern(0)
0
>>> pattern(1)
010
>>> pattern(2)
0102010
>>> pattern(3)
010201030102010
>>> pattern(4)
010201030102010 4 010201030102010
pattern(3) 4 pattern(3)
>>> pattern(7)
pattern(6) 7 pattern(6)
>>> pattern(n)
pattern(n-1) n pattern(n-1)
'''

# v1 - with explicit base case
def pattern(n):

    if n==0:
        print(0,end='')
    else:
        pattern(n-1)
        print(n,end='')
        pattern(n-1)

# v2 - with empty base case
def pattern(n):

    if n>=0:
        pattern(n-1)
        print(n,end='')
        pattern(n-1)


##### hw hints #####

'''
pascalLine
    - use recursion AND iteration

curve problem
    - will make sense after today
'''

##### recursive function that return something #####
'''
Golden Rule:

every branch of the function should return
something of the same type
(and in particular, should return something!)
'''

'''
make this work:

>>> factorial(0)  #0!
1
>>> factorial(1)
1
>>> factorial(3)
6 # 6 = 3*2*1
>>> factorial(8)
???   = 8*7*6*...*2*1 = 8 * factoral(7)
'''

def factorial(n):

    if n==0:
        return 1
    else:
        return n*factorial(n-1)

'''
>>> for i in range(10):
	print( i, factorial(i))

	
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
>>> 
'''

'''
fibonacci numbers

n     = 0,1,2,3,4,5, 6, 7
fib(n)= 1,1,2,3,5,8,13,21,34,55,...

every number is the sum of two previous

'''

# v1 - recursive, does a lot of redundant work
def fib(n):

    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# v2 - iterative, way faster
def fib(n):

    curr,prev = 1,0
    for i in range(n):
        curr,prev = curr+prev,curr
    return curr

# v3 - recursive with memory/cache?  will work

'''
pattern that returns rather than print

>>> pattern(0)
'0'
>>> pattern(3)
'010201030102010'
pattern(2) + '3' + pattern(2)
'''

def pattern(n):

    if n==0:
        return '0'
    else:
        return pattern(n-1) + str(n) + pattern(n-1)

# with empty base case?  no!
# but could have base case that returns empty str ''

##### turtle graphics #####

'''
>>> from turtle import Screen,Turtle
>>> s = Screen()
>>> t = Turtle()
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> t.forward(100)
>>> t.left(90)
>>> 

also:
t.setpos(x,y)
t.up() - pen up, stop drawing
t.down() - start drawing
'''

'''
make this work:
>>> draw( 4*'FL',100,90)
... draws a square with lengths 100 ...
'''

# a little more general than what is in the book

from turtle import Screen, Turtle

def draw( directions, length=100, angle=90,x=0,y=0):
    ''' draw string directions:
        start at x,y
        F - forward length
        R - right turn angle
        L - left turn angle
    '''
    s = Screen()
    t = Turtle()
    t.up()
    t.setpos(x,y)
    t.down()
    t.speed(0)

    for move in directions:
        if move=='F':
            t.forward(length)
        elif move=='R':
            t.right(angle)
        elif move=='L':
            t.left(angle)
        else:
            print('bad move')

    s.exitonclick()

def koch(n):
    ''' return directions for nth koch curve '''
    if n==0:
        return 'F'
    else:
        #return koch(n-1)+'L'+koch(n-1)+'RR'+koch(n-1)+'L'+koch(n-1)
        k = koch(n-1)
        return k + 'L' + k + 'RR' + k + 'L' + k

n = 4
# draw( koch(n), 400/3**n, 60, -200, 100)
draw( 3*(koch(n)+'RR'), 400/3**n, 60, -200, 100)



    

























