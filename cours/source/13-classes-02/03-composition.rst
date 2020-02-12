+++
title = "Composition"
weight = 3
+++

# Composition

## Définition

Une classe à l'intérieur d'une autre classe.

## Dépendances entre fonctions

Exemple: on veut dessiner un sapin dans le terminal:

```python
def main():
    largeur = demander_largeur()
    dessine_sapin(largeur)

main()
```


On voit que la fonction `dessine_sapin()` prend un argument `largeur`, qui est retourné
par la fonction `demander_largeur()`.

`dessine_sapin()` doit donc être appelée *après* `demander_largeur()`. On dit que `dessine_sapin()`
_dépend_ de `demander_largeur()`.

## Dépendances entre classes

Un bon moyen d'introduire une dépendance entre deux classes est d'utiliser les constructeurs.

Revoyons la classe Chat:

```python
class Chat:
    def __init__(self, nom):
        self.nom = nome
```

Comme le constructeur de la classe Chat prend un nom en argument, il est impossible de construire
des chats sans nom:

```python
>>> chat = Chat()
TypeError: __init__() missing 1 required positional argument: 'nom'
```

De la même façon, si on veut que tous les enfants aient un chat (pourquoi pas, après tout), on peut
avoir une classe Enfant, dont le constructeur prend une instance de chat en plus du prénom:

```python
class Enfant:
    def __init__(self, prénom, chat):
        self.prénom = prénom
        self.chat = chat

>>> alice = Enfant("Alice")
TypeError: __init__() missing 1 required positional argument: 'chat'

>>> boule_de_poils = Chat("Boule de Poils")
>>> alice = Enfant("Alice", boule_de_poils)
# OK!
```

## Utilisation de la composition

Maintenant qu'on vit dans un monde où tous les enfants ont chacun un chat, on peut
par exemple consoler tous les enfants en leur demandant de caresser leur chat, chat
qui va ronronner et faire plaisir à son propriétaire.

Voici comment on peut coder cela: d'abord, on rajoute les méthodes `caresse()`
et `ronronne()` dans la classe Chat:

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

Ensuite, on peut rajouter la méthode `console()` dans la classe Enfant,
qui va:

* récupérer l'instance de la classe Chat dans `self` - comme n'importe quel attribut
* puis appeler la méthode `caresse()` de cette instance

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

On dit parfois qu'on a *délégué* l'implémentation de la méthode `console()` de la classe Enfant
à la méthode `caresse()` de la classe Chat.
