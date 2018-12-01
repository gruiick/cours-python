def add(a, b):
    return a + b

a = 1
b = 2
c = add(a, b)
print(c)



def greet(name, shout=False):
    print("Hello,", end=" ")
    print(name, end="")
    if shout:
        print("!", end="")
    print("", end="\n")

greet("John")
greet("Jane", shout=True)
