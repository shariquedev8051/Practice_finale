from itertools import zip_longest

l1=[i for i in range(10)]
l2 =[i for i in 'abcdefghijklmnopqrstuvwxyz']
d = {k:v for (k,v) in zip_longest(l2,l1,fillvalue='Defualt')}
print(d)