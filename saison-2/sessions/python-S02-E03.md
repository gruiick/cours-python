% Programmation avec Python (chapitre 3)
% Dimitri Merejkowsky


#

\center \huge Rappels chapitre 2

# Retour sur les listes - 1

```python
vide = []
deux_éléments = ["pomme", 42]
for fruit in ["pomme", "banane", "poire"]:
    print(fruit)
```

# Retour sur les listes - 2

Index valides: de 0 à (taille - 1)

```python
>>> fruits = ["pomme", "banane", "poire"]:
>>> fruits[1]
"banane"


>>> fruits[2] = "orange"
>>> fruits
["pomme", "banane", "orange"]
```

# Retour sur les listes - 3

```python
>>> fruits = ["pomme", "banane", "poire"]:
>>> len(fruits)
3
>>> "mandarine" in fruits
False
```
# Fonctions sans argument

*Définition*:
```python
def dire_bonjour():
    print("Bonjour")
```

\vfill

*Appel*:
```python
>>> dire_bonjour()
Bonjour
```

# Fonctions avec un argument

```python
def dire_bonjour(prénom):
    print("Bonjour", prénom)
```

\vfill

```python
>>> dire_bonjour("Bob")
Bonjour Bob
```

# Arguments par défaut

```python
def dire_bonjour(prénom, enthousiaste=False):
    message = "Bonjour " + prénom
    if enthousiaste:
        message += "!"
    print(message)
```

\vfill

# Appeler une fonction avec des arguments par défaut

```python
>>> dire_bonjour("John", enthousiaste=True)
Bonjour John!

>>> dire_bonjour("John", enthousiaste=False)
Bonjour John

>>> dire_bonjour("John")
Bonjour John
```

# Retourner une valeur


```python
def additionner(x, y):
    return x + y
```


```python
>>> a = 3
>>> b = 4
>>> c = additionner(a, b)
>>> c
7
```

# Portée des variables - 1

```python
def dire_bonjour(prénom):
    # prénom est une variable locale
    print("Bonjour " + prénom)

dire_bonjour("Dimitri")
print(prénom)
```

# Portée des variables - 2

```python
# salutation est une variable globale
salutation = "Bonjour "

def dire_bonjour(prénom):
    print(salutation + prénom)

dire_bonjour("Dimitri")
```


# Portée des variables - 3

```python
def dire_bonjour(prénom):
    print("Bonjour " + prénom)

prénom = "Dimitri"
dire_bonjour(prénom)
```

#

\center \huge None

# Définition

`None` est un "objet magique" natif en Python. Il est toujours présent, et il est unique.

Un peu comme `True` et `False` qui sont deux objets qui servent à représenter tous les booléens.

# Représenter l'absence

L'interpréteur intéractif n'affiche rien quand la valeur est None

```python
>>> a = 42
>>> a
42
>>> b = None
>>> b
```

# Retourner None

En réalité, *toutes* les fonctions pythons retournent *quelque chose*, même quand
elle ne contiennent pas le mot-clé `return`.

```python
def ne_renvoie_rien():
    print("je ne fais qu'afficher quelque chose")
```

```python
>>> resultat = ne_renvoie_rien()
"je ne fais qu'afficher quelque chose"
>>> resultat
```

# Opérations avec None

La plupart des fonctions que nous avons vues échouent si on leur passe None
en argument:

```python
>>> len(None)
TypeError: object of type 'NoneType' has no len()
>>> None < 3
TypeError: '<' not supported between instances of
  'NoneType' and 'int'
>>> int(None)
TypeError: int() argument must be a string,
  a bytes-like object or a number,
  not 'NoneType'
>>> str(None)
'None'
```

# Example d'utilisation:

```python
def trouve_dans_liste(valeur, liste):
    for element in liste:
        if element == valeur:
            return element
    return None
```

```python
>>> trouve_dans_liste(2, [1, 2, 3])
2
>>> trouve_dans_liste(False, [True, False])
False
>>> trouve_dans_liste(1, [3, 4])
```


# Example d'utilisation - 2

```python
def trouve_dans_liste(liste, valeur):
    for element in liste:
        if element == valeur:
            return element
```

