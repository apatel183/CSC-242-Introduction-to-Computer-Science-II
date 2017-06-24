###Arpan Patel###
####lab4.py####

#Question 1#

class Mapping(dict):

    def __init__(self,dictionary=0):
        if dictionary:
            for key in dictionary:
                self[key] = dictionary[key]

    def __repr__(self):
        return "Mapping({})".format(dict.__repr__(self))


    def pop(self,key):
        dict.pop(self,self[key])
        if key in self:
            dict.pop(self,key)

    def __setitem__(self, key1, key2):
        for key in key1,key2:
            if key in self:
                self.pop(key)
        dict.__setitem__(self,key1,key2)
        dict.__setitem__(self,key2,key1)
        
           
#TEST
'''
>>> m = Mapping()
>>> m[1]=2
>>> m
Mapping({1: 2, 2: 1})
>>> m[1]
2
>>> m[2]
1
>>> m[3]=4
>>> m
Mapping({1: 2, 2: 1, 3: 4, 4: 3})
>>> m[5]=5
>>> m
Mapping({1: 2, 2: 1, 3: 4, 4: 3, 5: 5})
>>> m[5]
5
>>> m.pop(1)
>>> m
Mapping({3: 4, 4: 3, 5: 5})
>>> m.pop(5)
>>> m
Mapping({3: 4, 4: 3})
>>> m = Mapping( {1:2,2:3,4:4})
>>> m
Mapping({2: 3, 3: 2, 4: 4})
>>>
'''
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab4TEST.py') ) 
