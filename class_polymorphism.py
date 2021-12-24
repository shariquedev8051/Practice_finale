# same name can be using in child class and it will overwrite the parent class

class Greetings:
    def Hi(self):
        print('Hi from Parent class')


class Child(Greetings):
    def Hi(self):
        print("Hi from child class")


g = Greetings()
g.Hi()
c = Child()
c.Hi()
