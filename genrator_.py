def countdown(num):
    while(num > 0):
        yield num
        num -= 1


c = countdown(5)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
