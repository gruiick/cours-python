Chapitre 10 - Introduction aux classes
======================================

Ce qu'on a vu jusqu’ici :

* des types simples (entiers, booléens, ...) ;
* des structures de données (listes, dictionnaires, ...) ;
* des fonctions qui manipulent ces types ou ces structures de données ;
* ds fonctions qui s’appellent les unes les autres.

On appelle cet ensemble de concepts, cette façon d'écrire du code, un *paradigme*,
et c'est un paradigme *procédural*.

On va passer à un autre paradigme : *l'orienté objet*.

Orienté objet - une première définition
---------------------------------------

Un "objet" informatique *représente* un véritable "objet" physique
dans le vrai monde.

Ce n'est pas une très bonne définition :

1. Ce n'est pas nécessaire ;
2. Ce n'est même pas forcément souhaitable !

Je le mentionne juste parce que c'est une idée reçue très répandue.

Orienté objet - 2ème définition
-------------------------------

Une meilleure définition, c'est de dire que la programmation
orientée objet permet de mettre au même endroit :

* des données ;
* des fonctions qui opèrent sur ces données.

L'important c'est que les deux aillent ensemble !

*Note : ce n'est pas la meilleure définition de l'orienté objet, mais on s'en contentera pour le moment...*


Les classes
-----------

On va parler *d'une* façon de faire de l'orienté objet : avec des classes.

Mais notez bien qu'on peut faire de l'orienté objet *sans* classes !

Le plan de construction
-----------------------

On dit souvent qu'en Python, "tout est objet".

Pour bien comprendre cela, il faut d'abord parler des *classes* et des *instances de classes*.

Une classe est un *plan de construction*, et est définie avec le mot-clé ``class``, suivi
du nom de la classe : ::

    class MaClasse:
        # du code ici

Notez qu'on n'utilise pas le *snake case* pour les noms de classes, mais
le *Pascal Case* (ou *Camel Case*) : Le nom commence par une majuscule, et on alterne
minuscules et majuscules pour séparer les mots.

Comme les fonctions, les classes contiennent un *corps*, qui est le bloc *indenté* en dessous
du mot-clé ``class``, de nom de la classe et du ``:`` en fin de ligne.

Les classes sont utilisées pour construire des *instances*.

Créons des instances
--------------------

On peut faire un plan de construction vide avec le mot-clé ``pass`` : ::

   class MaClasse:
       pass

Dans ce cas, on crée une instance en mettant le nom de la classe suivi d'une 
paire de parenthèses, un peu comme pour appeler une fonction : ::

    mon_instance = MaClasse()

Ici, ``mon_instance`` est une *instance* de la classe ``MaClasse``. Notez que 
``mon_instance`` utilise *snake case*, comme toutes les variables qu'on a vues jusqu'ici.

Attributs
---------

Les attributs sont des éléments **nommés** à *l'intérieur* d'une instance.

On peut y accéder avec la syntaxe ``<instance>.<attribut>`` : ::

    y = a.x

Ici, ``y`` est l'attribut ``x`` de l'instance ``a``.

Les attributs peuvent être des fonctions : ::

   func = a.x
   func(10)

Ici, on crée une variable ``func`` qui prend la valeur de l'attribut ``x`` 
dans l'instance ``a``, puis on l'appelle avec l'argument ``10`` à la ligne suivante.

Le code suivant fait exactement la même chose, mais avec une ligne de moins : ::

    a.x(10)

On peut *créer* des attributs dans *n'importe quel instance*, en utilisant *l'assignation* : ::

   mon_instance = MaClasse()

   # Création de l'attribut `x` dans `mon_instance`
   mon_instance.x = 42

   # Accés à l'attribut `x` dans `mon_instance`
   print(mon_instance.x)
   # affiche: 42

Ici, on assigne la valeur ``42`` à l'attribut ``x`` de l'instance ``mon_instance``.

Méthodes - définition
---------------------

On peut aussi mettre des *méthodes* dans des classes.

On utilise le mot-clé ``def``, comme pour les fonctions, mais les méthodes *doivent* 
avoir au moins un argument appelé ``self``, et être à l'intérieur du bloc de la classe : ::

    class MaClasse:
        def ma_méthode(self):
            return 42

Notez que les méthodes *sont aussi des attributs*. Leur valeur est une *fonction*
qui se comporte légèrement différemment des fonctions qu'on a vu jusqu'ici.

Méthodes - appel
----------------

Une méthode ne peut être appelée que depuis une *instance* de la classe : ::

    class MaClasse:
        def ma_méthode(self):
                return 42

    ma_méthode()
    # erreur: NameError

    mon_instance = MaClasse()
    résultat = mon_instance.ma_méthode()
    print(résultat)
    # affiche: 42

