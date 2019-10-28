from objects.A import A
from objects.B import B


class C:
    c = None#type:str



a = A()
b = B()
c = C()

a.b = B()
b.a = A()

print(b)
print(a)