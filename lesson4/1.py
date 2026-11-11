import string


def greet(name):
    print("Hello " + name)
    return greet


name = str(input("введите name"))
print(greet(name))
