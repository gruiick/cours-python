+++
title = "Dictionnaires"
weight = 1
+++

# Dictionnaires

## Définition

Un dictionaire est une _association_ entre des clés et des valeurs.

* Les clés sont uniques
* Les valeurs sont arbitraires

## Création de dictionnaires

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

## Accès aux valeurs

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

## Test d'appartenance

Avec `in`, comme le listes:

```python
>>> scores = {"john": 10, "bob": 42}
>>> "charlie" in scores
False
```

## Modifier la valeur d'une clé

Comme pour les listes: on assigne la nouvelle variable:

```python
>>> scores = {"john": 10, "bob": 42}
>>> scores["john"] = 20
>>> scores
{"john": 20, "bob": 42}
```

## Créer une nouvelle clé

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

## Itérer sur les clés

Avec `for ... in ...`, comme pour les listes

```python
scores = {"john": 10, "bob": 42}
for nom in scores:
	# `nom` est assigné à "john" puis "bob"
	score_associé_au_nom = scores[nom]
	print(nom, score_associé_au_nom)
```


## Détruire une clé

Avec `del` - un nouveau mot-clé:

```python
>>> scores = {"john": 10, "bob": 42}
>>> del scores["bob"]
>>> scores
{"john": 10}
```

## Détruire un élément d'une liste

```python

>>> fruits = ["pomme", "banane", "poire"]
>>> del fruits[1]
>>> fruits
["pomme", "poire"]
```

## Détruire une variable

```python
>>> mon_entier = 42
>>> mon_entier += 3
>>> mon_entier
45
>>> del mon_entier
>>> mon_entier == 45
NameError: name 'mon_entier' is not defined
```

## Détruire une fonction

On peu aussi supprimer des fonctions:

```python
def ma_fonction():
	print("bonjour")


del ma_fonction
>>> ma_fonction()
NameError: name 'ma_fonction' is not defined
```

## Des dictionnaires partout

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


```python
$ python3
>>> a = 42
>>> del globals()["a"]
>>> a
NameError: name 'a' is not defined
```


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

