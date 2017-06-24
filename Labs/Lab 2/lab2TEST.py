>>> from lab2 import *

##### Animal #####

TEST constructors, __repr__ and set methods

>>> a = Animal()
>>> a
Animal('default','default',0)
>>> a.speak()
I am a 0 year-old default and I default.
>>> a.setSpecies('tiger')
>>> a.setLanguage('growl')
>>> a.setAge(8)
>>> a
Animal('tiger','growl',8)
>>> a.speak()
I am a 8 year-old tiger and I growl.
>>> b = Animal('jackalope','can imitate anything',33)
>>> b
Animal('jackalope','can imitate anything',33)
>>> b.speak()
I am a 33 year-old jackalope and I can imitate anything.
>>> [b.speak()]   # make sure print not return
I am a 33 year-old jackalope and I can imitate anything.
[None]

TEST for __repr__
note that there should be __repr__
should produce quotes around
the species and language but not the age

>>> eval(str(a))
Animal('tiger','growl',8)
>>> eval(str(b))
Animal('jackalope','can imitate anything',33)


##### processAnimals #####

>>> processAnimals( 'animals.txt' )
I am a 8 year-old cat and I meow.
I am a 22 year-old dog and I bark.
I am a 2 year-old bat and I use sonar.
[Animal('cat','meow',8), Animal('dog','bark',22), Animal('bat','use sonar',2)]
>>> processAnimals('animals.txt')
I am a 8 year-old cat and I meow.
I am a 22 year-old dog and I bark.
I am a 2 year-old bat and I use sonar.
[Animal('cat','meow',8), Animal('dog','bark',22), Animal('bat','use sonar',2)]
>>> 
