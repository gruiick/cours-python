def add(a, b):
    return a + b

nombre_1 = 1
nombre_2 = 2
c = add(nombre_1, nombre_2)
print(c)



def greet(name, shout=False):
    print("Hello,", end=" ")
    print(name, end="")
    if shout:
        print("!", end="")
    print("", end="\n")

greet("John")
greet("Jane", shout=True)
