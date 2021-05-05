Couplage
========

Définition
----------

Un couplage décrit une relation entre deux classes.

Exemple
-------

Ici on veut représenter des chats et des humains qui adoptent (on non) des chats.
Tous les chats ont un nom, et tous les humains ont un prénom.

On peut utiliser pour cela deux classes: `Chat` et `Humain`::

    class Chat:
        def __init__(self, nom):
            self.nom = nom

    chat = Chat("Monsieur Moustaches")
    prin(chat.nom)
    # affiche: Monsieur Moustaches

    class Humain:
        def __init__(self,  prénom):
            self.prénom = prénom

    alice = Humain(prénom="Alice")
    print(alice.prénom)
    # affiche: Alice

Maintenant on veut que les humains puissent adopter des chats.
Pour cela, on peut rajouter la méthode ``adopte`` dans la classe
``Humain``.

Cette méthode va prendre un argument - une instance de la
classe ``Chat``::

    class Humain:
        def __init__(self,  prénom):
            self.prénom = prénom

        def adopte(self, chat):
            print(self.prénom, "adopte un chat")

    boule_de_poils = Chat("Boule de Poils")
    alice = Humain("Alice")
    alice.adopte(boule_de_poils)
    # affiche: "Alice adopte un chat"

On peut accéder au nom du chat depuis la méthode ``adopte``,
en utilisant la syntaxe ``nom.attribut`` vue précédemment::

    class Humain:
        def __init__(self,  prénom):
            self.prénom = prénom

        def adopte(self, chat):
            print(self.prénom, "adopte", chat.nom)

    boule_de_poils = Chat("Boule de Poils")
    alice = Humain("Alice")
    alice.adopte(boule_de_poils)
    # affiche: Alice adopte Boule de Poils

Couplage
--------

.. code-block::

   class Humain:
       ...
       def adopte(self, chat):
           print(self.prénom, "adopte", chat.nom)

Notez également que nous avons écrit ``chat.nom``. ainsi, la méthode ``adopte()``
ne peut être appelée que part une instance qui a un attribut ``nom`` - sinon
on aura une erreur.

Donc si on modifie la classe ``Chat`` et qu'on renomme l'attribut ``nom`` en ``surnom`` par exemple,
la méthode ``adopte()`` de la classe ``Humain`` cessera de fonctionner: on dit
qu'on a un *couplage* entre les classes ``Chat`` et ``Humain``.
