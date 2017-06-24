####Arpan Patel###
####hw1.py


###Question 1 ####

class BankAccount:
    def __init__(self,balance=0):
        self.bal= balance

    def __repr__(self):
        return 'BankAccount({})'.format(self.bal)

    def setbalance(self, balance):
        self.bal= balance

    def withdraw(self, amount):
        self.bal -=amount

    def deposit(self, amount):
        self.bal += amount

    def balance(self):
        return (self.bal)
#TEST
'''
# constructor/repr

>>> b = BankAccount(100)
>>> b
BankAccount(100)
>>> b = BankAccount()
>>> b
BankAccount(0)
>>> [b] # check that str is returned, not printed
[BankAccount(0)]

# methods

>>> b.deposit(50.25)
>>> b
BankAccount(50.25)
>>> b.withdraw(17.50)
>>> b
BankAccount(32.75)
>>> b.balance()
32.75
>>> b.balance()==32.75 # check balance is returned, not printed
True 
'''

###Question 2####

def processAccount(filename):
    infile=open(filename).readlines()
    accountbal=BankAccount()
    for line in infile:
        txt=line.strip("\n").lower().split()
        if txt[0]=='d':
            accountbal.deposit(eval(txt[1]))
        elif txt[0] =='w':
            accountbal.withdraw(eval(txt[1]))
        else:
            accountbal.setbalance(eval(txt[0]))
    return accountbal

#TEST
'''
>>> processAccount('acct1.txt')
BankAccount(605.5500000000001)
>>> b = processAccount('acct1.txt')
>>> b
BankAccount(605.5500000000001)
>>> b.balance()
605.5500000000001
>>>
>>> b = processAccount('acct2.txt')
>>> b
BankAccount(46.94)
>>> b.balance()
46.94
>>>
>>> b = processAccount('acct3.txt')
>>> b
BankAccount(216.64)
>>> b.balance()
216.64
>>>
'''
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py') )
