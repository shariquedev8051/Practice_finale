
def add(a=None, b=None, *args, **kwargs):
    print(a, b)
    if args:
        print('You have passed arguments!!')
        print(args)
    if kwargs:
        print("You have passed kwargs!!")
        print(kwargs)


# add(20,30,40) #Positional arguments
# add([20,30,40]) # Only args
# All the positional argumnet, arguments and kwargs are there
add(10, 20, 30, 40, c=50)
