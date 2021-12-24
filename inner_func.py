def outer(func):
    def inner(name):
        print('In inner function')
        print("Calling main function")
        func(name)
    return inner
@outer
def hi(name):
    print(f"Hello {name}")


hi('sharique')