None est Falsy, et on peut vérifier si une variable vaut None avec `is None`

```python
# hypothèse: `ma_valeur` n'est pas None
mon_element = trouve_dans_liste(ma_valeur, ma_liste)
if mon_element is None:
    print("élément absent de la liste")
if not mon_element:
    # Peut-être que l'élément n'était pas dans la liste,
    # ou peut-être y était-il, mais avec une valeur falsy
    ...
```
#

\center \huge Les dictionnaires

# Définition

Un dictionaire est une _association_ entre des clés et des valeurs.

* Les clés sont uniques
* Les valeurs sont arbitraires

# Création de dictionnaires

```python
# dictionaire vide
>>> {}

# une clé, une valeur
>>> {"a": 42}

# deux clés, deux valeurs
>>> {"a": 42, "b": 53}

# les clés sont uniques:
>>> {"a": 42, "a": 53}
{"a": 53}
```

Note: tous les dictionnaires sont truthy, sauf les dictionnaires vides.

# Accès aux valeurs

Avec `[]`, comme pour les listes, mais avec une *clé* à la place d'un *index*.

```python
>>> scores = {"john": 10, "bob": 42}
>>> scores["john"]
10
>>> scores["bob"]
42
>>> scores["charlie"]
KeyError
```

# Test d'appartenance

Avec `in`, comme le listes:

```python
>>> scores = {"john": 10, "bob": 42}
>>> "charlie" in scores
False
```

# Modifier la valeur d'une clé

Comme pour les listes: on assigne la nouvelle variable:

```python
>>> scores = {"john": 10, "bob": 42}
>>> scores["john"] = 20
>>> scores
{"john": 20, "bob": 42}
```

# Créer une nouvelle clé

Même méchanisme que pour la modification des clés existantes

```python
>>> scores = {"john": 10, "bob": 42}
>>> scores["charlie"] = 30
>>> scores
{"john": 20, "bob": 42, "charlie": 30}
```

*rappel*: ceci ne fonctionne pas avec les listes!
```python
>>> ma_liste = ["a", "b"]
>>> ma_liste[1] = "c" # ok
["a", "c"]
>>> ma_liste[3] = "d"
IndexError
```

# Itérer sur les clés

Avec `for ... in ...`, comme pour les listes

```python
scores = {"john": 10, "bob": 42}
for nom in scores:
	# `nom` est assigné à "john" puis "bob"
	score_associé_au_nom = scores[nom]
	print(nom, score_associé_au_nom)
```


# Détruire une clé

Avec `del` - un nouveau mot-clé:

```python
>>> scores = {"john": 10, "bob": 42}
>>> del scores["bob"]
>>> scores
{"john": 10}
```

# Détruire un élément d'une liste

```python

>>> fruits = ["pomme", "banane", "poire"]
>>> del fruits[1]
>>> fruits
["pomme", "poire"]
```

# Détruire une variable

```python
>>> mon_entier = 42
>>> mon_entier += 3
>>> mon_entier
45
>>> del mon_entier
>>> mon_entier == 45
NameError: name 'mon_entier' is not defined
```

# Détruire une fonction

On peu aussi supprimer des fonctions:

```python
def ma_fonction():
	print("bonjour")


del ma_fonction
>>> ma_fonction()
NameError: name 'ma_fonction' is not defined
```

# Des dictionnaires partout

Les variables globales d'un programme Python sont dans un dictionnaire,
accessible avec la fonction native `globals()`:

```python
$ python3
>>> globals()
{
 ...
 '__doc__': None,
 '__name__': '__main__',
 ...
}
```

On reparlera de `__doc__` et `__name__` un autre jour ...

# Des dictionnaires partout - 2

```python
$ python3
>>> a = 42
>>> globals()
{
 ...
 '__doc__': None,
 '__name__': '__main__',
 ...
 'a': 42
}
```

# Des dictionnaires partout - 3

```python
$ python3
>>> a = 42
>>> del globals()["a"]
>>> a
NameError: name 'a' is not defined
```

# Des dictionnaires partout - 4

On peut accéder aux variables locales d'une fonction avec `locals()`

```python
def ma_fonction():
    a =  42
    b = 3
    c = a + b
    print(locals())

>>> ma_fonction()
{'a': 42, 'b': 3, 'c': 45}
```

