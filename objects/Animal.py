class Animal:

    can_move = True

    def __init__(self):
        self.name = ""
        self.eye_color = ""

    def walk(self):
        pass

    def __str__(self):
        return '{}, {}'.format("name : "+ self.name, "eye_color : " + self.eye_color)


class Person:

    def __init__(self):
        self.is_made_in_god_img = True

    def __str__(self):
        return '{}'.format("in_god_img : " + str(self.is_made_in_god_img))


class Human (Person):

    def __init__(self):
        super().__init__()
        self.name = "jason"
        self.eye_color = "brown"

    def walk (self):
        return "Human is walking"


class Bird (Animal):

    def __init__(self):
        self.name = "golondrina"
        self.eye_color = "blue"

    def walk(self):
        return "Bird is walking"


b1 = Bird()
h1 = Human()

print(b1)
print(h1)
