
# TODO: To learn Lambda function
# func = lambda x  :lambda y: lambda z:z+y+x
# print(func(30)(20)(10)) # first value of x than y than z


# def set_power(power):
#     return lambda num : num**power


# ? similar func lambda way
# set_power = lambda power: lambda num: num**power

# def print_range(power, start, end):
#     powered = set_power(int(power))
#     for num in range(int(start), int(end) + 1):
#         print(powered(int(num)))

# print_range(3, 1, 10)


# ? recursion using labmda function
# fact = lambda num: num if num ==1 else fact(num-1)*num
# print(fact(5))


# ? Filter function
# l1 = [i for i in range(31)]
# mul_five = list(filter(lambda x: (x % 5 == 0), l1))
# mul_6_and_5 = list(filter(lambda x: (x % 6 == 0 and x % 5 == 0) and (x!=0), l1))

# print(mul_five)
# print(mul_6_and_5)


# ? Map
"""
l1 = [i for i in range(11)]
l1 = list(map(lambda x: x*2 if x%2==0 else 0, l1))
print(l1)
"""


# ? reduce
"""
from functools import reduce

l1 = [i for i in range(11)]
# print(reduce(lambda x, y: x if x > y else y, l1))
print(reduce(lambda x,y:(x+y),l1))
"""

l = [i for i in range(10)]
print(l)

l = list(filter(lambda x:(x%2==0),l))
print(l)