En revanche, il n'est pas conseillé de modifier le dictionaire renvoyé par `locals()` ...

#

\center \huge Les tuples

# Définition

Un tuple est un ensemble *ordonné* et *immuable* d'éléments. Le nombre, l'ordre et la valeur des objets sont fixes.

# Création de tuples

```python
# Un tuple vide
()

# Un tuple à un élément
(1,)   # notez la virgule

# Un tuple à deux éléments, aussi appelé couple
(1, 2)
```

Sauf pour le tuple vide, c'est la *virgule* qui fait le tuple

Note: tous les tuples sont truthy, sauf les tuples vides.

# Tuples hétérogènes

Comme les listes, les tuples peuvent contenir des éléments de types différents:

```python
# Un entier et une string
mon_tuple = (42, "bonjour")

# Un entier et un autre tuple
mon_tuple = (21, (True, "au revoir"))
```

# Accès

Avec `[]` et l'index de l'élément dans le tuple:

```python
mon_tuple = (42, "bonjour")
mon_tuple[0]
42
mon_tuple[1]
"bonjour"
```

# Modification

Interdit!

```python
mon_tuple = (42, "bonjour")
mon_tuple[0] = 44
TypeError: 'tuple' object does not support item assignment
```


# Test d'appartenance

Avec `in`

```python
>>> mon_tuple = (42, 14)
>>> 42 in mon_tuple
True
>>> 14 in mon_tuple
True
>>> 13 in mon_tuple
False
```

# Déstructuration

Créer plusieurs variables en une seule ligne:

```python
>>> couple = ("Batman", "Robin")
>>> héro, side_kick = couple
>>> héro
'Batman'
>>> side_kick
'Robin'
```


# Quelques erreurs classiques

```python
>>> héro, side_kick, ennemi = couple
ValueError (3 != 2)

>>> (héro,) = couple
ValueError (1 != 2)

# Gare à la virgule:
>>> héro, = couple
ValueError (1 != 2)
```

# Pièges

```python
f(a, b, c)   # appelle f() avec trois arguments

f((a, b, c)) # appelle f() avec un seul argument
             # (qui est lui-même un tuple à 3 valeurs)

f(())        # appelle f() avec un tuple vide


(a)      # juste la valeur de a entre parenthèses
(a,)     # un tuple à un élément, qui vaut la valeur de a
```

# On peut aussi déstructurer des listes

```python
>>> fruits = ["pomme", "banane", "orange"]
>>> premier, deuxième, troisième = fruits
>>> premier
"pomme"
>>> deuxième
"banane"
>>> troisième
"orange"
```
On dit aussi: unpacking

# Utilisations des tuples - 1

Pour simplifier des conditions:

```python
# Avant
if (
   ma_valeur == "nord" or
   ma_valeur == "sud" or
   ma_valeur == "ouest" or
   ma_valeur == "est"):
   		print("direction", ma_valeur)
```


\vfill

```python
# Après
if ma_valeur in ("nord", "sud", "est", "ouest"):
   		print("direction", ma_valeur)
```

# Pour retourner plusieurs valeurs

```python
def tire_carte():
    valeur = "10"
    couleur = "trèfle"
    return (valeur, couleur)

v, c = tire_carte()
print(v, "de", c)
# 10 de trèfle
```

Ce n'est pas une nouvelle syntaxe, juste de la manipulation de tuples!

#

\center \huge Atelier

#
Retour au pendu, mais cette fois nous voulons implémenter la gestion des high scores!

#

\center \huge Consignes pour travailler chez vous

# Préparation

* Récupérer l'archive `pendu-1.zip` dans la section Cours/Ateliers/Labos du site de l'ECL
* L'extraire dans un répertoire quelconque
* Se rendre dans ce répertoire et taper `python3.py pendu.py`
* Si tout va bien, le message 'bonjour' s'affiche



# Consignes

* Remplacer le code dans `main()` en appelant correctement les autres fonctions définies dans le ficher.
* Vérifier que le code fonctionne en jouant avec plusieurs noms différents.
* Envoyez votre code ou questions par mail à dimitri@e2li.org



