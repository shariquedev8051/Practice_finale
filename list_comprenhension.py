

# ? formate [value for value in range()]
# l1 = [i for i in range(10)]
l1 = [i * 2 for i in range(10)]

# ? For conditional operator [value for value in range() if conditon]
l1 = [i for i in range(10) if i % 2 == 0 if i % 3 == 0]

# ? for else condtion
l1 = ['odd' if i % 2 == 0 else 'Even' for i in range(10)]
l1 = [i**2 if i % 2 == 0 else i for i in range(10)]

print(l1)
