myset to be our version of set
doent have duplicate items
un-ordered in general

>>> m = myset()
>>> m
myset([])
>>> m.add(4)
>>> m.add(3)
>>> m.add(3)
>>> m == myset([3,4])
True
>>> m.remove(3)
>>> m == myset([4])
True

>>> m = myset([2,3,4,4,4,5])
>>> m==myset([5,4,3,2])
True
>>> 4 in m
True
>>> 7 in m
False

comparisons:
>>> mm = myset([3,5])
>>> mm<m   # proper subset
True
>>> mm < myset([5,3])
False   # not a PROPER subset
>>> mm <= myset([5,3])
True

>>> mm.intersection( myset([5,7,9]))==myset([5])
True
>>> mm.union( myset([5,7,9]))==myset([3,5,7,9])
True








