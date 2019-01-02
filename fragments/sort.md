% notions: sort, lambdas, sort avec une fonction key()

# Trier des listes

# sort() - ordre naturel

```python
>>> nombres = [2, 3, 1, 5]
>>> nombres.sort()
>>> nombres
[1, 2, 3, 5]
```

Notez que la liste est modifiée *sur place*.

# sort() - ordre alphabétique

```python
>>> mots = ["abeille", "faucon", "chat"]
>>> mots.sort()
>>> mots
['abeille', 'chat', 'faucon']
```

# sort() - ordre lexicographique

Pour chaque "liste-élément" on compare le premier élément.
S'il y a égalité, on regarde le deuxième élément, etc:

```python
>>> composite = [["chat", 1], ["abeille", 2], ["chat", 3]]
>>> composite.sort()
>>> composite
[['abeille', 2], ['chat', 1], ['chat', 3]]
```

L'ordre alphabétique est l'ordre lexicographique pour les chaînes de caractères :)

# Attention!

Tous les éléments de la liste doivent être comparables deux à deux:

\vfill

```python
>>> mauvaise_liste = ["un", 2]
>>> mauvaise_liste.sort()
TypeError
```


# Comparer autrement

Exemple: trier les mots par leur taille avec l'argument `key`

\vfill

```python
def taille(mot):
    return len(mot)

mots = ["chat", "abeille", "faucon"]
mots.sort(key=taille)
>>> mots
["chat", "faucon", "abeille"]
```

# Lambda

Sert définir une fonction sans utiliser `def`

```python
>>> retourne_42 = lambda: 42  # pas d'argument
>>> retourne_42()
42
>>> ajoute_deux = lambda x: x + 2  # un seul argument
>>> ajoute_deux(3)
5
>>> multiplie = lambda x, y: x* y  # deux arguments
>>> multiplie(2, 3)
6
```
Note: le corps de la fonction doit tenir en une seule ligne

# Utilisation avec sort

```python
>>> mots = ["chat", "abeille", "faucon"]
>>> mots.sort(key=lambda x: len(x))
>>> mots
["chat", "faucon", "abeille"]
```
