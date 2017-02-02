"""
    With is a built in feature allows for more easy clean up. In the example below
    it closes the open file automatically.
    It is good practice to close files as soon as possible.
"""

with open('filename.txt') as fh:
    for line in fh:
        line = line.rstrip()
        print(line)

fh = open('filename.txt')
for line in fh:
    print(line)
fh.close()

"""
    In this example __enter__() is called when with in invoked, sayhi() is called
    in the body of the with block of code, and __exit()__ is called at the end of
    the block.

    with can also be used to catch exceptions if an exception occurs in the with
    code block the __exit__() would pretty out the information of the exception.
"""

class MyClass(object):
    def __enter__(self):
        print("Entered 'with'"):
        return self

    def __exit__(self, type, value, traceback): #args are required
        print("Leaving 'with'"):
        print("error type: {0}".format(type))
        print("error value: {0}".format(value))
        print("error traceback: {0}".format(traceback))

    def sayhi(self):
        print("hi, instance %s" $(id(self)))

with MyClass() as cc:
    cc.sayhi()