Notez qu'on ne passe *pas* d'argument quand on appelle ``ma_méthode`` depuis l'instance.


Méthodes et attributs
---------------------

``self`` *prend la valeur de l'instance courante* quand la méthode est appelée.

On peut le voir en utilisant des attributs : ::

    class MaClasse:
        def affiche_attribut_x(self):
            # Accès à l'attribut `x` dans `self`
            print(self.x)


    mon_instance = MaClasse()
    mon_instance.x = 42
    mon_instance.affiche_attribut_x()
    # affiche: 42

On peut aussi *créer* des attributs dans une méthode : ::

    class MaClasse:
        def crée_attribut_x(self):
            self.x = 42
        def affiche_attribut_x(self):
            print(self.x)

    mon_instance = MaClasse()
    mon_instance.affiche_attribut_x()
    # erreur: `mon_instance` n'a pas d'attribut `x`

    mon_instance.crée_attribut_x()
    mon_instance.affiche_attribut_x()
    # affiche: 42

Les méthodes peuvent aussi prendre plusieurs arguments, en plus de ``self``, 
mais ``self`` doit toujours être le premier argument.

Par example, pour créer un attribut avec une certaine valeur : ::


    class MaClasse
        def crée_attribut_x(self, valeur_de_x):
            self.x = valeur_de_x

        def affiche_attribut_x(self);
            print(self.x)

    mon_instance = MaClasse()
    mon_instance.crée_attribut_x(42)
    mon_instance.affiche_attribut_x()
    # affiche: 42

Méthodes appelant d'autres méthodes
-----------------------------------

Comme les méthodes sont *aussi* des attributs, les méthodes d'une instance 
peuvent s'appeler les unes les autres : ::

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


    mon_instance = MaClasse()
    mon_instance.méthode_2()

.. code-block::

    la méthode 2 appelle la méthode 1
    démarrage de la méthode 1
    la méthode 1 affiche bonjour
    bonjour
    fin de la méthode 1
    fin de la méthode 2

Une méthode spéciale
--------------------

Si vous définissez une méthode nommée ``__init__``, celle-ci est appelée *automatiquement*
quand l'instance est construite.

On dit que c'est une méthode "magique" parce qu'elle fait quelque chose sans qu'on
l'appelle explicitement.

On utilise souvent ``__init__`` pour créer des attributs : ::


    class MaClasse:
        def __init__(self):
            self.x = 1
            self.y = 2

    mon_instance = MaClasse()

    # __init__ est appelée automatiquement!
    print(mon_instance.x)
    # affiche: 1
    print(mon_instance.y)
    # affiche: 2

On prend souvent les *valeurs* des attributs à créer en arguments de la méthode ``__init__`` : ::

    class MaClasse:
        def __init__(self, x, y):
            self.x = x
            self.y = y

Dans ce cas, les arguments de la méthode ``__init__`` apparaissent à l'intérieur 
des parenthèses après le nom de la classe : ::

    mon_instance = MaClasse(3, 4)
    print(mon_instance.x)
    # affiche: 3
    print(mon_instance.y)
    # affiche: 4

.. note::

   Pour cette  raison, ``__init__`` est souvent appelé le **constructeur** de la classe.

Les constructeurs en pratique
-----------------------------

Une bonne pratique consiste à créer *tous* les attributs nécessaires dans le constructeur.

Si les atttributs ont une valeur par défaut, ou une valeur initiale, on peut les créer
dans le constructeur directement.

Sinon, on créera l'attribut avec une valeur qui viendra d'un paramètre du constructeur (souvent
avec le même nom)

Premier example::

    class Point2D:
        # x et  y n'ont pas de bonne valeur par défault,
        # donc on utilise un constructeur qui prend
        # x et y en paramètre
        def __init__(self, x, y):
            self.x = x
            self.y = y

    origine = Point2D(0, 0)


Deuxième example::

    class Joueur:
        # Quand on crée un joueur, il a un score à 0
        def __init__(self, nom):
            self.nom = nom
            self.score = 0

    alice = Joueur("alice")


Récapitulatif
-------------

* Classe : plan de construction.
* Instance : valeur issue d'une classe.
* Attribut : variable dans une instance.
* Méthode : fonction dans une instance (qui prend `self` en premier argument).
* ``__init__`` : méthode magique appelée automatiquement pendant l'instanciation.


Classes et programmation orienté objet
--------------------------------------

Ainsi, on peut ranger au même endroit des données et des fonctions opérant sur ces données.

Les données sont les attributs, et les fonctions opérant sur ces attributs sont les méthodes.

On peut ainsi séparer les *responsabilités* à l'intérieur d'un code en les répartissant
entre plusieurs classes.

