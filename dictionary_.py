
# ? To add number of student in dictionary and display there marks when asked
"""
no_student = int(input('Enter the number of student:- '))
i = 0 
stud_dict = {}
while i<no_student:
    name = input('Enter the student name ')
    marks = int(input('Enter the student marks '))
    stud_dict[name] = marks
    i+=1

for name,marks in stud_dict.items():
    print(name,'------',marks)
"""


# ? Calculating the length of word and storing it in value
# sentence =[word for word in input("Enter the sentence here :- ").split()]
# d = {word:len(word) for word in sentence}
# print(d)


# ? How to combined tow values without actually using longest zip
# l1 = [i for i in 'abcdefghi']
# l2 = [i for i in range(5)]
# len1 = len(l1)  # reduces the time needed in while loop
# len2 = len(l2)  # reduces the time needed in while loop
# l = []
# i = 0
# while i < len1 or i < len2:  # replacement in indexError
#     try:
#         l.append((l1[i], l2[i]))
#     except IndexError:
#         l.append((l1[i], 'Default'))
#     finally:
#         i += 1
# print(l)


# ? reverse the string
# s = "Hello$world#"
# index_list = [(index,w) for index,w in enumerate(s) if not w.isalnum()]
# l = [w for w in s if w.isalnum()]
# l.reverse()
# for index,w in index_list:
#     l.insert(index,w)
# print("".join(l))


# ? lambda function to return factorial of number
# num = int(input("Enter the number :- "))
# fact = lambda x: 1 if x==1 else x*fact(x-1)
# print('Factorial is',fact(num))




