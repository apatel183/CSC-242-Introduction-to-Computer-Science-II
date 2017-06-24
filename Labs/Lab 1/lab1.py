###lab1.py### 
###Arpan Patel###

#Question 1#

def printTwoLargest():
    lst = []
    finish = False
    while finish == False:
        number= eval(input('Please enter a number: '))
        if number > 0:
            lst.append(number)
        else:
            finish= True
            lst.sort()
            if len(lst) >=5:
                print('The largest is ' + str(lst[-1]))
                print('The second largest is ' + str(lst[-2]))
            elif len(lst) == 1:
                print('The largest is ' + str(lst[0]))
            else:
                print('No positive numbers were entered')
#TEST
'''
>>> printTwoLargest()
Please enter a number: 12
Please enter a number: 99.9
Please enter a number: 4.5
Please enter a number: 77
Please enter a number: 0
The largest is 99.9
The second largest is 77
>>> printTwoLargest()
Please enter a number: 23.2
Please enter a number: -99
The largest is 23.2
>>> printTwoLargest()
Please enter a number: -9
No positive numbers were entered
>>>
'''

#Question 2#

def printWordsLines(filename):

    content = open(filename).read()
    letters = open(filename).read().split()
    numword= 0
    for x in letters:
        numword += 1
    print('The file', filename, 'contains', numword, 'words and', len(open(filename).readlines()), 'lines.')

#TEST
'''
>>> printWordsLines('test1.txt')
The file test1.txt contains 17 words and 3 lines
>>> printWordsLines('test2.txt')
The file test2.txt contains 38 words and 5 lines
'''
##Question 3 #### 
    
def reverseDict(letters):
    return{letters[i]:i for i in letters}
#TEST
'''
>>> reverseDict( {'a':1,'b':2,'c':3})
{1: 'a', 2: 'b', 3: 'c'}
>>> reverseDict( {1:'apple', 2:'pear', 3:'orange'} )
{'orange': 3, 'apple': 1, 'pear': 2}
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab1TEST.py') )
