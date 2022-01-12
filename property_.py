
# class Person:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def del_name(self):
#         del self.__name

#     name = property(fget=get_name, fset=set_name, fdel=del_name)

class Person:
    """Using Decorators"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


p = Person('Sharique')
print(p.name)

p.name = 'Nargis'
print(p.name)

del p.name
print(p.__dict__)
