import random

class Card(object):
#1
	def __init__(self, rank):
	#is called as instance is created. 
	#__init__ methods intialize the instance, ether by settings a variable
	#in the method, or setting an agrument
		print("calling init")
		#self.rank = "Ace"
		self.rank = rank
		
	def increment_rank(self):
		#self.rank = "Two"
		self.rank = "Two"
		
	value = "2 of Hearts"
	#This is an instance method. It is defined in the Class and accessed
	#through the instnace.
	#An instance method passes the instance itself as the first arguemnt
	#and that argument is called 'self'
	def card_value(self):
		print("Your card is the 2 of Hearts")
		
	def rand_card(self):
		self.rand_card = random.randint(1,10)
		
#2 ----------------------------------------------------------------------------------------------
class Attibutes(object):
	class_attribute = 10
	
	def set_val(self):
		self.instance_att = 100

class OrderLookup(object):
	attr = "from the class"

		
#1		
card = Card("Ace")
print card.rank		#Ace
card.increment_rank()		
print card.rank #Two


#2
dd = Attibutes()
dd. set_val()

print dd.class_attribute #10
print dd.instance_att	#100

#fyi this breaks in encapsulation
d = OrderLookup()
print d.attr #"from the class"

d.attr = "from the instance"
print d.attr #"from the instnace"

del d.attr #deletes instance attr
print d.attr #"from the class"

"""
1. Encapsulation
	Object:
		A unit of data of a particular class or type, with associted functionality
		-'Instance' and 'object' can be used interchanably.
		
	Self:
		The instance upon  which the method is called.
		
	Encapsulation:
		The safe storage of data in an instance
			Data should be accesed through the instance methods. 
			Data shoud validated as correct
			Data should be safe from changes to external processes
		Setter and Getter method implements encapsulation. 
		Integrity gates are good practice. And it is good practice to put integrity gates into
		the __init__ method.


2. Attibutes
	Attributes
		There are class attributes defined in the class, and instance attributes defined in the functions
		
		Attribute order look up: In python, attribute are modified first in the instance, then in class
	
	Class data is to be shared amoung all instances. 
	
3. Working with Class and Instance Data
	Classes are objects (everything in python are objects)
		Classes have their own attributes. 
		When you give classes attributes the dir(Class) will include the set of native attributes as well as the attribute you give it. '
		
	
"""
