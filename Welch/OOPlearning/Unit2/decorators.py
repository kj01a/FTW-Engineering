"""
	The type of methods used up to this point are instance methods. They are meant to be used on the instance itself. In the
	original InstanceCounter get_count worked as an instance method. Which works, but it more logically consistent to 
	classify get_count as a class method. This helps keep the code maintainable and understanble. 
"""


class InstanceCount(object):
	count = 0
	
	def __init__(self, val):
		self.val = val
		InstanceCount.count += 1
		
	def set_val(self, newval):
		self.val = newval
		
	def get_val(self):
		return self.val
	
	@classmethod #class function decorator
	def get_count(cls):
		return cls.count
		
a = InstanceCount(5)
b = InstanceCount(13)
c = InstanceCount(17)

for obj in (a, b, c):
	print "val = %s" % obj.get_val()
	print obj.get_count()
	
"""
	The other kind of decorator is s@staticmethod. filterint() is not a class method or an instance method (note that 
	self is not passed). It works neither with the class data or instance data. It simply does somthing useful. Again if 
	it just a utility method that does not need the instance to work, we should not imply that it does. 
"""

class InstanceCount(object):
	count = 0
	
	def __init__(self, val):
		self.val = self.filterint(val)
		InstanceCount.count += 1
		
	@staticmethod #static function decorator
	def filterin(value):
	#This is a cool little gate for checking to make sure a value is an integer. 
		if not isinstance(value, int):
			return 0
		else:
			return value

a = InstanceCount(5)
b = InstanceCount(13)
c = InstanceCount(17)

print a.val
print b.val 
print c.val 

"""
	A lot of OOP seems very abstract and built more out of convention to maintain readablility than any need inheirnet in 
	the paradign. Just an observation. 
"""