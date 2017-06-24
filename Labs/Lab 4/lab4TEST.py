# lab4TEST.py

>>> from lab4 import *

##### Mapping #####

>>> m = Mapping()
>>> m[1]=2
>>> m==Mapping({1: 2, 2: 1})
True
>>> m[1]
2
>>> m[2]
1
>>> m[3]=4
>>> m == Mapping({1: 2, 2: 1, 3: 4, 4: 3})
True
>>> m[5]=5
>>> m==Mapping({1: 2, 2: 1, 3: 4, 4: 3, 5: 5})
True
>>> m[5]
5
>>> m == eval( str(m))   # test __repr__
True
>>> m.pop(1)
>>> m==Mapping({3: 4, 4: 3, 5: 5})
True
>>> m.pop(5)
>>> m==Mapping({3: 4, 4: 3})
True
>>> m = Mapping( {1:2,2:3,4:4})
>>> m == Mapping({2: 3, 3: 2, 4: 4})
True
