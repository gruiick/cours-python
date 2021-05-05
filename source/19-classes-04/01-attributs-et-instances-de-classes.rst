Attributs et instances de classe
================================

Rappels
-------

Voici un exemple de classe qui contient une méthode::

   class MaClasse
       def ma_méthode(self):
            print(self.mon_attribut)


Le bloc indenté en-dessous du mot-clé ``class`` s'appelle le
*corps* de la classe. Et les méthodes sont définies avec le
mot-clé ``def`` dans le corps de la classe.

On dit que ce sont des *méthodes d'instance* par ce qu'il
faut créer une instance pour pouvoir les appeler::

    mon_instance = MaClasse()
    mon_instance.ma_méthode()


Attributs de classes
---------------------

On peut également déclarer des variables dans le corps d'une classe.

On crée ainsi des *attributs de classe*::

    class MaClasse:
        mon_attribut_de_classe = 42


Ici ``mon_attribut_de_classe`` existe *à la fois* dans les instances de ``MaClasse``
et dans la classe elle-même::

    print(MaClasse.mon_attribut_de_classe)
    # affiche 42
    mon_instance = MaClasse()
    print(mon_instance.mon_attribut_de_classe)
    # affiche 42


Un point important est que les attributs de classe sont *partagés* entre
toutes les instances. Voici un exemple d'utilisation possible::

    class Voiture:
        nombre_total_de_voitures_fabriquées = 0

        def __init__(self, marque, couleur):
            print("Construction d'une", marque, couleur)
            Voiture.nombre_total_de_voitures_fabriquées += 1


    ferrari_1 = Voiture("Ferrari", "rouge")
    mercedes_1  = Voiture("Mercedes, "noire")
    ferrari_2 = Voiture("Ferrari", "rouge")
    print("total:", Voiture.nombre_total_de_voitures_fabriquées)
    # Affiche:
    # Construction d'une Ferrari rouge
    # Construction d'une Mercedes noire
    # Construction d'une Ferrari rouge
    # total: 3

Notez que pour changer l'attribut de classe depuis une méthode, (comme dans le méthode
``__init__`` ci-dessus) on utilise le nom de la classe directement, et non pas ``self``.

Méthodes de classes
--------------------

On peut aussi définir des méthodes de classes avec le décorateur `classmethod`

Dans ce cas, le permier argument s'appelle ``cls`` et prend la valeur de la *classe*
elle-même. Pour poursuivre sur notre exemple::

    class Voiture:
        nombre_total_de_voitures_fabriquées = 0

        def __init__(self, marque, couleur):
            print("Construction d'une", marque, couleur)
            Voiture.nombre_total_de_voitures_fabriquées += 1

        @classmethod
        def fabrique_ferrari(cls):
            return cls("ferrari", "rouge")


    ferrari = Voiture.fabrique_ferrari()


Détaillons ce qu'il se passe sur la dernière ligne:
à gauche du égal il y a une variable et à droite une expression(``Voiture.fabrique_ferrari()``)

L'expression est constitué d'une classe à gauche du point  (``Voiture``) et
d'un attribut à droite du point ``fabrique_ferrari`` suivi de parenthèses.

Comme ``fabrique_ferrari`` est une méthode de classe, on va appeler la méthode
de classe ``fabrique_ferrari`` en lui passant la classe Courante en argument.

On arrive ainsi dans le corps de la méthode de classe ``fabrique_ferrari``, et
``cls`` vaut la classe `Voiture`.

Finalement, on évalue l'expression ``cls("ferrari", rouge")`` en remplaçant
``cls`` par sa valeur, ce qui donne ``Voiture("ferrari", "rouge")`` qui
correspond bien à ce qu'on obtient : une instance de la classe Voiture.
