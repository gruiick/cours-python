Composition
============


Définition
-----------

Une classe à l'intérieur d'une autre classe.

Dépendances entre fonctions
-----------------------------

Exemple ::

    def calcule_x():
        ...
        # du code ici

    def fait_un_truc_avec_x(x):
        ...
        # du code ici

    x = calcule_x()
    fait_un_truc_avec_x(x)



On voit que la fonction ``fait_un_truc_avec_x()`` prend un argument ``x``, qui est retourné
par la fonction ``calcule_x()``.

``fait_un_truc_avec_x()`` doit donc être appelée *après* ``calcule_x()``. On dit que ``fait_un_truc_avec_x()``
*dépend* de ``calcule_x()``.

Dépendances entre classes
-------------------------

Un bon moyen d'introduire une dépendance entre deux classes est d'utiliser les constructeurs.

Revoyons la classe Chat::

   class Chat:
       def __init__(self, nom):
           self.nom = nome

Comme le constructeur de la classe Chat prend un nom en argument, il est impossible de construire
des chats sans nom::

    chat = Chat()
    # erreur: TypeError: __init__() missing 1 required positional argument: 'nom'

De la même façon, si on veut que tous les enfants aient un chat (pourquoi pas, après tout), on peut
avoir une classe Enfant, dont le constructeur prend une instance de chat en plus du prénom::

    class Enfant:
        def __init__(self, prénom, chat):
            self.prénom = prénom
            self.chat = chat

     alice = Enfant("Alice")
     # erreur: TypeError: __init__() missing 1 required positional argument: 'chat'

     boule_de_poils = Chat("Boule de Poils")
     alice = Enfant("Alice", boule_de_poils)
     # OK!

Utilisation de la composition
-----------------------------

Maintenant qu'on vit dans un monde où tous les enfants ont chacun un chat, on peut
par exemple consoler tous les enfants en leur demandant de caresser leur chat, chat
qui va ronronner et faire plaisir à son propriétaire.

voici comment on peut coder cela: d'abord, on rajoute les méthodes ``caresse()``
et ``ronronne()`` dans la classe chat::

    class Chat:
        def __init__(self, nom):
            self.nom = nom

        def ronronne(self):
            print(self.nom, 'fait: "prrrrr"')

        def caresse(self):
            self.ronronne()


    boule_de_poils = Chat("Boule de Poils")
    boule_de_poils.caresse()
    # affiche: Boule de Poils fait "prrrrr"

Ensuite, on peut rajouter la méthode ``console()`` dans la classe Enfant,
qui va:

* récupérer l'instance de la classe Chat dans ``self`` - comme n'importe quel attribut
* puis appeler la méthode ``caresse()`` de cette instance::

    class Enfant:
        def __init__(self, prénom, chat):
            self.chat = chat

        def console(self):
            self.chat.caresse()

    boule_de_poils = Chat("Boule de Poils")
    alice = Enfant("Alice", boule_de_poils)
    # Alice est triste, on la console
    alice.console()
    # affiche: Boule de Poils fait "prrrrr"
    # Alice est consolée :)

On dit parfois qu'on a *délégué* l'implémentation de la méthode ``console()`` de la classe Enfant
à la méthode ``caresse()`` de la classe Chat.
