"""
    This code is showing examples of what inheritance can do.
        Inherit: Use the parnet class method
        Override/overload: Provider child class's own version of the parent class
        method
        Extend: do things in addtion to the parent method
        Provide: implement abstract method that the parent requires

    In the example below:
        GetSetParent is an object class from which multiple class inherit from
        Those child classes will have the option of behaving as GetSetParent is
        designed to do, or modifying the methods in GetSetParent depending on it's
        own requirements. 
        This makes GetSetParent both a contract (quite explicitly in the case of
        showdoc) or a library to allow children to craft their own behavior.

"""

import abc #Allows the use of an abstract method

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta #set GetSetParent as a meta class
                                #Disallows GetSetParent to be instanciated

    def __init__(self, value):
        self.val = 0

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val

    @abc.abstractmethod #Again showdoc will be required in each child class
    def showdoc(self):
        return

class GetSetInt(GetSetParent):

    def set_val(self, value):
        if not isinstance(value, int):
            return 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print "GetSetInt object ({0}), only "
            "accepts integer values".format(id(self))

class GetSetList(GetSetParent):
    def __init__(self, value=0): #You can set the value in the paramenter!!
        self.vallist = [value]

    def get_val(self):
        return self.vallist(-1)

    def get_vals(self):
        return self.vallist

    def set_val(self, value):
        self.vallist.append(value)

    def showdoc(self):
        print "GetSetList object, len {0}, stores history
            "of values set.".format(len(self.vallist))

x = GetSetInt(3)
x.set_val(5)
print x.get_val()
x.showdoc()
