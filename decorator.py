

# def first_decorator(func):
#     print('In first decorator')

#     def inner(*args):
#         return func(*args)
#     return inner


# def second_decorator(func):
#     print('In second decorator')

#     def inner(*args):
#         return func(*args)
#     return inner


# @first_decorator
# @second_decorator
# def greeting(*args):
#     name = args[0]
#     return f'Hello {name}'


# print(greeting('Sharique'))

# ? to caculate time using time and timeit module

from time import time
from timeit import timeit


def time_decorator(func):
    def inner(l):
        t1 = time()
        for i in range(100):
            func(l)
        t2 = time()
        print('Time taken is :-', t2 - t1)
    return inner


@time_decorator
def list_func(l):
    add = 0
    for num in l:
        add += num
    print(f'Sum is {add}')
    


l = [i for i in range(100)]
list_func(l)
