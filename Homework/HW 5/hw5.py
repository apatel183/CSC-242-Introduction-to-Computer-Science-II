#hw5##
####Arpan Patel## 

##Question1###

def pascalLine(number):
    pascalstart=1
    newline =[pascalstart]

    if number == 0:
        return newline
    else:
        for i in range(number):
            pascalstart =(pascalstart)*(number-i)*(1/(i+1))
            newline.append(int(pascalstart))
    return newline

#TEST
'''
>>> pascalLine(0)
[1]
>>> pascalLine(1)
[1, 1]
>>> pascalLine(2)
[1, 2, 1]
>>> pascalLine(3)
[1, 3, 3, 1]
>>> pascalLine(4)
[1, 4, 6, 4, 1]
>>> pascalLine(7)
[1, 7, 21, 35, 35, 21, 7, 1]
'''

##Question 2###

def levy(number):
    if number==0:
        return 'F'
    else:
        l=levy(number-1)
        return 'L' + l + 'RR' + l + 'L'
#TEST
'''
>>> levy(0)
'F'
>>> levy(1)
'LFRRFL'
>>> levy(2)
'LLFRRFLRRLFRRFLL'
>>> levy(3)
'LLLFRRFLRRLFRRFLLRRLLFRRFLRRLFRRFLLL'
>>>
'''

#Question3##

def base(number,numbase):
    if number%numbase == number:
        return str(number)
    else:
        return base(number//numbase,numbase) + base(number%numbase,numbase)
#TEST
'''
>>> base(0,3)  # write 0 in base 3
'0'
>>> base(5,3)  # write 5 in base 3  
'12'
>>> base(887,7)  # write 887 in base 7
'2405'
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw5TEST.py') )
