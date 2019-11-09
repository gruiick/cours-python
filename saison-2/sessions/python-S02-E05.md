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

# Aparté - le mot-clé `pass`

En Python, à cause de l'organisation en blocs indentés, on ne
peut pas vraiment avoir de blocs vides. Mais parfois, on
a besoin d'un bloc qui ne fasse rien.

Dans ce cas, on peut utiliser le mot-clé `pass`, par exemple
après un if:

```python
une_condition = False
if une_condition:
    pass
else:
    print("une_condition n'est pas vraie")
```

# Le mot-clé `pass` - 2

On peut aussi - et c'est l'usage le plus courant - utiliser `pass` pour
définir une fonction qui ne fait rien:

```python
def ne_fait_rien():
    pass
```

```python
>>> ne_fait_rien()
<rien>
```


# Changement de paradigme

Ce qu'on a vu jusqu’ici:

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

Une meilleure définition, c'est de dire que la programmation
orientée objet permet de mettre au même endroit:

* des données
* des fonctions qui opèrent sur ces données

L'important c'est que les deux aillent ensemble!

\vfill

*Note: ce n'est pas **la** meilleure définition de l'orienté objet, mais on s'en contentera
pour le moment ...*


# Les classes

On va parler *d'une* façon de faire de l'orienté objet: avec des classes.

Mais notez bien qu'on peut faire de l'orienté objet *sans* classes!

# Le plan de construction

Pour construire un objet en Python, on a besoin d'un *plan de construction*.

On appelle ce plan une *classe* et on la définit ainsi:

```python
class MonObjet:
    # du code ici
```

Comme les fonctions, les classes contiennent un *corps*, qui est le bloc *identé* en dessous
du mot-clé `class`, de nom de la classe et du `:` en fin de ligne

# Créons des objets

On peut faire un plan de construction vide avec le mot clé pass:

```python
class MonObjet:
    pass
```

Dans ce cas, on crée un objet en mettant le nom de la classe suivi d'une paire de parenthèses -
un peu comme pour appeler une fonction:

```python
>>> objet_1 = MonObjet()
```

Ici, `objet_1` est une *instance* de la classe `MonObjet`.

# Attributs

Les attributs sont des éléments **nommés** à *l'intérieur* d'un objet.

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

Ici, on crée une variable `func` qui prend la valeur de l'attribut `x` dans l'objet `a`, puis
on l'appelle avec l'argument `10` à la ligne suivante.

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
que cet attribut est une fonction qu'on peut appeler avec deux arguments.

On reviendra sur les modules dans un prochain chapitre.

# Attributs - 4

On peut *créer* des attributs dans *n'importe quel objet*, en utilisant l'*assignation*:

```python
>>> mon_instance = MonObjet()

# Création de l'attribut `x` dans `mon_instance`
>>> mon_instance.x = 42

# Accès à l'attribut `x` dans `mon_instance`
>>> mon_instance.mon_attribut
42
```

# Méthodes - définition

On peut aussi mettre des *méthodes* dans des classes.

On utilise `def`, comme pour les fonctions, mais les méthodes *doivent* avoir au
moins un argument appelé `self`, et être à l'intérieur du bloc de la classe:

```python
class MonObjet:
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

Notez qu'on ne passe *pas* d'argument quand on appelle `ma_méthode` depuis l'instance de l'objet.


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

Les méthodes peuvent aussi prendre plusieurs arguments, en plus de `self` - mais `self` doit
toujours être le premier argument.

Par exemple, pour créer un attribut avec une certaine valeur:


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

On prend souvent les *valeurs* des attributs à créer en arguments de la méthode `__init__ `.

```python
class MonObjet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Dans ce cas, les arguments de la méthode `__init__` apparaissent à l'intérieur des parenthèses après le
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
* `__init__`: méthode magique appelée automatiquement pendant l'instanciation


# Classes et programmation orienté objet

Ainsi, on peut ranger au même endroit des données et des fonctions opérant sur ces données.

Les données sont les attributs, et les fonctions opérant sur ces attributs sont les méthodes.

On peut ainsi séparer les *responsabilités* à l'intérieur d'un code en les répartissant
entres plusieurs classes.

# Encapsulation

Définition: cacher à l'utilisateur de la classe certains détails du
fonctionnement de celle-ci.

On parle souvent d'opposition entre code *public*, utilisable à l'extérieur,
de la classe, et code *privé*, utilisé à l'intérieur de la classe.

Ou encore *d'interface* et de *d'implémentation*.

