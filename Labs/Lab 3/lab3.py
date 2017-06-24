###lab3.py###
###Arpan Patel###


class Stack():
    
    def __init__(self, lst=None):
        if lst==None:
            self.s = list()
        else:
            self.s = lst

    def __repr__(self):
        return 'Stack({})'.format(self.s)

    def push(self,item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return self.s == []
    
    def __len__(self):
        return len(self.s)
    
    def __getitem__(self,index):
        return self.s[index]
#TEST
'''
>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s.push('pear')
>>> s.push('kiwi')
>>> s
Stack(['apple', 'pear', 'kiwi'])
>>> top = s.pop()
>>> top
'kiwi'
>>> s
Stack(['apple', 'pear'])
>>> len(s)
2
>>> s.isEmpty()
False
>>> s.pop()
'pear'
>>> s.pop()
'apple'
>>> s.isEmpty()
True
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s[0]
'apple'
>>> 
'''

    
def parenthesesMatch(characters):
    emptystack= []
    pushS, popS = "<({[",">)}]"
    for marks in characters:
        if marks in pushS:
            emptystack.append(marks)
        elif marks in popS:
            if not len(emptystack):
                return False
            else:
                sTop = emptystack.pop()
                emarks = pushS[popS.index(marks)]
                if sTop != emarks:
                    return False 
        else:
            return False
    return not len(emptystack)

#TEST
'''
>>> parenthesesMatch('(){}[]')
True
>>> parenthesesMatch('{[()]}')
True
>>> parenthesesMatch('((())){[()]}')
True
>>> parenthesesMatch('(}')
False
>>> parenthesesMatch('({])')
False
>>> parenthesesMatch('((())')
False
>>> parenthesesMatch('(()))')
False
'''

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab3TEST.py') )    
    
