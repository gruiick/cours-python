+++
title = "Fonctions natives"
weight = 5
+++

# Fonctions natives

Fonctions qui sont toujours présentes dans l'interpréteur. On en a déjà vu quelques unes:

* `print`, `input`: écrire et lire sur la ligne de commande
* `str`, `int`: convertir des entiers en strings et vice-versa

Il y en a tout un tas!

La liste ici:  https://docs.python.org/fr/3/library/functions.html#built-in-funcs

## Retour sur print

On peut passer autant d'arguments qu'on veut à `print` et:

* Il les sépare par des espaces
* Ajoute un retour à la ligne à la fin:

```python
>>> prénom = "Charlotte"
print("Bonjour", pŕenom)
Bonjour Charlotte
```

On peut demander à `print` de changer son séparateur:

```python
>>> a = "chauve"
>>> b = "souris"
>>> print(a, b, sep="-")
chauve-souris
```

Ou de changer le caractère de fin:
```python
>>> print("Ceci tient", end="")
>>> print("sur une seule ligne")
Ceci tient sur une seule ligne
```


