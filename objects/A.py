from objects.AInterface import AInterface
from objects.BInterface import BInterface


class A(AInterface):

    def __init__(self):
        self.

    def testA(self, b:BInterface):

        print("in test A")
        b.testB1()

    def testA1(self):
        print("printing test A1")



# a = A()
# a.testA()

