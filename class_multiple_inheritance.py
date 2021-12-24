class Parent:
    def House(self):
        print('You get your parents house')


class Grandpa:
    def Farm(self):
        print('You got your grandpa farm')


class You(Parent, Grandpa):
    def Job(self):
        print("You got your Job")


y = You()  # You inherting both farm and house from Grandpa and Parent
y.Farm()
y.House()
y.Job()
