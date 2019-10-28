class Student:


    school = "marriaqua"

    def __init__(self, name, age, school, is_registered, gpa):
        self.name = name
        self.age = age
        self.school = school
        self.is_registered = is_registered
        self.gpa = gpa

    def __init__(self):
        self.name = "test"


    def is_on_honor_roll(self):
        if self.gpa >=3.5:
            return True
        else:
            return False

    @classmethod
    def get_school (cls):
        print(cls.school)

    @staticmethod
    def get_info():
        print("this is my class")



s1 = Student("jason","37","man",True,3.9)
s2 = Student()


#print (s1.get_info())
print (s1.get_school())
print (s2.age)




