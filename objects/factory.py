from objects.A import A
from objects.B import B
from objects.IFactory import IFactory


class Factory(IFactory):

    def a(self):
        return A()
    def b(self):
        return B()
    def create(self, obj_name:str):

        switcher = {
            "a": self.a,
            "b": self.b
        }
        func = switcher.get(obj_name,lambda:"invalid object")
        return func()


# fac =Factory()
# print(fac.create("c"))

