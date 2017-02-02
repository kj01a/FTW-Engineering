"""
    Encapsulation affords privacy to attribute.
    Python allows for attribute to be at any time in the instance, class, etc...
    This breaks encapsulation. One way around this is to use getter and setter,
    and ask the user to make use of those methods. This requires user cooperation.

    Python does not enforce privacy by design. Instead relying on user to do the
    right thing. Trusting the user is more pythonic!

    @property designates instance attribute as encapsuable. Let's user use
    attribute access instead of calling a method.

    Below: the decorators allow the methods to be used as attibutes, basically.
    This allows the actual class attribute (attrval) to be seperate from the the
    attribute the user uses. Calling attrval "var" would cause a recursion error.
"""

class GetSet(object):

    def __init__(self, value):
        self.attrval = value

    @property
    def var(self):
        return self.attrval #get var attribute

    @var.setter
    def var(self, value):
        self.attrval = value #set var attribute

    @var.deleter
    def var(self):
        self.attrval = None #del var attribute

x = GetSet(5)

print(x.var)

x.var = 1000 #calls the method with the @var.setter decorator

print(x.var)  #calls the mehhod with the @property decorator
del(x.var) #calls the method with the #var.deleter decorator 
print(x.var)
