##lab10.py###
######ARPAN PATEL###

#Question1##

def maximum(numberlst):
    if type(numberlst) != list:
        return numberlst
    else:
        biggestnumber=[]
        for branch in numberlst:
            if type(branch) == list:
                biggestnumber.append(maximum(branch))
            else:
                biggestnumber.append(branch)
        return max(biggestnumber)

'''
>>> maximum( 7 )
7
>>> maximum( [7,8] )
8
>>> maximum( [7,8,[9,10],[[11,[12]],13]] )
13
>>>
'''
###Question 2###

def printstack(number,t=0):
    if number>0:
        printstack(number-1,t+1)
        print(' '*t + 'U ' * number)
#TEST
'''
>>> printstack(1)
U
>>> printstack(2)
 U
U U 
>>> printstack(3)
  U
 U U 
U U U 
>>> printstack(6)
     U
    U U 
   U U U 
  U U U U 
 U U U U U 
U U U U U U 
>>> printstack(3,2)
    U
   U U 
  U U U 
>>>
'''

if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab10TEST.py'))
