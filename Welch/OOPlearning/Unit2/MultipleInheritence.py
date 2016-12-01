"""
	In python classes can inherit from more than one parent. And those parent classes can inherit from other classes. 
	
	Method Resolution Order (MRO): The order in which python looks through the inheritence tree to find the method it needs to 
	call when the class inherits multiple classes. 
	
	Python, by default, follows a 'depth first' lookup order. Meaning the mro will follow up to the top level parent in a
	tree before going to the next class the child inherits from.
	In the example below:
		the mro looks like this: D-B-A-C. When a method is called on an instance of D mro will look first in
		the D class, then in the B class because D inherits from B first. Then it will look in the A class because B inherits
		from A. If it has still not found the method it is looking for will it begin searching through the C class tree.
	
	mro() is a method that shows the lookup order for a particular class. 
"""


class A(object):
	def dothis(self):
		print "Doing A"
		
class B(A):
	pass
	
class C(object):
	def dothis(self):
		print "Doing C"
		
class D(B, C): #Syntax for multiple inheritence. 
	pass
	
d = D()
d.dothis() # "Doing A"

print D.mro() #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C', <type 'object>]


"""
	Diamond Inheritence: when a child class has multiple parent classes and those parent classes inherit from the same 
	grandparent class. 
	
	In the example below. 
		You would expect the mro to be D-B-A-C. Same as before. 
		But because C also inherits from A the mro looks like this: D-B-A-C-A. This is ambiguous! 
		Starting in python 2.3, python now deletes the eariler appearances of classes from the mro. The mro becomes: D-B-C-A.
			At first glances this looks like a 'breadth first' lookup, but understand that python is deleting the first
			appreance of the A class in the mro.
"""

class A(object):
	def dothis(self):
		print "doing A"
		
class B(A):
	pass
		
class C(A):
	def dothis(self):
		print "doing C"
		
class D(B, C):
	pass
	
d = D()

print d.mro() #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A', <type 'object>]

"""
	This mro is used for 'new style' classes. New Sytle classes inherit from an ancestor class (object) --Disscussed later
	
	
	I don't like multiple inheritence. I think I will avoid it at all costs!
"""
	
