import csv

"""
# To write csv data into csv.files
with open('first.csv', 'w', newline="") as f:  # To avoid new line between the csv files
    w = csv.writer(f)
    w.writerow(['ENO', 'ENAME', "ESAL", "EADDR"])
    n = int(input('Enter Numbers of Employees: '))
    for i in range(n):
        eno = input('Enter employee no: ')
        ename = input('Enter employee name: ')
        esal = input('Enter employee salary: ')
        eaddr = input('Enter employee address: ')
        w.writerow([eno, ename, esal, eaddr])
    print("Employees Added!!")

"""

# To read data from csv files

with open('first.csv', 'r') as f:
    r = csv.reader(f)
    data = list(r)
    # print(data)
    for line in data:
        for word in line:
            print(word, '\t', end='')
        print()
