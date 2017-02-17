class MaxSizeList(object):
	#Sets max size of the list and creates a list for each instance
	def __init__(self, max):	
		self.max = max
		self.list = []
		
	def push(self, i):
		self.list.append(i)
		
		if len(self.list) > self.max:
			self.list.pop(0)
			
	def get_list(self):
		return self.list
