% Programmation avec Python (chapitre 5)
% Dimitri Merejkowsky


#

\center \huge Rappels sur les fonctions

# Exemple 1

```python
# Définition d'une fonction sans arguments
def ma_fonction():
    print("ma_fonction commence ...")
    print("bonjour")
    print("ma_fonction finit.")

# Appel de la fonction `ma_fonction`:
>>> ma_fonction()
ma_fonction commence ...
bonjour
ma_fonction finit.
```

# Exemple 2

```python
# Définition d'une fonction avec un argument, x:
def ma_fonction(x):
    print("x vaut", x)

# Appel de la fonction `ma_fonction`:
>>> ma_fonction(42)
x vaut 42
```

# Changement de paradigme

Ce qu’on a vu jusqu’ici:

* Des types simples (entiers, booléens, ...)
* Des structures de données (listes, dictionnaires, ...)
* Des fonctions qui manipulent ces types ou ces types
* Des fonctions qui s’appellent les unes les autres

On appelle cet ensemble de concepts, cette façon d'écrire du code, un *paradigme* -
et c'est un paradigme *procédural*.

On va passer à un autre paradigme: l'*orienté objet*.

# Orienté objet - une première définition

Un "objet" informatique *représente* un véritable "objet" physique
dans le vrai monde véritable.

Ce n'est pas une très bonne définition:

1. Ce n'est pas nécessaire
2. Ce n'est même pas forcément souhaitable!

Je le mentionne juste parce que c'est une idée reçue très répandue.

# Orienté objet - 2ème définition

Mettre au même endroit:

* des données
* des fonctions qui opèrent sur ces données

L'important c'est que les deux aillent ensemble!


# Orienté objet - 3ème définition

Des "cellules" qui s'envoient des "messages".

Notamment, les cellules ne "voient" que leur état interne.

On peut envoyer un message d'une cellule à une autre *sans* connaître
beaucoup de détails à propos du destinataire du message.

On a déjà vu ce concepts avec des fonctions fonctionnant en mode
*boîte noire* du point de vue du code qui les appelle.


# Les classes

On va parler *d'une* façon de faire de l'orienté objet: avec des classes.

Mais notez bien qu'on peut faire de l'orienté objet *sans* classes!

# Le plan de construction

La seule chose dont on a besoin pour construire un objet, c'est d'un *plan de construction*.

On appelle ce plan une *classe* et on la définit ainsi:

```python
class MonObjet:
    pass
```

Ça ressemble un peu à la définition d'une fonction. Les noms des classes commencent souvent
par une majuscule.


# Créons des objets

On crée un objet en mettant le nom de la classe suivi d'une paire de parenthèses -
un peu comme pour appeler une fonction:

```python
>>> objet_1 = MonObjet()
```

Ici, `objet_1` est une *instance* de la classe `MonObjet`.

# Attributs

Les attributs sont des éléments _nommés_ "à l'intérieur" d'un objet.

On peut y accéder avec la syntaxe `<objet>.<attribut>`:

```python
y = a.x
```

Ici, `y` est l'attribut `x` de l'objet `a`.

# Attributs - 2

Les attributs peuvent être des fonctions:

```python
func = a.x
func(10)
```

Ici, on crée une variable `func` qui prend la valeur de l'attribut `x` dans `a`, puis
on l'appelle dans la ligne suivante.

Le code suivant fait exactement la même chose, mais avec une ligne de moins:

```python
a.x(10)
```

# Attributs - 3

On a déjà vu des attributs, quand on a utilisé des `modules`

```python
import random

nombre_au_hasard = random.randint(0, 10)
```

Ici, `random` est un module, et `randint` est un *attribut* du module `random`. Il se trouve
que cet attribut est un fonction qu'on peut appeler avec deux arguments.

On reviendra sur les modules dans un prochain chapitre.

# Attributs - 4

On peut *rajouter* des attributs à n'importe quel objet, en utilisant l'*assignation*:

