% Programmation avec Python (chapitre 9)
% Dimitri Merejkowsky



\center \huge Formats et chaînes de caractères

# Formater des chaînes de caractères

Problème:

\vfill

```python
>>> nom = "Ford"
>>> résultat = 42
>>> message = "Bonjour, " + nom + ". "
>>> message += "La réponse est: " + str(résultat) + "."
>>> message
'Bonjour, Ford. La réponse est: 42.'
```

\vfill

Ce n'est pas très lisible ...

3 solutions différentes en Python

# Solution 1: À l'ancienne

* Avec `%`
* Compatible avec les très vieux Pythons
* Compatibles avec d'autres langage (`printf` en C par example)


# Example 1

```python
name = "John"
print("Bonjour %s!" % name)   # 's' comme string

age = 42
print("Vous avez %i ans" % age)  # 'i' comme integer

poids = 68.5
print("Vous pesez %f kilos" % poids)  # 'f' comme integer

```

# Attention aux types:

```python
>>> print("Bonjour %i!" % name)
TypeError: %i format: a number is required, not str
```

# On peut en mettre plusieurs

Avec un tuple:
```python
print("Bonjour %s, vous avez %i" % (name, age))
```
\vfill

Avec un dictionnaire:
```python
data = {"name": "John", "age": 42}
print("Bonjour %(name)s, vous avez %(age)i ans" % data)
```

# Solution 2: format()

Des `{}` comme "placeholders" et une *méthode* sur les strings:

```python
>>> nom = "Ford"
>>> résultat = 42
>>> template = "Bonjour, {}. La réponse est: {}"
>>> message = template.format(nom, résultat)
>>> message
'Bonjour, Ford. La réponse est: 42.'
```

* Pas de types!

# format() - à plusieurs

On peut aussi nommer les remplacements:

```python
template = "Bonjour, {nom}. La réponse est: {résultat}"
template.format(nom="Ford", résultat=42)
```

# format() - à plusieurs

On peut les ordonner:

```python
template = "Bonjour {1}. La réponse est {0}"
template.format(reponse, name)
```

* Pas possible avec `%`!

# Solution 3: f-strings

* La meilleure de toutes :)
* Plus succint que `format()`
* Plus performant que `%` et `.format()`
* Mais pas avant Python 3.6 (2016)

# Principe

On peut mettre du *code* dans `{}` avec la lettre `f` devant la chaîne:

```python
name = "Patrick"
score = 42
text = f"Bonjour {name}. Votre score est: {score}"
```

\vfill

Mais aussi:

```python
a = 2
b = 3
text = f"résultat: {a + b}"
```

# Conclusion

Je vous ai présenté `%` et `format()` parce que vous risquez d'en voir.

Mais si vous avez le choix, utilisez des `f-strings`!


# Spécifications de formats

* Permet des opérations pendant la conversion en texte
* Fonctionne avec les 3 solutions

# Tronquer

```python
>>> pi = 3.14159265359
>>> f"pi vaut à peu près {pi:.2f}"
pi vaut à peu près 3.14
```

Le texte dans les accolades après le `:` est un mini-langage de spécification de format.
`.2f` veut dire: 2 chiffres après la virgule maximum.

Fonctionne aussi avec `.format()` `et %`:

```python
"pi vaut à peu près {:.2f}".format(pi)
"pi vaut à peu près %.2f" % pi
```

# Alignements et paddings

On peut aussi faire des alignements et du "padding":

\vfill

```python
template = "{name:>10}: {score:03}"
print(template.format(name="Alice", score=42))
print(template.format(name="Bob", score=5))
```

```
     Alice: 042
       Bob: 005
```

* `>10` : aligné à gauche, taille minimum 10
* `03`: rajouter jusqu'à 2 zéros à gauche pour que la taille fasse 3

# Documentation

Documentation ici:

htps://docs.python.org/fr/3/library/string.html#format-specification-mini-language

#

\center \huge Rappels sur les classes

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
    	password = self.auth.get_password()
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

On dit aussi que A est la classe *de base* et B la classe *dérivée*.

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
    def do_stuff(self):
        print("A!")

class B(A):
    def do_stuff(self):
        print("B!")

