####hw2.py###
###Arpan Patel###

####Question 1 ###

class Pizza():

    def __init__(self, size='M', tops=set()):
        self.setsize=size
        self.settopp=set(tops)

    def __repr__(self):
        return "Pizza('{}',{})".format(self.setsize,self.settopp)

    def setSize(self,size):
        self.setsize=size
        
    def getSize(self):
        return self.setsize

    def addTopping(self,tops):
        self.settopp.add(tops)

    def removeTopping(self,tops):
        self.settopp.remove(tops)

#TEST
'''
>>> pie = Pizza()
>>> pie
Pizza('M',set())
>>> pie.setSize('L')
>>> pie.getSize()
'L'
>>> pie.addTopping('pepperoni')
>>> pie.addTopping('anchovies')
>>> pie.addTopping('mushrooms')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.addTopping('pepperoni')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.removeTopping('anchovies')
>>> pie
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie.price()
16.65
>>> pie2 = Pizza('L',{'mushrooms','pepperoni'})
>>> pie2
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie==pie2
True
'''
    def price(self):
        if self.setsize== 'S':
            return 6.25 + (0.70 * len(self.settopp))
        elif  self.setsize== 'M':
            return 9.95 + (1.45 * len(self.settopp))
        else:
            return 12.95 + (1.85 * len(self.settopp))
        
    def __eq__(self,other):
        return (self.setsize == other.setsize) and (self.settopp - other.settopp == set())


####Question 2####
    
def orderPizza():
    print('Welcome to Python Pizza!')
    Choosesize= input('What size pizza would you like (S,M,L): ')
    setchoice= Pizza(Choosesize, set())
    while True:
          typetop= input('Type topping to add (or Enter to quit): ')
          if typetop == '':
              break
          else:
              setchoice.addTopping(typetop)
    print('Thanks for ordering!')
    print('Your pizza costs $' + str(setchoice.price()))
   #print (setchoice)
    return setchoice

#TEST
'''
>>> pie = Pizza()
>>> pie
Pizza('M',set())
>>> pie.setSize('L')
>>> pie.getSize()
'L'
>>> pie.addTopping('pepperoni')
>>> pie.addTopping('anchovies')
>>> pie.addTopping('mushrooms')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.addTopping('pepperoni')
>>> pie
Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
>>> pie.removeTopping('anchovies')
>>> pie
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie.price()
16.65
>>> pie2 = Pizza('L',{'mushrooms','pepperoni'})
>>> pie2
Pizza('L',{'mushrooms', 'pepperoni'})
>>> pie==pie2
True
'''
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw2TEST.py'))

