class InstanceCounter(object):
	count = 0 #class attribute
	
	def __init__(self, val):
		self.val = val #instance attribute, call it here
		InstanceCounter.count += 1 #object.attribute syntax (dot notation)
		
	def set_val(self, newval):
		#setter method, but why is it here?? Taking this out does nothing. My guess is this 
		#is for changing object attributes at the instance level. Encapsulation and all that...
		self.val = newval #instance attribute, set it here
		
	def get_val(self):
		#getter method
		return self.val
		
	def get_count(self):
		return InstanceCounter.count
		
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
	print "value of object = %s" % (obj.get_val()) #5, 13, 17
	#obj.get_count() can also be written as obj.count which would take the count from the class
	#attribute directly.
	print "count is: %s " % (obj.get_count()) #3, 3, 3
	
	
"""
	WORKING WITH CLASS AND INSTANCE DATA
	Classes are objects (everything in python are objects)
		Classes have their own attributes. 
		When you give classes attributes the dir(Class) will include the set of native attributes as well
		as the attribute you give it. 
		
	object.attribute syntax is how you access class attritubes, and is how you differential from 
	global variables
	
	The last print statment confused me. At first glance it looks like it should print 1, 2, 3 for
	each iteration of the for loop, but it prints 3 every time. This is because count is incremented
	in the __init__ method, and __init__ is called upon creation of the instance. This means that 
	count is incremented on line 20, 21, & 22, and its value is 3 thereafter. 
"""
