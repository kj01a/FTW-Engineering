"""
    1 + 2 == 1.__add__(2)
    The __add__() function is a method attribute of the integer class. When
    python sees the plus sign it knows to run the first statment as the second
    statment.

    These are the magic attributtes. They are called implicitly and not directly
    by us.

    As shown in the code below, these magic methods can be modified to fit needs.

"""
class SumList(object):
    def __init__(self, this_list):
        self.mylist = this_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)

cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ee = cc + dd
print(ee)
