# hw1TEST.py

>>> from hw1 import *   # import code, file must be named hw1

##### BankAccount ######

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


###### processAccount ######

# able to manipulate accounts

>>> processAccount('acct1.txt')
BankAccount(605.5500000000001)
>>> b = processAccount('acct1.txt')
>>> b
BankAccount(605.5500000000001)
>>> b.balance()
605.5500000000001


>>> b = processAccount('acct2.txt')
>>> b
BankAccount(46.94)
>>> b.balance()
46.94


>>> b = processAccount('acct3.txt')
>>> b
BankAccount(216.64)
>>> b.balance()
216.64

# checks on the code

now, run some checks on the code
in the file, make sure it is using a
BankAccount object and methods
and not doing + and -
also make sure there is a return statement and no print


>>> import inspect
>>> 
>>> 
>>> code = inspect.getsource(processAccount)
>>> 'BankAccount' in code
True
>>> '.deposit' in code
True
>>> '.withdraw' in code
True
>>> '+' in code or '-' in code
False
>>> 'return' in code
True


