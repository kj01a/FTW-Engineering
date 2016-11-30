"""
	MaxSizeList as a module should create a list given the arguments of of push and return
	the list with a number of entires equal to the instance argument. If the list size 
	exceeds the max size take off the entry in the first position. Output should match 
	lines 24 & 25.
"""


from assignments import MaxSizeList

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")

b.push("what")
b.push("up")
b.push("broseph")
b.push("stalin")

print a.get_list()  #["ho", "let's", "go"]
print b.get_list()  #["stalin"]