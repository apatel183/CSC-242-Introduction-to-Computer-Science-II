# review.py

# week 10
# last lab tomorrow
# last hw due Friday
# csc 300 next quarter?
    # do some Java prep first
    # code academy?
    # eclipse
    # c++



##### towers of hanoi #####

# download from d2l
# done separately

##### final exam #####

# final here
# March 17, 2016, from 8:30 AM to 10:45 AM
# same format and rules:
# on compute
# HARDCOPY NOTES: 2 double sided -OR- 4 single sided
#                 will be collected

'''
cumulative, includes most midterm material
    inheritance
    will not cover - guis,tkinter
recursion, Chapter 10
HTMLParser
Crawler
'''

##### midterm #####

# go over midterm
# will not be posted

##### final practice #####

'''
make this work:
>>> pattern(1)
1
>>> pattern(2)
 1
121
 1
>>> pattern(3)
  1
 121
  1
12321
  1
 121
  1
>>> pattern(2,3)
    1
   121
    1
'''

def pattern(n,shift=0):

    # base case
    if n==1:
        print(shift*' '+str(1))
    # recursive case
    else:
        # prev pattern, shifted +1
        pattern(n-1,shift+1)
        # print up/down, i.e. 123...n...321
        print(shift*' ',end='') # spaces
        for i in range(1,n):
            print(i,end='')
        for i in range(n,0,-1):
            print(i,end='')
        print()
        # prev pattern, shifted +1
        pattern(n-1,shift+1)

'''
make this work:
return the count of even numbers in a nested list
>>> count( [1,[2,[3],4],5,[6,[[7],8]],9] )
4
'''

def count( tree ):

    # base case, not a list
    # return 1 or 0, depending on whether number
    # is even or odd
    if type(tree)!=list: # tree an int
        if tree%2>0:
            return 0
        else:
            return 1
        #return abs(tree%2-1)
        #return (tree+1)%2
    # recursive case, is a list
    # iterate over branches
    # accumulate number of evens in each branch
    # return total
    else:
        cnt = 0
        for branch in tree:
            cnt+=count(branch)
        return cnt
        return sum( [count(branch) for branch in tree])
        

    













