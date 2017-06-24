# recursion2.py

# recall the following


# prints
def pattern(n):

    if n==0:
        print(0,end=' ')
    else:
        pattern(n-1)
        print(n,end=' ')
        pattern(n-1)

'''
>>> pattern(3)
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
>>> pattern(4)
0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 4 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0 
>>> 
'''

# do a return version of the same pattern
# leave out the spaces

def pattern(n):

    if n==0:
        return '0'
    else:
        return pattern(n-1)+str(n)+pattern(n-1)

'''
>>> pattern(3)
'010201030102010'
>>> pattern(4)
'0102010301020104010201030102010'
>>> 
'''

##### turtle graphics #####

from turtle import Screen,Turtle

# draw a square
'''
>>> s = Screen()
>>> t = Turtle()
>>> t.forward(50)
>>> t.lt(90)
>>> t.forward(50)
>>> t.lt(90)
>>> t.forward(50)
>>> t.lt(90)
>>> t.forward(50)
>>> 

also:
t.setpos(x,y)
t.up()
t.down()
'''

'''
make this work (draws a square):
>>> draw('FLFLFLFL',50,90) # 50 pixels, 90 degrees
>>>
'''

from turtle import Screen,Turtle

# this is a bit different than the book
# little more general

def draw(directions,length=100,angle=90,x=0,y=0):
    ''' draw string directions:
    start at x,y
    F - forward length
    L - left turn angle
    R - right turn angle
    '''

    # initialize
    s = Screen()
    t = Turtle()
    t.up()
    t.setpos(x,y)
    t.down()
    t.speed(300)

    # draw directions
    for move in directions:
        if move=='F':
            t.forward(length)
        elif move=='L':
            t.lt(angle)
        elif move=='R':
            t.rt(angle)
        else:
            print( 'bad move')

    s.exitonclick()


'''
make this work:
>>> koch(0)
'F'
>>> koch(1)
'FLFRRFLF'
>>> koch(2)
'FLFRRFLF' + 'L' + 'FLFRRFLF' + 'RR' + 'FLFRRFLF' + 'L' + 'FLFRRFLF'
>>> koch(3)
koch(2) + 'L' + koch(2)+'RR' + koch(2) + 'L' + koch(2)
'''

# v1 - not so efficient
def koch(n):

    if n==0:
        return 'F'
    else:
        return koch(n-1)+'L'+koch(n-1)+'RR'+koch(n-1)+'L'+koch(n-1)

# v2 - more efficient
def koch(n):

    if n==0:
        return 'F'
    else:
        k = koch(n-1)
        return k+'L'+k+'RR'+k+'L'+k




#draw( koch(1),200,60,-300,0 )
n=4
#draw( koch(n),400/3**n,60,-200,0)

# snowflake, 3 copies with a turn in between

#draw( 3*(koch(n)+'RR'),400/3**n,60,-200,100)


# recall fibonacci numbers: 1,1,2,3,5,8,13,21,...

def fib(n):

    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# way more efficient - use a loop
def ifib(n):
    curr=1
    prev=1
    for i in range(n):
        # iterate
        curr, prev = curr+prev, curr
    return curr

    
























