from objects.AInterface import AInterface
from objects.BInterface import BInterface


class B(BInterface):

    def testB(self,a:AInterface):

        print("in test test B")
        a.testA1()

    def testB1(self):
        print("printing test B1")





