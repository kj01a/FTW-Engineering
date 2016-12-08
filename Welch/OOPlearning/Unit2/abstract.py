"""
Abstract class: A class that is a blueprint for how child classes should be
designed.

Abstract classes are not meant to be instaniated. They are blueprints for child
classes, defining an interface.

A child class that inherits from an abstract class will have to implement the
methods from the parent class.

In the example below. The GetterSetter class is an abstract class, and MyClass is
a child class to GetterSetter. This means that MyClass has to implement set_val
and get_val or python will throw an error.

The abc module provides facilites for creating abstract classes. One way to do
is __metaclass__. Basically a __metaclass__ is a class that can define another
class (most info on this is above the level of this class). Basically this is
how you define the parent class as an abstract class.
"""

import abc

class GetterSetter(object):
	__metaclass__ = abc.ABCMeta #Define GetterSetter as an abstract class

	@abc.abstractmethod #Set methods as abstract methods
	def set_val(self, input):
		#Set a value in the instance
		return

	@abc.abstractmethod
	def get_val(self):
		#Geta and return a value from the instance
		return

class MyClass(GetterSetter):

	def set_val(self, input):
		#Changing the name of set_val (e.g. set_vals) would cause this class not
		#to instanciate.
		#TypeError: Can't instanciate abstract class MyClass with abstract methods set_val
		self.val = input

	def get_val(self):
		return self.val

x = MyClass()
y = GetterSetter() #TypeError: Can't instanciate abstract Class GetterSetter with abstract methods get_val, set_val
print x
