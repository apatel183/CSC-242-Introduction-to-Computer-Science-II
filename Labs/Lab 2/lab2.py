####Arpan Patel###
####lab2.py#### 


#Question 1###

class Animal:
    def __init__(self, species='default', language='default', age=0):

        self.setspec = species
        self.setlan = language
        self.seta = age
        
    def __repr__(self):

        return "Animal('{}','{}',{})".format(self.setspec, self.setlan, self.seta)

    def setSpecies(self, species):

        self.setspec = species

    def setLanguage(self, language):

        self.setlan = language

    def setAge(self, age):

        self.seta = age

    def get(self):

        return (self.setspec,self.setlan,self.seta)

    def speak(self):
        
        print('I am a {} year-old {} and I {}.'.format(self.seta, self.setspec, self.setlan))

#TEST
'''
 
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
note that quotes should appear around
the species and language but not the age

>>> eval(str(a))
Animal('tiger','growl',8)
>>> eval(str(b))
Animal('jackalope','can imitate anything',33)
'''

def processAnimals(namefile):
    animalObjects = []
    file = open(namefile, 'r')
    for inLine in file:
        txt1=inLine.strip("\n").split(",")
        newAnimal = Animal(txt1[0], txt1[1],txt1[2])
        animalObjects.append(newAnimal)
        newAnimal.speak()
    file.close()

    return animalObjects
#TEST
'''
>>> processAnimals('animals.txt')
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
'''
    
    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab2TEST.py') )    