```python
>>> mon_instance = MonObjet()

# Création de l'attribut `x dans `mon_instance`
>>> mon_instance.x = 42

# Accés à l'attribut `x` dans `mon_instance`
>>> mon_instance.mon_attribut
42
```

# Méthodes - définition

On peut aussi mettre des *méthodes* dans des classes.

On utilise `def`, comme pour les fonctions, mais les méthodes *doivent* avoir au
moins un argument appelé `self`, et être à l'intérieur du bloc de la classe:

```python
class MonObjet:
    # le bloc 'def' est a l'intérieur du bloc
    # de la classe
    def ma_méthode(self):
        return 42
```

# Méthodes - appel

Une méthode ne peut être appelée que depuis une *instance* de
l'objet:

```python
class MonObjet:
    def ma_méthode(self):
            return 42
>>> ma_méthode()
Erreur

>>> mon_instance = MonObjet()
>>> mon_instance.ma_méthode()
42
```

Notez qu'on ne passe *pas* d'argument quand on apelle `ma_méthode` depuis l'instance de l'objet.


# Méthodes et attributs - 1

`self` *prend la valeur de l'instance courante* quand la méthode est appelée.

On peut le voir en utilisant des attributs:

```python
class MonObjet:
    def affiche_attribut_x(self):
        # Accès à l'attribut `x` dans `self`
        print(self.x)


>>> mon_instance = MonObjet()
>>> mon_instance.x = 42
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes et attributs - 2

On peut aussi *créer* des attributs dans une méthode:

```python
class MonObjet:
    def crée_attribut_x(self):
        self.x = 42
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MonObjet()
>>> mon_instance.affiche_attribut_x()
# Erreur: `mon_instance` n'a pas d'attribut `x`

>>> mon_instance.crée_attribut_x()
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes et attributs - 3

Les méthodes peuveunt aussi prendre plusieurs arguments, en plus de `self` - mais `self` doit
toujours être le premier argument.

Par example, pour créer un attribut avec une certaine valeur:


```python
class MonObjet
    def crée_attribut_x(self, valeur_de_x):
        self.x = valeur_de_x

    def affiche_attribut_x(self);
        print(self.x)

>>> mon_instance = MonObjet()
>>> mon_instance.crée_attribut_x(42)
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes appelant d'autres méthodes - 1

Comme les méthodes sont *aussi* des attributs, les méthodes d'un objet peuvent s'appeler
les unes les autres:

```python
class MonObjet:
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

# Méthodes appelant d'autres méthodes - 2

```python
>>> mon_instance = MonObjet()
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

# Une méthode spéciale

Si vous définissez une méthode `__init__`, celle-ci est appelée *automatiquement*
quand l'objet est construit.

On dit que c'est une méthode "magique" parce qu'elle fait quelque chose _sans_ qu'on
l'appelle explicitement.

# \_\_init\_\_

On utilise souvent `__init__` pour créer des attributs


```python
class MonObjet:
    def __init__(self):
        self.x = 1
        self.y = 2

>>> mon_instance = MonObjet()

# __init__ est appelée automatiquement!
>>> mon_instance.x
1
>>> mon_instance.y
2
```

# \_\_init\_\_ - 2

On prend souvent les *valeurs* des attributs à créer en paramètres de la méthode `__init__ `.

```python
class MonObjet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Dans ce cas, les paramètres des `__init__` apparaissent à l'intérieur des parenthèses après le
nom de la classe:

```
>>> mon_instance = MonObjet(3, 4)
>>> mon_instance.x
3
>>> mon_instance.y
4
```

*Pour cette  raison, `__init__` est souvent appelé le _constructeur_ de la classe.*

# Récapitulatif

* Classe: plan de construction
* Objet: ce qu'on crée avec le plan
* Attribut: variable dans un objet
* Instance: objet issue d'une classe
* Méthode: fonction dans une classe (qui prend `self` en premier argument)
* `__init__`: méthode magique appelée automatiquement pendant l'instaciation
