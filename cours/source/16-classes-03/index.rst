Héritage
========

Rappel - composition
---------------------

Dans un chapitre précédent on a parlé de *composition* qui décrit une classe à l'intérieur
d'une autre classe.

Pour rappel::


    class Chat:
        def __init__(self, nom):
            self.nom = nom

        def ronronne(self):
            print(self.nom, 'fait: "prrrrr"')

        def caresse(self):
            self.ronronne()


    class Enfant:
        def __init__(self, prénom, chat):
            self.chat = chat

        def console(self):
            self.chat.caresse()



Vocabulaire
-----------

Ici on va parler d'héritage, qui décrit une autre relation entre classes, appelée parfois un peu abusivement "partage de code".

Pour indiquer qu'une classe ``B`` hérite d'une classe ``A``, on écrit ``A`` dans des parenthèses au moment de
déclarer la classe ``B``::

    class A:
       ...

    class B(A):
        ...


Les trois formulations suivantes sont souvent employées:

* A est la classe *parente* de B.
* B *hérite* de A.
* B est une classe *fille* de A.

Utilisation
-----------

Si une méthode n'est pas trouvée dans la classe courante, Python ira la
chercher dans la classe parente::

    class A:
       def méthode_dans_a(self):
           print("dans A")

    class B(A):
       def méthode_dans_b(self):
           print("dans B")


    b = B()
    b.méthode_dans_b()
    # Affiche: 'dans B', comme d'habitude

    b.méthode_dans_a()
    # Affiche: 'dans A'

Ordre de résolution
--------------------

S'il y a plusieurs classes parentes, Python les remonte toutes une à une.
On dit aussi qu'il y a une *hiérarchie* de classes::

    class A:
        def méthode_dans_a(self):
             print("dans A")

    class B(A):
        def méthode_dans_b(self):
             print("dans B")

    class C(B):
        def méthode_dans_c(self):
             print("dans C")

    c = C()
    c.méthode_dans_a()
    # affiche: 'dans A'

Avec \_\_init\_\_
--------------------

La résolution fonctionne pour toutes les méthodes, y compris ``__init__``::

    class A:
        def __init__(self):
             print("initialisation de A")

    class B(A):
        ...

    b = B()
    # affiche: "initialisation de A"

Attributs
----------

Même mécanisme pour les attributs::

    class A:
        def __init__(self):
            self.attribut_de_a = 42

    class B(A):
        ...

    b = B()
    print(b.attribut_de_a)
    # affiche: 42

Surcharge
----------

On peut aussi *surcharger* la méthode de la classe parente dans la classe fille::

    class A:
       def une_méthode(self):
           print("je viens de la classe A")

    class B(A):
        def une_méthode(self):
            print("je viens de la classe B")


    b = B()
    b.une_méthode()
    # affiche: "je viens de la classe B'

super()
-------

On peut utiliser ``super()`` pour chercher *explicitement* une méthode dans la classe parente::


    class A:
       def une_méthode(self):
           print("je viens de la classe A")

    class B(A):
        def une_méthode(self):
            super().une_méthode()
            print("je viens de la classe B")

    b = B()
    b.une_méthode()
    # affiche:
    # je viens de la classe A
    # je viens de la classe B

super() et \_\_init\_\_
------------------------

Erreur très courante::

    class A:
       def __init__(self):
           self.attribut_de_a = "bonjour"

    class B(A):
        def __init__(self):
           self.attribut_de_b = 42

     b = B()
     print(b.attribut_de_b)
     # affiche: 42
     print(b.attribut_de_a)
     # erreur:  AttributeError

On a surchargé ``A.__init__()``, du coup l'initialisation de A n'a jamais
été faite.

La plupart du temps, si ``A`` et ``B`` ont de constructeurs, on appellera
``super().__init__()`` dans le constructeur de la classe fille::

    class A:
       def __init__(self):
           self.attribut_de_a = "bonjour"

    class B(A):
        def __init__(self):
           super().__init__()
           self.attribut_de_b = 42

     b = B()
     print(b.attribut_de_b)
     # affiche: 42
     print(b.attribut_de_a)
     # affiche:  "bonjour"
