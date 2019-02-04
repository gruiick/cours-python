% Programmation avec Python (chapitre 6)
% Dimitri Merejkowsky


#

\center \huge Les classes

# Paradigmes

Une façon d'envisager le code.
Pour l'instant on n'a vu que le paradigme *procédural* (ou (impératif).

Il y en a plein d'autres! (*fonctionnel* notamment, dont on parlera un jour)

# Détails du procédural

* des types simples (entiers, booléens)
* des structures de données (dictionnaires, listes ...)
* des fonctions qui manipulent des types simples ou des structures
* les fonctions sont appelées les unes après les autres

Aujourd'hui on va parler de *l'orienté objet*.

# Un petit détour

Un nouveau built-in: `id()`

L'adresse de l'objet pointé par la variable:

```
>>> a = 42532
>>> id(a)
94295009035968
>>> b = a
>>> id(b)   # même objet
94295009035968
>>> c = 42532  # objet différent, même valeur
>>> id(c)
```

# Orienté objet - 1ère définition

Mettre au même endroit:

* des données
* des fonctions qui opèrent sur ces données

L'important c'est que les deux aillent ensemble

OOP en Anglais (ou juste OO)

# Orienté objet - 2ème définition

Des "cellules" qui s'envoient des "messages".

Notamment, les cellules ne "voient" que leur état interne.

On peut envoyer un message d'une cellule à une autre *sans* connaître
beaucoup de détails à propos du destinataire du message

# Les classes

On va parler *d'une* façon de faire de l'orienté objet: avec des classes.

Mais notez bien qu'on peut faire de l'orienté objet *sans* classes!

# Le plan de construction

La seule chose dont on a besoin, c'est le mot-clé `class` et un nom.

```python
class MyObject:
    pas
```

La classe est le plan de construction de notre objet.

# Créons des objets

```python
>>> object_1 = MyObject()
>>> object_2 = MyObject()
```

Python ne sait rien de l'objet à part son adresse on mémoire et son nom:

```python
print(object_1)
 <__main__.MyObject at 0x7f52c831e2b0>
```

On appelle `object_1` et `object_2` des *instances* de la classe `MyObject`.

# Méthodes

Une fonction dans une classe

```
class MyObject:
    def my_method(the_object):
        print("hello", the_object)
```

C'est tout!

# Méthodes - 2

La méthode n'existe pas en dehors de la classe (souvenez vous des cellules !)

```
>>> my_method()
NameError
>>> object = MyObject()
>>> object.my_method()
Hello, <MyObject at 0x7f52c9f6d6d8>
```

Notez que `my_method` a pris en premier argument ce qu'il y avait *à gauche* du point:

D'ailleurs, ce code fonctionne aussi et retourne *la même chose*:

```
>>> MyObject.my_method(object)
Hello, <MyObject at 0x7f52c9f6d6d8>
```

# Méthodes - 3

Il *faut* passer l'objet en cours en paramètre:

```python
class MyObject:
    def broken():
        print("You cannot call me!")
```

```python
>>> o = MyObject()
>>> o.broken()
TypeError: broken() takes 0 positional arguments but 1 was given
```

# Conventions

* Les classes sont en CamelCase
* Tout le reste (méthodes, etc...) en snake_case
* L'objet en cours s'appelle **toujours** `self`


```python
class MyObject:
    def my_method(self):
        print("hello", self)
```

# Attributs

* Des variables dans un objet.
* On peut ajouter un attribut quand on veut à qui on veut, et toujours avec le
  point au milieu:

```python
>>> object = MyObject()
>>> object.attribute   # ici l'attribut n'existe pas
AttributError
>>> object.attribute = 42  # maintenant oui
>>> object.attribute
42
```

# Attributs dans les méthodes

Avec `self`, bien sûr:

```python
class MyObject:
    def print_attribute(self):
        print(self.attribute)

    def change_attribute(self, new_value)
        self.attribute = new_value
```

# Accéder aux attributs

```python
>>> object = MyObject()
>>> object.print_attribute()  # ici l'attribut n'existe pas
AttributError
>>> object.attribute = 42
>>> object.print_attribute() # ça marche
42
>>> object.change_attribute(43)
>>> object.attribute
43
```

# Initialisation des attributs

Avec `__init__`:

* méthode "spéciale"
* appelée automatiquement
* notez les deux underscores avant et après ('dunder' en Anglais)

```python
class MyObject:
    def __init__(self):
        self.attribute = 42
```

```python
>>> object = MyObject()
>>> object.attribute
42
```

# Construire des objets différents

`__init__()` et `MyObject()` sont des appels de fonctions comme les autres

```python
class Car:
    def __init__(self, color_to_use="black"):
        self.color = color_to_use

>>> ford = Car()
>>> ford.color
"black"
>>> ferrari = Car(color_to_use="red")
>>> ferrari.color
"red"
```

# Notes

En vrai, on nomme souvent les paramètres du constructeur et les attributes de la même façon.

```python
class Car:
    def __init__(self, color="black"):
        self.color = color
```

# Récapitulatif

* Classe: plan de construction
* Object: ce qu'on crée avec le plan
* Instance: objet issue d'une classe
* Méthode: fonction dans une classe (qui prend `self` en premier argument)
* Attribut: variable dans un objet
