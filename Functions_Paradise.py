

# #? in form of function
# def sum_func(string):
#     l = string.split()
#     l = [int(x) for x in l]
#     return sum(l)

# # print(sum_func(input("Enter value seprated by spaces: ")))


# #? in a single line
# def func_one_line(string):
#     return lambda x:sum([int(x) for x in string.split()])

# # print(func_one_line(input("Enter value seprated by spaces: ")))


# ? for equilateral triangle
# for i in range(1,7,1):
#     print("*"*i if i<=2 else ('*'+' '*(i-2)+'*') if 3<=i<=5 else "*"*i)


# ? for third finding greatest number
'''
data = [int(i) for i in input('Enter the data:- ').split()]
if not data:
    data = [1, 2, 3, 4, 3, 4, 3, 8, 5]

first, second, third = data[:3]
count=2
while count<len(data):
    num = data[count]
    if num == first or num == second or num == third or num<third:
        count+=1
        continue 
    else:
        if num>first:
            first,second = num,first
        elif third<num<second:
            second, third = num, second
        else:
            third = num
    count+=1
print(third)
'''


# ? to find the third greatest number
"""
from random import randint
first = second = third = 0
data = [randint(1, 20) for i in range(10)]
print(sorted(list(set(data))))
"""
"""
for num in data:
    if num in (first,second,third) or num<third:
        continue
    if num>first:
        first ,second,third = num, first,second
    elif second<num<first:
        second, third = num, second
    else :
        third = num
    print(first,second,third)
print(third)
"""

# ? finding the greatest third number
"""
first = second = third = 0
for num in data:
    if num in (first,second, third) or num < third:
        continue
    if num > first:
        first, second, third = num, first, second
    elif first > num > second:
        second, third = num, second
    else:
        third = num
    print(first,second,third)
print(third)
"""

# ? using lambda functions

# ? Finding the greatest number

"""
from functools import reduce
def sorted_list(l):
    sorted_list = []
    for i in l:
        if i not in sorted_list:
            sorted_list.append(i)
    return sorted_list


def find_greatest(l, index):
    indexed_greatest_number = 0
    for i in range(index):
        indexed_greatest_number = l.pop(
            l.index(reduce(lambda x, y: x if x > y else y, l)))
    return indexed_greatest_number


data = [int(i) for i in input('Enter the numbers:-\n').split()]
l = sorted_list(data)
print(find_greatest(l, 4))
"""

# ? reverse the strings but not the special character

"""
def find_special_char():
    s = input('enter the sample string:- ')
    if not s:
        s = "Hello$world"

    index_l = []
    string_list = [i for i in s]

    for index, a in enumerate(string_list):
        if not a.isalnum():
            index_l.append((index, a))
            string_list.pop(index)
    string_list.reverse()
    for index, spchar in index_l:
        string_list.insert(index, spchar)
    return "".join(string_list)


reversed_string = find_special_char()
print(reversed_string)
"""

# ? star pattern

# rows = int(input('entter number of row here:- '))

# * for simple star pattern
# for i in range(1, rows + 1, 1):
#     print('*' * i)

# * equilateral
# for i in range(1,rows,1):
#     print(' '*(rows-i)+'* '*i)


# ? programms to finds all substrings from strings

# def find_index(string='Hello world', sub_string='l'):
#     pos = -1
#     flag = False
#     slen = len(string)
#     while True:
#         pos = string.find(sub_string, pos + 1, slen)
#         if pos == -1:
#             break
#         print(f'substring found at index:- ', pos)
#         flag = True
#     if not flag:
#         print('No substring found!')

# find_index('ABABAAAABA','C')


# ? To reverse the character on their places
# s = 'Hello world'
# s = s.split()
# for index,word in enumerate(s):
#     s[index]= word[::-1]
# print(' '.join(s))


# ? For printing data ulternatively
# s1= input("Enter first string:- ")
# s2= input("Enter second string:- ")
# s = ''
# i=j=0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         s+=s1[i]
#         i+=1
#     if j<len(s2):
#         s+=s2[j]
#         j+=1
# print(s)


# ? converting two different list into dictionary without data loss
# l1 = [i for i in range(10)]
# l2 = ['Apple', 'Banana', 'Mango','Cherry','Chikoo','Water melon']
# len1 = len(l1)
# len2 = len(l2)
# flag = False
# if len1 != len2:
#     if len1 > len2:
#         for i in range(len1 - len2):
#             l2.append('No value found')
#     else:
#         for i in range(len2 - len1):
#             l1.append('No value found')
#             flag = True
# if not flag:
#     d = {key:value for (key,value) in zip(l1,l2)}
# else:
#     d = {key:value for (key,value) in zip(l2,l1)}
# print(d)


# ? For
# w = "$Hello#world&"
# index_list = [(index, s) for (index, s) in enumerate(w) if not s.isalnum()]
# l = [s for s in w if s.isalnum()]

# print(index_list,l)

#? star pattern
# n = int(input('Enter the numbers of rows:- '))
# # for i in range(1,1+n):
# #     print(" "*(n-i), end='')
# #     for j in range(1,1+i):
# #         print("* ", end ='')
# #     print()

# for i in range(1,1+n):
#     print(" "*(n-i)+f'{chr(64+i)} '*i)
# for i in range(n-1,0,-1):
#     print(" "*(n-i)+f'{chr(64+i)} '*i)


#?