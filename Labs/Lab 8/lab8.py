##lab8.py##
##Arpan Patel## 


##Question 1##

def printPattern(n,defaults=0):
    if n>0:
        printPattern(n//2,defaults)
        print(defaults*' '+n*'*')
        printPattern(n//2,defaults+(n//2))
#TEST
'''
>>> printPattern(8,0)
*	
**
 *
****
  *
  **
   *
********
    *
    **
     *
    ****
      *
      **
       *
>>> printPattern(4,2)
  *
  **
   *
  ****
    *
    **
     *
>>> printPattern(4)
*
**
 *
****
  *
  **
   *
'''

#Question 2###

def gcd(m,n):
    if n==0:
        return m
    else:
        return gcd(n,m%n)
#TEST
'''
>>> gcd(5,0)
5
>>> gcd(15,5)
5
>>> gcd(5,7)
1
>>> gcd(24,144)
24
>>> gcd(124,144)
4
>>>
'''

#Question 3##

def count(lst,target):

    if type(lst)!=list:
        if lst==target:
            return 1
        else:
            return 0
    else:
        total=0
        for i in lst:
            total += count(i,target)
        return total
#TEST
'''
>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 1 )
2
>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 5 )
4
>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 0 )
0
'''

    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py') )