# Exemple

```python
class MonObject:
    def __init__(self):
        # Notez le tiret bas en début
        # du nom de l'attribut
        self._mon_attribut_privé = ...

    def ma_méthode_publique(self):
        return self._mon_attribut_privé

>>> mon_objet = MonObject()
>>> mon_objet.ma_méthode_publique()
```

# Conventions

Notez que rien ne vous empêche d'écrire:

```python
>>> mon_objet= MonObjet()
>>> mon_objet._mon_attribut_privé = "une-autre-valeur"
```

mais alors vous n'êtes plus dans le cas d'usage prévu
par l'auteur de la classe MonObjet.

# Exemple d'usage - 1

Si `_mon_attribut_privé` demande de longs calculs, on peut envisager de stocker le résultat
de façon à ce que le deuxième appel à `ma_méthode_publique()` soit plus rapide.

De l'extérieur, l'appel à `ma_méthode_publique()` sera "magiquement" plus rapide la deuxième
fois :)

# Exemple d'usage - 2

```python
class MonObject:
    def __init__(self):
        self._mon_attribut_privé = None

    def ma_méthode_publique(self):
        if self._mon_attribut_privé is None:
            self._mon_attribut_privé = gros_calcul()
        else:
            return self._mon_attribut_privé

>>> mon_objet = MonObject()
>>> mon_objet.ma_méthode_publique()
# gros_calcul() est appelée
>>> mon_objet.ma_méthode_publique()
# retourne une valeur immédiatement!
```

#

\center \huge QCM

#

```python
def dire_bonjour():
    return "Bonjour"

dire_bonjour()
```

1. Erreur
2. Affiche "Bonjour"
3. N'affiche rien

\pause

Réponse: 3: la fonction retourne quelque chose,
mais on n'en fait rien

#

```python
def différencernce(x, y):
    return x - y

z = différence(y=4, x=5)
```

Que vaut `z`?

1. `1`
2. `-1`
3. Erreur

\pause

Réponse: 1 Quand on nomme les arguments, on les mets dans l'ordre qu'on veut.

#

```python
class MonObject:
    def ma_méthode():
        print("Bonjour")

mon_objet = MonObject()
mon_objet.ma_méthode()
```

1. Erreur
2. Affiche 'Bonjour'

\pause

Réponse 1: les méthodes prennent `self` en premier argument

#

```python
class MonObject:
    def ma_méthode():
        print("mon attribut est", self.mon_attribut)

mon_attribut = 42
mon_objet = MonObject()
mon_objet.ma_méthode()
```

1. Affiche "mon attribut est 42'
2. Erreur

\pause

Réponse 2: Les attributs doivent exister quand ils sont utilisés comme valeur

#

```python
class MonObject:
    def ma_méthode(self):
        print(self.mon_attribut)

mon_objet = MonObject()
mon_objet.mon_attribut = 42
mon_objet.ma_méthode()
```

1. Erreur
2. Affiche '42'

\pause

Réponse 2: On peut créer des attributs avec des assignations

#

```python
class MonObject:
    def ma_méthode(self):
        self.mon_attribut = 42
        print("mon attribut est", self.mon_attribut)

mon_objet = MonObject()
mon_objet.ma_méthode()
```

1. Affiche "mon attribut est 42'
2. Erreur

\pause

Réponse 1: On peut créer des attributs dans
des méthodes grâce à `self`.

#

```python
class MonObject:
    def __init__(self, valeur):
        self.mon_attribut = valeur

mon_objet = MonObject()
valeur = mon_objet.mon_attribut
print(valeur)
```

1. Erreur
2. Affiche '42'

\pause

Réponse 2: `__init__` est une méthode magique appelée automatiquement.

#

\center \huge Atelier

# Consignes

Vous êtes développeur dans une usine de fabrication de robots.

* Quand les robots sortent de la chaîne de montage, ils n'ont pas encore de nom
* La première fois qu'on démarre un robot, un nom est généré au hasard, avec
  le format suivant: deux lettres majuscules et trois chiffres. Par exemple:
  `RX837` ou `BC811`
* De temps en temps, les robots sont remis à aux paramètres d'usine, le nom
  est effacé et doit être regénéré

# Pour vous aider

* Un squelette `robot.py`, à récupérer sur `git.e2li.org`
* Contient déjà le `main()` de test - à vous d'implémenter la classe!


# Pour aller plus loin

* Le robot n'a pas le droit d'avoir deux fois le même nom. À vous de coder cela!

