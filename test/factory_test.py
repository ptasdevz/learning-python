from objects.factory import Factory

fac = Factory()
a = fac.create("a")#type:A
b = fac.create("b")#type:B
b.testB(a)
a.testA(b)