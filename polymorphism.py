"""
	Polymorphism: Two classes with methods of the same name, 'the same interface'.
	Used for methods that are conceptually similar but with different implementation
	
	In the example below, if you know every animal can show_affection, it doesn't matter what kind of animal it is. 
	You are able to call show_affection on any animal object and know that it will work, regardless of what show_affection
	actually does for a paticular object. 
	
	Duck Typing: Reading an objects attributes to decide whether it is of a proper type, rather than check the type directly
		'If it walks like a duck, quacks like a duck, it must be a duck.'
		We don't what kind of Animal is called, we trust the interface contract
		Checking the type beforehand is considered un-pythonic. 
		We deal with expections as they come up.  --Discussed later. 
		
	Python has native functions that are polymorhic. 
		len("hello") #5
		len('1', '2', '3') #3
		len(('1', '2', '3')) #3
		len({'a' : 1, 'b' : 2}) #2
	The len() function is that works like a built in function. This is just an easy way to write them. They are translated
	into a method call. 
		x = "hello"
		
		len(x) # 5
		x.__len__() # 5
		
	Objects, like strings, have built in attributes and operators like any other objects. dir(x) with list all methods
	callable for that data type. len() uses just a bit of magic to call the __len__() method. Because len() can be called on
	different objects, lists, tuples, etc... This means those object also have a __len__() attribute. Polymorphism!
"""

class Animal(object):
	def __init__(self, name):
		self.name = name
		
	def eat(self, food):
		print "{0} eats {1}".format(self.name, food)
	
class Dog(Animal):
	def fetch(self, thing):
		print "{0} goes after the {1}".format(self.name, thing)
		
	def show_affection(self):
		#This function is polymorphized with the Cat method of the same name. 
		print "{0} wags tail".format(self.name)
	
class Cat(Animal):
	def swatstring(self):
		print "{0} shreds the string!".format(self.name)
		
	def show_affection(self):
		#This function is polymorphized with the Dog method of the same name. 
		print "{0} purrs".format(self.name)
		
for a in (Dog("Rover"), Cat("Fluffy"), Cat("Precious"), Dog("Scout")): a.show_affection()
	#Rover wags tail
	#Fluffy purrs
	#Precious purrs
	#Scout wags tail