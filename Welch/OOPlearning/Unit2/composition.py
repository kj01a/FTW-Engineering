"""
    Opponents of inheritance say it can be brittle. Brittle meaning that if you
    change one thing in one place you'll have to change many things in many places

    Decoupled code works independently. As long as the interface is maintaned the
    interactions between the classes will work. With fewer dependieces makes for
    more maintainable code.

    Not checking or requiring types is polymorphic and pythonic.

    In the example below: WriteMyStuff is an example of composition. The write()
    function can write to any input be a file or a database or a the web. Any
    class we create that interfaces with WriteMyStuff will not have to worry about
    changes itself affects WriteMyStuff.

    This example seems a little too simple to really illustrate what is going on,
    but I think I understand it better than I do inheritance. 
"""

import random
import StringIO

class WriteMyStuff(object):

        def __init__(self, writer): #__init__ accepts writer object
            self.writer = writer #argument becomes the object

        def write(self): #def calls write() on object in
            write_text = "This is a silly message"#The message that is written to the object
            self.writer.write(write_text) #Writes write_text to the write object

fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh) #instantiats fh as an WriteMyStuff object
w1.write() #calls WriteMyStuff.write()
fh.close() #closes file

sioh = StringIO.StringIO() #StringIO writes to a string the way it would to a file
w2 = WriteMyStuff(sioh)
w2.write()

print "file object: ", open('test.txt', 'r').read()
print "StringIO object: ", sioh.getvalue()
