from Singleton import Singleton


class Singleton1:
    __instance = None #type:Singleton1

    @staticmethod
    def get_instance():
        if Singleton1.__instance == None:
           Singleton1()
        return Singleton1.__instance

    def __init__(self):
        if Singleton1.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton1.__instance = self

    @staticmethod
    def print_text():
        print("printing text")

s = Singleton1()
s = Singleton1.get_instance()

print(s.print_text())
s.print_text()



@Singleton
class Singleton2:

    def __init__(self):
        print("test")

    def test(self):
        print("herere")

s3 = Singleton2.instance()
s3.test()

