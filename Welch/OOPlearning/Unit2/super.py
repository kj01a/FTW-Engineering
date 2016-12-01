"""
	When a new instance is created normally it looks for the __init__ constructor in the class the instance was called on.
	If it does not find it there, it looks in the parent class. To combine specific __init__ fucntionality with general
	__init__ functionality, we use super()
	
	super() a built in function that acts as a pointer to the child class's parent class
	
	When using super() the effect is basically the same as Parent.__init__(), in the example below Animal.__init__(). 
	Which could be used directly, but we use super() to generalize the functionaility. That way if we decide to change
	the name of the parent class or if we decide to change the hierarchy structure of Dog, we don't have to change 
	the code in the Dog class. 
"""

import random

class Animal(object):
	def __init__(self, name):
		self.name = name

class Dog(Animal):
	def __init__(self, name):
		#The super function in this case is calling the __init__ of the Animal class. 
		#Because Animal is the parnet class to the Dog class
		super(Dog, self).__init__(name)
		self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])
		
	def fetch(self, thing):
		print "%s goes after the %s) % (self.name, thing)
		
d = Dog("Name")

print d.name
print d.breed