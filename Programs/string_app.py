
def func():
    """String manipulations program"""
    string = input('Enter the strings here: ')
    l1 = ""
    for index, element in enumerate(string):
        if index == 0:
            count = 1
            continue
        if element != string[index - 1]:
            l1 += f"{count}{string[index - 1]}"
            count = 1
        else:
            count += 1
    l1 += f"{count}{string[index]}"
    return l1


print(func())
