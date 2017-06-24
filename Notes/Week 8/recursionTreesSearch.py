# recursionTreesSearch.py

# week 8 - recursion
# week 9 - web crawling, scraping
# week 10 - review, go over midterm
# week 11 - final
#           March 17, 2016, from 8:30 AM to 10:45 AM

##### hw q's #####

# pascalLine
'''
>>> pascalLine(0)
[1]
>>> pascalLine(1)
[1,1]
>>> pascalLine(2)
[1,2,1]
>>> pascalLine(3)
[1,3,3,1]

suppose we want to compute answer for n=5

0) get previous, recursively, i.e. pascalLine(4)
   [1,4,6,4,1]
1) make new list [1]
2) iterate over successive pairs
   of previous one (1,4), (4,6), (6,4), (4,1)
   take sum of each pair and add it to the list
3) add a final 1 to the list
4) return the answer

   

'''


# base - general

'''

base(n,b)

>>> base(3,5)
'3'
>>> base(5,5)
'10'
>>> base(42,8)
'52'


>>> base(887,7)
'2403'

'240' = base(887//7,7)
'3'   = base(887%7,7) = 887%7



'''

# patt

'''
>>> patt(1)
1
>>> patt(2)
22
 1
 1
>>> patt(3)   = patt(3,0)
333   - print 0 spaces, 3 3's
 22
  1   - patt(2,1)
  1
 22
  1   - patt(2,1)
  1
>>> patt(3,2)   
  333   - print 2 spaces, 3 3's
   22
    1   - patt(2,2+1)
    1
   22
    1   - patt(2,2+1)
    1
>>> patt(4)
4444
 333
  22
   1
   1
  22
   1
   1
 333
  22
   1
   1
  22
   1
   1

add a paramter, an indentation value
>>> patt(2,3)
   22
    1
    1

>>> patt(n,t)
print t spaces, n n's
patt(n-1,t+1)
patt(n-1,t+1)

'''

def patt(n,t=0):

    if n>0:
        print( t*' '+n*str(n))
        patt(n-1,t+1)
        patt(n-1,t+1)

'''
actually of use when printing
file/folder structure

root
    folder1
        file1
        file2
        file3
    folder2
        file1
        file2
    file1
    file2
'''

##### trees #####

'''
algorithm to count leaves on a tree

    iterate over branches
    get the count for each branch (recursive)
    total the counts

'''

# arbitrarily nested list

numsTree = [1,2,[3,[4,5]],6,[[7,[[8]]],9]]

# branch - list
# leaf - a number

def traverse( tree,indent=0 ):
    ''' print all items in arbitrarily nested list '''
    if type(tree)!=list:  # i.e. its a number, a lead
        print( indent*'  ',tree )
    else: # its a list
        for branch in tree:
            traverse( branch,indent+1 )
        

def total( tree ):
    ''' return the total of all numbers in an
arbitrarily nested list '''
    if type(tree)!=list:  # tree is a number
        return tree
    else: # is a list
        tot = 0
        for branch in tree:
            tot+=total(branch)
        return tot


'''
make this work:
>>> flatten( numsTree )
[1,2,3,4,5,6,7,8,9]
>>> flatten( [2,3,4] )
[2,3,4]
>>> flatten( 3 )
[3]
'''

def flatten( tree ):
    ''' return flattened (1-diml) version of a tree '''
    if type(tree)!=list:  # base case, a leaf
        return [tree]
    else: # is a list
        lst = []
        for branch in tree:
            # bad - lst.append( flatten( branch ) )
            # fine: lst += flatten(branch)
            lst.extend( flatten(branch) )
        return lst
    
##### folders/files #####
        
# download test.zip
# and extract it in same folder as this module

# use os module

import os

def printFiles( path ):
    ''' recursively print all filenames in path '''

    try: # to treat path as folder
        for item in os.listdir( path ):
            # build absolute pathname
            fullpath = os.path.join( path, item)
            printFiles( fullpath )
    except NotADirectoryError:  # whoops, path is a file
        print( path )

'''
>>> printFiles('test')
test\test\fileA.txt
test\test\folder1\fileB.txt
test\test\folder1\fileC.txt
test\test\folder1\folder11\fileD.txt
test\test\folder2\fileD.txt
test\test\folder2\fileE.txt
>>> 
'''

def search( path, target ):
    ''' recursively search all files in path and
print all those that contain the text target '''
    try: # to treat path as folder
        for item in os.listdir( path ):
            # build absolute pathname
            fullpath = os.path.join( path, item)
            search( fullpath, target )
    except NotADirectoryError:  # whoops, path is a file
        if target in open(path).read():
            print( path )

def getFiles( path, target ):
    ''' recursively search all files in path and
return a list of all those that contain the text target '''
    try: # to treat path as folder
        ans = []
        for item in os.listdir( path ):
            # build absolute pathname
            fullpath = os.path.join( path, item)
            ans+=getFiles( fullpath, target )
        return ans
    except NotADirectoryError:  # whoops, path is a file
        if target in open(path).read():
            return [path]
        else:
            return []

'''
>>> getFiles( 'test','ye8009')
['test\\test\\fileA.txt', 'test\\test\\folder1\\fileB.txt']
>>> getFiles( 'test','ye8009kjkhkjh')
[]
>>> getFiles( 'test','')
['test\\test\\fileA.txt', 'test\\test\\folder1\\fileB.txt', 'test\\test\\folder1\\fileC.txt', 'test\\test\\folder1\\folder11\\fileD.txt', 'test\\test\\folder2\\fileD.txt', 'test\\test\\folder2\\fileE.txt']
>>> 
'''

import random
n = 1000000
lst = random.sample( range(2*n), n)
lst.sort()

# iterative search
def isearch( target, lst ):
    for i in range(len(lst)):
        if lst[i]==target:
            return i
    return -1 # not found

def bsearch(target,lst,i=0,j=None):
    ''' return index of target in SORTED
list lst[i:j], or, -1 if not found '''

    if j==None:
        j = len(lst)
    if i==j:
        return None
    # check item at the middle of window [i:j]
    m = (i+j)//2
    if lst[m]==target:
        return m
    elif target<lst[m]:  # look in left half
        return bsearch(target,lst,i,m)
    else: # right half
        return bsearch(target,lst,m+1,j)
        
    































