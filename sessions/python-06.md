% Programmation avec Python (chapitre 6)
% Dimitri Merejkowsky


#

\center \huge Orienté objet et classes

# Un petit détour

Un nouveau built-in: `id()`

L'adresse de l'objet pointé par la variable:

```python
>>> a = 42532
>>> id(a)
94295009035968
>>> b = a
>>> id(b)   # même objet
94295009035968
>>> c = 42532  # objet différent
>>> id(c)
140400601470800
```

Notez bien les deux objets différents (le fait que
l'objet *pointé* ait la même valeur n'a pas d'importance)

# Paradigmes

Une façon d'envisager le code.
Pour l'instant on n'a vu que le paradigme *procédural* (ou impératif).

Il y en a plein d'autres! (*fonctionnel* notamment, dont on parlera un jour)

# Détails du procédural

* des types simples (entiers, booléens)
* des structures de données (dictionnaires, listes ...)
* des fonctions qui manipulent des types simples ou des structures
* les fonctions sont appelées les unes après les autres

Aujourd'hui on va parler de *l'orienté objet*, OOP en anglais (ou juste OO)

# Orienté objet - une mauvaise définition

Un "objet" informatique *représente* un véritable "objet" physique
dans le vrai monde véritable.

Ce n'est pas une très bonne définition:

1. Ce n'est pas nécessaire
2. Ce n'est même pas forcément souhaitable!

Je le mentionne juste parce que c'est une idée reçue très répandue.

# Orienté objet - 1ère définition

Mettre au même endroit:

* des données
* des fonctions qui opèrent sur ces données

L'important c'est que les deux aillent ensemble


# Orienté objet - 2ème définition

Des "cellules" qui s'envoient des "messages".

Notamment, les cellules ne "voient" que leur état interne.

On peut envoyer un message d'une cellule à une autre *sans* connaître
beaucoup de détails à propos du destinataire du message


# Les classes

On va parler *d'une* façon de faire de l'orienté objet: avec des classes.

Mais notez bien qu'on peut faire de l'orienté objet *sans* classes!

# Le plan de construction

La seule chose dont on a besoin pour construire un objet, c'est un plan.

On note le plan avec le mot-clé `class` et un nom:

```python
class MyObject:
    pass
```

La classe est le plan de construction de notre objet.

# Créons des objets

```python
>>> object_1 = MyObject()
```

Python ne sait rien de l'objet à part son adresse on mémoire et son nom:

```python
>>> id(object_1)
139993522758320
>>> print(object_1)
 <__main__.MyObject at 0x7f52c831e2b0>
```

On appelle `object_1` une *instance* de la classe `MyObject`.


# Créons d'autres objets

```python
>>> object_2 = MyObject()
>>> id(object_2)
140409432622920
>>> print(object_2)
<__main__.MyObject at 0x7fb39e5ac748>
```

Une autre adresse mémoire, donc un objet différent.

# Méthodes

Une fonction dans une classe:

```python
class MyObject:
    def my_method(the_object):
        print("hello", the_object)
```

\vfill

C'est tout!

# Méthodes - 2

La méthode n'existe pas en dehors de la classe - souvenez vous des cellules !

```python
>>> my_method()
NameError
>>> object = MyObject()
>>> object.my_method()
Hello, <MyObject at 0x7f52c9f6d6d8>
```

# Méthodes - 2

```.python
>>> object = MyObject()
>>> object
<MyObject at 0x7f52c9f6d6d8>
>>>> object.my_method()
Hello, <MyObject at 0x7f52c9f6d6d8>
```

Notez que `my_method` a pris en premier argument ce qu'il y avait *à gauche* du point.
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
TypeError: broken() takes 0 positional arguments
           but 1 was given
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
>>> object.attribute   # l'attribut n'existe pas
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
>>> object.print_attribute()  # l'attribut n'existe pas
AttributError
>>> object.attribute = 42
>>> object.print_attribute() # maintenant oui
42
>>> object.change_attribute(43)
>>> object.attribute
43
```

# Initialisation des attributs

Avec `__init__`:

* méthode "spéciale"
* appelée automatiquement
* notez les deux underscores avant et après ('dunder' en anglais)

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

#

\center \huge Modules

# Un fichier = un module

Et oui, vous faites des modules sans le savoir depuis le début :)

Un fichier `foo.py` correspond au module `foo`

# Attention

C'est pas tout à fait réciproque. Le module `foo` peut venir d'autre chose
qu'un fichier.

# Importer un module

Ou: accéder à du code provenant d'un *autre* fichier source.


```python
# Dans foo.py
a = 42
```

\vfill

```python
# Dans bar.py
import foo
print(foo.a)

```
\vfill

* Affiche '42'

# Espaces de noms
On dit aussi *namespace*.

Du point de vue de `bar.py`, `a` est dans l'*espace de nom* foo.

* On retrouve la syntaxe pour accèder à un attribut: `<variable>.<membre>`.
(ce n'est pas un hasard)

* Les namespaces sont automatiques en Python

# Importer dans le REPL

```python
# dans foo.py

def ma_fonction():
    return 42
```

```python
# dans le REPL
>>> import foo
>>> foo.ma_fonction()
42
```

* Plus sympa que de rajouter des `print()` à la fin de `foo.py` ;)

# Les imports ne sont faits qu'une seule fois

```python
# Dans foo.py
print("Je suis le module foo et tu viens de m’importer")

```

```python
>>> import foo
Je suis le module foo et tu viens de m’importer
>>> import foo
<rien>
```

On retrouve le concept de *cache*.

# Attention

Il faudra donc redémarrer le REPL à chaque fois que le code change.

Parfois, les gens conseillent d'utiliser `reload()` mais cette fonction n'est pas toujours fiable :/

# Importer juste une seule fonction ou variable

```python
# Dans foo.py
a = 42

def ma_fonction():
    return 43
```

\vfill

```python
# Dans bar.py
from foo import ma_fonction()
ma_fonction()
```

# Un raccourci

```
>>> from foo import *
>>> ma_fonction()
42
```

* Utile dans le REPL
* Pas une très bonne idée dans du vrai code
  * On perd la trace de où vient la variable
  * Possibilité de collisions de noms

# Retour sur les scripts

Un script, par opposition à un module n'est pas censé être importé.

Une solution est de mettre des tirets dans le nom:

```python
# Dans foo.py
import my-script

```

* Essaye de soustraire `script` à `my`
* ça ne fonctionne pas


# Retour sur main()

La méthode `main()` ne *doit* pas être exécutée quand on importe le code!

Solution:

```python
# Dans foo.py
def my_function():
    # Fonction utile qui peut être ré-utilisée

def main():
    # Fonction d'entrée principale
    # Utilise my_function()


# magie!
if __name__ == "__main__":
   main()
```


# Explication (partielle) de la magie

Le `if` n'est vrai *que* quand on lance `python3 foo.py`, mais pas quand on appelle `import foo` depuis
un autre module.

La variable magique `__name__` est égale au nom du module quand il est importé, et à la string `"__main__"` sinon.


# La librarie standard (1)

* Une collection de modules directement utilisables fournis à l'installation de Python.
* on a déjà vu `sys`, pour `sys.exit()` ou `sys.argv`

# La librarie standard (2)

Toute la librarie standard est documentée - même en Français.

https://docs.python.org/fr/3/library/index.html

* Gardez-là sous votre oreiller :)

# La librarie standard (3)

Beacoup de choses dedans. (*batteries included*)

De quoi faire de la manipulation de texte, des statistiques, du réseau, de la concurrence, etc ...


#

\center \huge  Atelier

# Jouons avec les API Web

API web: un serveur avec qui on peut parler depuis un programme.

Il en existe des quantités sur internet.

Aujourd'hui on va utiliser `numbersapi.com`

# Numbersapi

Example: On fait une requête sur `http://numbersapi.com/42`, on récupère du texte
contenant un fait intéressant (*trivia* en anglais) à propos du nombre 42 .

# Code de départ

Voir sur GitHub: https://github.com/E2L/cours-python/blob/master/sources/numbers/numbers_proc.py

```python
import sys
import urllib.request

def main():
    number = sys.argv[1]
    with urllib.request.urlopen("http://numbersapi.com/" + number) as request:
        response = request.read().decode("utf-8")
        print(response)


if __name__ == "__main__":
    main()

```

# Idée

* Transformer ceci en une classe réutilisable
* Gérer les faits mathématiques (avec une URL en http://numbersapi/42/math) en plus
  des trivias (avec une URL en http://numbersapi/42)

# Refactoring

Démo faite en cours.

# Extraction de variable

*avant*:
```python
with urllib.request.urlopen(
  "http://numbersapi.com/" + number) as request:
    ...
```

*après*:
```
url = "http://numbersapi.com/" + number
with urllib.request.urlopen(url) as request:
```


# Extraction de méthode - avant

```python
def get_trivia(self, number):
    url = "http://numbersapi.com/" + number
    with urllib.request.urlopen(url) as request:
        response = request.read().decode("utf-8")
        return response
```


# Extraction de méthode - après

```python
def build_url(self, number):
    return "http://numbersapi.com/" + number

def do_request(self, url):
    with urllib.request.urlopen(url) as request:
        response = request.read().decode("utf-8")
        return response

def get_trivia(self, number):
    url = self.build_url(number)
    return self.do_request(url)
```


# Code final

Voir sur GitHub:
https://github.com/E2L/cours-python/blob/master/sources/numbers/numbers_object.py


# Pour la prochaine fois - Exercice 1


Partir des sources dans le répertoire `hangman`:

https://github.com/E2L/cours-python/tree/master/sources/hangman

* Rajouter la gestion des scores (dans `scores.py`) au code exsistant
  du jeu du pendu (dans `hangman.py`)


* Refactorer en essayant d'introduire des classes

# Pour la prochaine fois - Exercice 2

Partir du code dans `numbers_object.py`, rajouter la getsion
des autres URL de http://numbersapi.com

# Des questions? Du code?

Envoyez-moi un e-mail à `d.merej@gmail.com` :)
