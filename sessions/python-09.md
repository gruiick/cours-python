% Programmation avec Python (chapitre 9)
% Dimitri Merejkowsky

\center \huge Rappels

# Classes

```python
class Car:
    total_number_of_cars = 0

    def __init__(self, color="black"):
        self.color = color
        Car.total_number_of_cars += 1

    def drive(self):
        print("vroom")

    @classmethod
    def print_number_of_cars(cls):
       print(cls.total_number_of_cars,
               "cars have been made")
```

# Composition


```python
class Authorization:
    def __init__(self, credentials_file):
        ...
        self.password = ...

class Client:
    url = "https://exmple.com"
    def __init__(self, auth)
        self.auth = auth

    def make_request(self):
    	password = self.auth.password
    	requests.get(url, password=password)
```

# Héritage - partage des attributs et méthodes

```python
class A:
    def method_in_a(self):
       self.attribute_in_a = 42

class B(A):
    def method_in_b(self):
        self.method_in_a()  # ok
        self.attribute_in_a # ok
```

# Héritage - ordre de résolution des méthodes

```python
class A:
    def method_in_a(self):
        pass

class B(A):
    def method_in_b(self):
    	pass

>>> a = A()
>>> a.method_in_a() # ok
>>> a.method_in_b() # error

>>> b = B()
>>> b.method_in_b()  # ok
>>> b.method_in_a()  # ok
```

# Héritage - ordre de résolution des méthodes

```python
class A:
    def method_in_a(self):
        pass

class B(A):
    def method_in_b(self):
    	pass

>>> a = A()
>>> a.method_in_a() # ok
>>> a.method_in_b() # error

>>> b = B()
>>> b.method_in_b()  # ok
>>> b.method_in_a()  # ok
```

# Héritage: surcharge

```python
class A:
    def method(self):
        print("A!")

class B(A):
    def method(self):
        print("B!")

>>> a = A()
>>> a.method() # ok
'A!'

>>> b = B()
>>> b.method()
'B!'
```

# Héritage - super()


```python
class A:
    def method(self):
        print("A!")

class B(A):
    def method(self):
        super().method()
        print("B!")

>>> a = A()
>>> a.method() # ok
'A!'
>>> b = B()
>>> b.method()
'A!'
'B!'
```

# Héritage - super() et \_\_init\_\_


```python
# All animals have a species
class Animal:
    def __init__(self, species):
    	self.species = species

# Pets are animals with a name
class Pet(Animal):
    def __init__(self, species, name):
    	super().__init__(species)   # <- à ne pas oublier
    	self.name = name

# All dogs are pets
class Dog(Pet):
   def __init__(self, name):
   	super().init("dog", name)
```
