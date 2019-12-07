% Programmation avec Python (Épisode 7)
% Dimitri Merejkowsky


\center \huge Rappels


# Classes vides

Définition:
```python
class MaClasse:
    pass
```

Instanciation:
```python
>>> instance_1 = MaClasse()
```

# Attributs

Un attribut est une variable _à l'intérieur_ d'autre chose (par exemple une instance de classe).

```python
>>> mon_instance = MaClasse()
# création de l'attribut `x` dans mon_instance:
>>> mon_instance.x = 42
# accès à l'attribut `x` dans mon_instance:
>>> mon_instance.x
42
```

# Méthodes

Une méthode est une fonction définie à l'intérieur d'une classe:

Définition:
```python
class MaClasse:
    def ma_méthode(self):
        return 42
```

Les méthodes sont des attributs des instances de classes:

```python
class MaClasse:
    def ma_méthode(self):
            return 42
>>> ma_méthode()
Erreur
>>> mon_instance = MaClasse()
>>> mon_instance.ma_méthode()
42
```


# self

`self` *prend la valeur de l'instance courante* quand la méthode est appelée.

```python
class MaClasse:
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.x = 42
>>> mon_instance.affiche_attribut_x()
42
```

# self (2)

On peut aussi *créer* des attributs dans une méthode:

```python
class MaClasse:
    def crée_attribut_x(self):
        self.x = 42
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.affiche_attribut_x()
# Erreur: `mon_instance` n'a pas d'attribut `x`

>>> mon_instance.crée_attribut_x()
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes avec arguments

```python
class MaClasse
    def crée_attribut_x(self, valeur_de_x):
        self.x = valeur_de_x

    def affiche_attribut_x(self);
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.crée_attribut_x(42)
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes appelant d'autres méthodes

```python
class MaClasse:
    def méthode_1(self):
        print("démarrage de la méthode 1")
        print("la méthode 1 affiche bonjour")
        print("bonjour")
        print("fin de la méthode 1")


    def méthode_2(self):
        print("la méthode 2 appelle la méthode 1")
        self.méthode_1()
        print("fin de la méthode 2")
```


```python
>>> mon_instance = MaClasse()
>>> mon_instance.méthode_2()
```

```text
la méthode 2 appelle la méthode 1
démarrage de la méthode 1
la méthode 1 affiche bonjour
bonjour
fin de la méthode 1
fin de la méthode 2
```

# Constructeur sans arguments

Un constructeur en Python désigne la méthode nomée `__init__`,
quand celle-ci existe.

La méthode `__init__` est appelée automatiquement quand la
classe est instanciée:

```python
class MaClasse:
    def __init__(self):
        self.x = 1
        self.y = 2

>>> mon_instance = MaClasse()
>>> mon_instance.x
1
>>> mon_instance.y
2
```

# Constructeur avec arguments

La méthode `__init__` peut avoir des arguments,
dans ce cas, ceux ci doivent être fournis
lors de l'instanciation:

```python
class MaClasse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```python
>>> mon_instance = MaClasse(3, 4)
>>> mon_instance.x
3
>>> mon_instance.y
4
```

# Couplage (1)

## Définition

Un couplage décrit une relation entre deux classes.

## Exemple

Ici on veut représenter des chats et des humains qui adoptent (on non) des chats.
Tous les chats ont un nom, et tous les humains ont un prénom.

On peut utiliser pour cela deux classes: `Chat` et `Humain`:

# Couplage (2)


```python
class Chat:
    def __init__(self, nom):
        self.nom = nom

>>> chat = Chat("Monsieur Moustaches")
>>> chat.nom
'Monsieur Moustaches'
```

```python
class Humain:
    def __init__(self,  prénom):
        self.prénom = prénom
>>> alice = Humain(prénom="Alice")
>>> alice.prénom
"Alice"
```

#

Maintenant on veut que les humains puissent adopter des chats.
Pour cela, on peut rajouter la méthode `adopte` dans la classe
`Humain`.

Cette méthode va prendre un argument - une instance de la
classe `Chat`:

```python
class Humain:
    def __init__(self,  prénom):
        self.prénom = prénom

    def adopte(self, chat):
        print(self.prénom, "adopte un chat")

>>> boule_de_poils = Chat("Boule de Poils")
>>> alice = Humain("Alice")
>>> alice.adopte(boule_de_poils)
"Alice adopte un chat"
```

#

On peut accéder au nom du chat depuis la méthode `adopte`,
en utilisant la syntaxe `nom.attribut` vue précédemment:

```python
class Humain:
    def __init__(self,  prénom):
        self.prénom = prénom

    def adopte(self, chat):
        print(self.prénom, "adopte", chat.nom)

>>> boule_de_poils = Chat("Boule de Poils")
>>> alice = Humain("Alice")
>>> alice.adopte(boule_de_poils)
"Alice adopte Boule de Poils"
```

# Couplage

```python
class Humain:
    ...
    def adopte(self, chat):
        print(self.prénom, "adopte", chat.nom)
```

Notez également que nous avons écrit `chat.nom`. ainsi, la méthode `adopte()`
ne peut être appelée que part une instance qui a un attribut `nom` - sinon
on aura une erreur.

Donc si on modifie la classe `Chat` et qu'on renomme l'attribut `nom` en `surnom` par exemple,
la méthode `adopte()` de la classe `Humain` cessera de fonctionner: on dit
qu'on a un *couplage* entre les classes `Chat` et `Humain`.

# Couplage entre fonctions

```python
largeur = demander_largeur()
dessine_sapin(largeur)
```


\vfill

* `dessine_sapin()` prend un argument `largeur`, retourné par `demander_largeur()`.
* `dessine_sapin()` _dépend_ de `demander_largeur()`

# Dépendances entre classes (1)

```python
class Chat:
    def __init__(self, nom):
        self.nom = nome
```

On ne peut pas construire des chats sans nom:

```python
>>> chat = Chat()
TypeError: __init__() missing 1 required positional
          argument: 'nom'
```


# Dépendances entre classes (2)

Tous les enfants ont un chat!

```python
class Enfant:
    def __init__(self, prénom, chat):
        self.prénom = prénom
        self.chat = chat

>>> alice = Enfant("Alice")
TypeError: __init__() missing 1 required positional
           argument: 'chat'

>>> boule_de_poils = Chat("Boule de Poils")
>>> alice = Enfant("Alice", boule_de_poils)
# OK!
```

# Utilisation de la composition


```python
class Chat:
    def __init__(self, nom):
        self.nom = nom

    def ronronne(self):
        print(self.nom, 'fait: "prrrrr"')

    def caresse(self):
        self.ronronne()


>>> boule_de_poils = Chat("Boule de Poils")
>>> boule_de_poils.caresse()
Boule de Poils fait "prrrrr"
```

# Composition (2)

```python
class Enfant:
    def __init__(self, prénom, chat):
        self.chat = chat

    def console(self):
        self.chat.caresse()

>>> boule_de_poils = Chat("Boule de Poils")
>>> alice = Enfant("Alice", boule_de_poils)
# Alice est triste, on la console
>>> alice.console()
Boule de Poils fait "prrrrr"
# Alice est consolée :)
```
