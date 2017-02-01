"""
    Classes can inherit from python's built-in classes. In the code below, MyDict
    inherits from the dict class-the class that builds dictionaries. It is able
    modify python's magic function like it it does with __setitem__(). But there
    is a danger! Using the dictionary operator will result in a recursion error.
    Because the operator access the child class before the parent.
"""
class MyDict(dict):
    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        #self[key] = val causes recursion error
dd = MyDict()s

dd['a'] = 5
dd['b'] = 6


"""
    MyList a child of list. It uses subclassing princples to modify the
    __getitem__() and __setitem__() methods that are part of the parent class. 
"""

class MyList(list):
    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0: raise IndexError
        if index > 0: index = index - 1
        list.__setitem__(self, index, value)

x = MyList(['a', 'b', 'c'])

x.append('spam')

print(x[1])
print(x[4])
