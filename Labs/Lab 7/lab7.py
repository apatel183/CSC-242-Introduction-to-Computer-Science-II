##lab7.py##
##Arpan Patel##

##Question 1##
def silly(n):

    if n<=0:
        pass
    else:
        print('*', end='')
        silly(n-1)
        print('!', end='')
#TEST
'''
>>> silly(0)
>>> silly(1)
*!
>>> silly(2)
**!!
>>> silly(3)
***!!!
>>> silly(10)
**********!!!!!!!!!!
>>>
'''

##Question 2###
def stars(n):

    if n == 0:
        pass
    else:
        stars(n-1)
        print(n*'*')
        stars(n-1)
#TEST
'''
>>> stars(1)
*
>>> stars(2)
*
**
*
>>> stars(3)
*
**
*
***
*
**
*
'''
##Question 3###
def pattern(n):
    if n<=0:
        pass
    else:
        pattern(n//2)
        pattern(n//2)
        print(n,end='')
   
#TEST
'''
>>> pattern(1)
1
>>> pattern(2)
112
>>> pattern(4)
1121124
>>> pattern(8)
112112411211248
'''    

        
if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab7TEST.py'))
