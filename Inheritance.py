class Date(object):
#Parent class
	def get_date(self):
		return "2014-10-13"

class Time(Date):
#Child class, takes parnet class as argument
	def get_time(self):
		return "08:13:07"
		
dt = Date()
#Instance of the Date class. It only has access to Date attributes
print dt.get_date()

tm = Time()
#Instance of the Time class. Because it is a child of the Date class it 'inherits' the 
#attributes of its parnet.
print tm.get_time()
print tm.get_date() #Thus enabling tm to access the get_date method. 






"""
	Inheritance: the mechanism for on class to access the attributes of another class
		-Essentially it is an added level of attribute lookup.
		
		Object.attribute lookup hierarchy
			1. Instance
			2. Class
			3. Inherited class
		
		The inheriting class is called the child class
		The inherited class is called the parent class
"""


#The classic example!
class Animal(object):
	#These are the attibutes all animals have.
	#All animals have names, and all animals are able to eat. 
	def __init__(self, name):
		self.name = name
		
	def eat(self, food):
		print "%s is eating %s." % (self.name, food)
		
class Dog(Animal):
	def fetch(self, thing):
		#fetch is a Dog specific trait
		print "%s goes after the %s" % (self.name, thing)
		
class Cat(Animal):
	def swatsting(self):
		#swatsting is a Cat specific trait
		print "%s shreads the string" % (self.name)
		
d = Dog("Rover")
c = Cat("Fluffy")

d.fetch("paper")
c.swatsting()
d.eat("dog food") #Rover can eat because it is a Dog and Dogs are Animals
c.eat("cat food") #Same with Cats. Cats are animals
d.swatstring()	#Rover is not able to swatsting, because it is not a Cat.
				#Should throw an AttributeError

		
	