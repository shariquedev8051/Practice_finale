import re
while not input():
    matcher = re.finditer(input("Enter "),'abbx#$556A')
    for match in matcher:
        print(match.start(),'-----',match.end(),'-----',match.group())