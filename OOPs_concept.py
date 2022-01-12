

# ?  without using decorators
# class Person:
#     def __init__(self,name) :
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self,name):
#         self.__name = name

#     def del_name(self):
#         del self.__name

#     name = property(get_name,set_name,del_name)

# p = Person('Steven')
# print(p.name)
# p.name = 'Sharique'
# print(p.name)
# del p.name
# print(p.name)


# ? using decorator
# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @name.deleter
#     def name(self):
#         del self.__name


# p = Person('Steven')
# print(p.name)
# p.name = 'Sharique'
# print(p.name)
# del p.name
# print(p.__dict__)
