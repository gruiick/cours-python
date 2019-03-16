% Programmation avec Python (chapitre 8)
% Dimitri Merejkowsky

\center \huge Rappels

# Définition et utilisation d'une classe

```python
class Counter:
   def __init__(self):
   	self.count = 0

   def increment(self, times=1):
   	self.count += times

>>> counter = Counter()
>>> counter.increment(times=2)
>>> counter.count
2
>>> counter.increment()
>>> counter.count
3
```

# Vocabulaire

* `counter` est une *instance* de la *classe* `Counter`
* `increment` est une *méthode d'instance*
* `count` est un *attribut d'instance*
* `__init__` est un *constructeur*

# Méthodes et attributs de classe

```python
class Car:
    total_number_of_cars = 0

    def __init__(self, color="black"):
        self.color = color
        Car.total_number_of_cars += 1

    @classmethod
    def print_number_of_cars(cls):
       print(cls.total_number_of_cars,
               "cars have been made")

 >>> ford = Car()
 >>> ferrari = Car(color="red")
 >>> Car.print_number_of_cars()
 2 cars have been made
```

#

\center \huge Composition

# Composition

* Quand on met une classe dans une autre.

* Par exemple, le constructeur de la classe A va prendre en paramètre une
  instance de la classe B.

* Introduit un *couplage* entre les classes A et B.

# Example

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

# Couplage 1

Il faut construire une instance d'`Authorization` pour pouvoir
construire une instance de `Client`


```python
>>> auth = Authorization("credentials.txt")
>>> client = Client(auth)
>>> client.make_request()
```

# Couplage 2

Si jamais l'atttribut `password` dans la classe `Authorization` change,
le code dans `Client.make_request()` devra changer aussi.

```python
class Authorization:
    ...
    self.password = ...


class Client:
   ...

    def make_request(self):
        password = self.auth.password
        ...
```

# Conclusion

Prenez le temps d'étudier les relations entre les différentes classes!

Souvent un simple schéma suffira.

#

\center \huge Héritage

# Petit détour

Qu'est-ce qui ne va pas dans ce code?

```python
def faire_le_cafe():
    mettre_cafe_dans_tasse()
    allumer_bouilloire()
    attendre_que_ca_bouille()
    verser_dans_tasse()
    melanger()

def faire_le_the():
    mettre_the_dans_tasse()
    allumer_bouilloire()
    attendre_que_ca_bouille()
    verser_dans_tasse()
    laisser_infuser()
```

# Duplication

* Les lignes de `allumer_bouilloire()` à `verser_dans_tasse()` sont les mêmes
* Le code est plus long
* Si jamais la procédure pour faire chauffer l'eau change, il faudra changer
  le code a deux endroits différents

# Solution: extraire une fonction

```python
def faire_chauffer_l_eau():
    allumer_bouilloire()
    attendre_que_ca_bouille()

def faire_le_cafe():
   mettre_cafe_dans_tasse()
   faire_chauffer_l_eau()
   verser_dans_tasse()
   melanger()

def faire_le_the():
    mettre_the_dans_tasse()
    faire_chauffer_l_eau()
    verser_dans_tasse()
    laisser_infuser()
```

# Facile à changer

Si maintenant il faut débrancher le grille-pain avant de pouvoir faire chauffer l'eau,
on a juste à changer une fonction:

```python
def faire_chauffer_l_eau():
    debrancher_grille_pain()
    brancher_bouilloire()
    allumer_bouilloire()
    attendre_que_ca_bouille()
```

# Note

Notez qu'on a *laissé* la ligne `verser_dans_tasse()` dupliquée.

C'est une duplication par *coïncidence*.

Et ça nous permet de faire ça:

```python
def faire_le_the():
    faire_chauffer_l_eau()
    mettre_the_dans_tasse()
    verser_dans_tasse()
    laisser_infuser()
```

# Conclusion

Encore une fois, réfléchissez avant d'agir!

#

\center \huge Héritage

# Un autre type de relation entre classes

Si la composition est une relation "has-a", l'héritage décrit
une relation "is-a".

# Composition

```python
class Dog:
    pass

class Person:
     def __init__(self, pet=None):
          self.pet = pet

>>> nestor = Dog()
>>> john = Person(pet=nestor)
>>> john.pet
nestor
```

`John` *a* un animal.


# Héritage

```python
class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
     pass

```

`Dog` et `Cat` *sont* des animaux.

# Vocabulaire

```python
class A:
    ...

class B(A):
    ...
```

* A est la classe *parente* de B.
* B *hérite* de A.
* B est une classe *fille* de A.


# Utilisation

* Si une méthode n'est pas trouvée dans la classe courante,
  Python ira la chercher dans la classe parente

```python
class A:
   def method_in_a(self):
       print("in a")

class B(A):
   def method_in_b(self):
       print("in b")


>>> b = B()
>>> b.method_in_b()
'in b'  # comme d'habitude
>>> b.method_in_a()
'in a'
```

# Ordre de résolution

S'il y a plusieurs classes parentes, Python les remonte toutes:

```python
class A:
    def method_in_a(self):
         print("in a")

class B(A):
    def method_in_b(self):
         ...

class C(B):
    def method_in_c(self):
         ...

>>> c = C()
>>> c.method_in_a()
'in a'
```

# Avec `__init__`

La résolution fonctionne pour toutes les méthodes, y compris `__init__`

```python
class A:
    def __init__(self):
         print("Building parent")

class B(A):
    ...

>>> b = B()
Building parent
```

# Attributs

Même méchanisme pour les attributs:

```python
class A:
    def __init__(self):
        self.a_attribute = 42

class B(A):
    ...

>>> b = B()
>>> b.a_attribute
42
```

# Overriding

On peut aussi *écraser* la méthode du parent dans l'enfant:

```python
class A:
   def my_method(self):
       print("method in A")

class B(A):
    def my_method(self):
        print("method in B")


>>> b = B()
>>> b.my_method()
"method in B"
```

# super()

Demande à chercher une méthode dans la classe parente

```python
class A:
   def a_method(self):
      print("method in A")

class B(A):
   def b_method(self):
       super().a_method()
       print("method in B")

>>> b = B()
>>> b.b_method()
method in A
method in B
```

# `super` et `__init__`

Erreur très courante:

```python
class A:
   def __init__(self):
       self.a_attribute = "foo"

class B(A):
    def __init__(self):
       self.b_attribute = 42

>>> b = B()
>>> b.b_attribute
42
>>> b.a_attribute
AttributeError
```

On a écrasé `A.__init__`!

# `super` et `__init__`

```python
class A:
   def __init__(self):
       self.a_attribute = "foo"

class B(A):
    def __init__(self):
       super().__init__()
       self.b_attribute = 42

>>> b = B()
>>> b.b_attribute
42
>>> b.a_attribute
"foo"  # OK
```

#


\center \huge Atelier


# Objectif

*Une autre vision de l'héritage*: on va rajouter une fonctionnalité dans
notre script marvel, puis on va réduire le code dupliqué.

# Résultats

* Départ: https://github.com/E2L/cours-python/blob/master/sources/marvel/marvel_04.py

\vfill

* Arrivée: prochainement sur `git.e2li.org` :)
