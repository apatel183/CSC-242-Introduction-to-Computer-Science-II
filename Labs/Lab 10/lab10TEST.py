# lab9TEST.py

>>> from lab10 import *

##### maximum #####

>>> maximum( 7 )
7
>>> maximum( [7,8] )
8
>>> maximum( [7,8,[9,10],[[11,[12]],13]] )
13
>>> 
>>> exec('\nimport random\nrandom.seed(0)\ndef t(n):\n    if n==0:\n        return random.randrange(10)\n    elif random.randrange(2):\n        return [ random.randrange(10), t(n-1)]\n    else:\n        return [t(n-1),random.randrange(10),t(n-1)]\n')
>>> [ maximum(t(i)) for i in range(4)]
[6, 4, 7, 9]
>>> 


##### printstack #####

>>> printstack(1)
U 
>>> printstack(2)
 U 
U U 
>>> printstack(3)
  U 
 U U 
U U U 
>>> printstack(4)
   U 
  U U 
 U U U 
U U U U 
>>> printstack(4,3)
      U 
     U U 
    U U U 
   U U U U 