>>> a = A()
>>> a.do_stuff() # ok
'A!'

>>> b = B()
>>> b.do_stuff()
'B!'
```

# Héritage - super()


```python
class A:
    def do_stuff(self):
        print("A!")

class B(A):
    def do_stuff(self):
        super().do_stuff()
        print("B!")

>>> a = A()
>>> a.do_stuff() # ok
'A!'
>>> b = B()
>>> b.do_stuff()
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
        super().__init__("dog", name)
```

#

\center \huge Interfaces et classes abstraites

# Example

Imaginons un jeu où il faut retrouver le nom d'un super-héros à partir
de sa description.

On a une classe `MarvelClient` qui permet de lister les personnages et leurs
descriptions et une class `Game` pour la logique du jeu

# Implémentation - MarvelClient

```python
class MarvelClient:
    url = "https://marvel.com/api"

    def __init__(self, credentials_file):
        # réupére les clés depuis un fichier

   def get_all_characters(self):
        # appelle l'api marvel pour récupérer
        # tous les personnages

    def get_description(self, character_name)
        # appelle l'api marvel pour récupérer
        # une description

```

# Implémentation - Game

```python
import random


class Game:
  def __init__(self, marvel_client)
    self.marvel_client = marvel_client

  def play(self):
    characters = self.marvel_client.get_all_characters()
    name_to_guess = random.choice(characters)
    description = self.marvel_client.get_description(
      name_to_guess)

    while not self.won():
      ...
```

# Contrats implicites - 1

Il y a un *contrat implicite* entre `Game` et `MarvelClient`.

Dans `play` on appelle `self.marvel_client.get_all_characters()` donc la méthode
`get_all_characters()` doit:

* exister
* ne prendre aucun argument
* retourner une liste de noms

# Contrats implicites - 2

Pareil avec `get_description()`. La méthode doit:

* exister
* prendre un nom en unique argument
* retourner une description

# Une force et une faiblesse

On peut passer à `Game.__init__()` n'importe qu'elle classe pourvu qu'elle ait
les bonnes méthodes!

On appelle ça "duck typing"

# duck typing

Définition traditionnelle (pas exacte à mon sens):

* Si ça marche comme un canard et que ça fait coin-coin comme un canard alors c'est un canard.

\vfill

Meilleure définition:

* Tu peux passer remplacer le canard par une vache. Tant que la vache a un bec et fait coin-coin, c'est bon!

# En image

![canard vache](img/canard-vache.jpg)

# Exemple utile


```python
class FakeClient():
    def get_all_characters(self):
       return ["Spider-Man", "Batman", "Superman"]

    def get_description(self, name):
        if name == "Spider-Man":
           ...

       ...
fake_client = FakeClient()
game = Game(fake_client)
game.play()

# Tout marche!
```

# Problème

Comment s'assurer que `FakeClient` et `MarvelClient` restent synchronisés?


# Solution

Une classe *abstraite*:

```python
import abc

class BaseClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_all_characters(self):
        pass

    @abc.abstractmethod
    def get_description(self, name):
        pass
```

On retrouve le `@` au-dessus des méthodes.
On reparlera des metaclasses plus tard :)

# Utilisation

On ne peut pas instancier la classe abstraite directement:

```python
>>> client = BaseClient()
# Cannot instantiate abstract class BaseClient
# with abstract methods
# get_all_characters, get_description
```

En revanche on peut en hériter:


```python
class MarvelClient(BaseClient):
    def get_all_characters(self):
    	...

    def get_description(self, name):
    	...
```

À la construction, Python va vérifier que les méthodes abstraites
sont bien surchargées.

# Conclusion

Plein de langages ont un concept d'interface.

C'est utile de savoir que les interfaces existent en Python et ça peut rendre
le code plus clair.

Cela dit, dans le cas de Python c'est complètement *optionnel*.

#

\center \huge Atelier

# Encore un refactoring

Résultat sur `git.e2li.org`:

`dmerejkowsky/cours-python/sources/marvel/marvel.py`

# Pour la prochaine fois:

* Créer un compte dévelopeur sur le site de Marvel
* Implémenter le jeu!
* Consignes:

`dmerejkowsky/cours-python/sources/marvel/consignes.md`
