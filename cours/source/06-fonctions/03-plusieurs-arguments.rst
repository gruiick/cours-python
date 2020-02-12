+++
title = "Fonctions à plusieurs arguments"
weight = 2
+++

# Fonctions à plusieurs arguments

On peut mettre autant d'arguments qu'on veut, séparés
par des virgules:
```python
def afficher_addition(x, y):
	résultat = x + y
	print(résultat)
```

```python
>>> a = 4
>>> b = 5
>>> afficher_addition(a, b)
9
```

## Arguments nommés

En Python, on peut aussi utiliser le *nom* des arguments au lieu de
leur position:

```python
def dire_bonjour(prénom):
	print("Bonjour " + prénom)
```

```python
>>> dire_bonjour(prénom="Gertrude")
Bonjour Gertrude

>>> afficher_addition(y=3, x=4)
7
```


// TODO: soustraction

