make this work:

>>> from queues import *
    
>>> q = Queue()
>>> q.enqueue( 'Mary' )
>>> q.enqueue( 'Fred' )
>>> q.enqueue( 'Alice')
>>> q
Queue(['Mary', 'Fred', 'Alice'])
>>> nowserving=q.dequeue()
>>> nowserving   # FIFO - first in first out
'Mary'
>>> q[1]   # Queue.__getitem__
'Alice'
>>> qq = Queue( [1,2,3] )
>>> qq
Queue([1, 2, 3])
>>> len( qq )
3
>>> [ item for item in qq]
[1, 2, 3]
>>> q[1]=77
...
CuttingError: no cutting in line jerk
>>> 
