% Programmation avec Python (chapitre 3)
% Dimitri Merejkowsky

\centering
Retours sur le chapitre 2

#

\centering
Retour sur les listes

# extend()

Pour concaténer des listes:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.extend(["orange", "abricot"])
>>> fruits
['pomme', 'banane', 'orange', 'abricot']
```
\vfill

Peut aussi s'écrire `+=`

```python
>>> nombres = [1, 2]
>>> nombres += [3, 4]
>>> nombres
[1, 2, 3, 4]
```

# pop()

`pop()` existe aussi pour les listes:

\vfill

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.pop()  # Retourne l'élément
'pomme'
>>> fruits  # Et modifie la liste
["banane"]

>>> vide = list()
>>> vide.pop()
IndexError
```

# clear()

Pour vider une liste:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.clear()
>>> fruits
[]
```

# index()

Pour récupérer la position d'un élément:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.index("banane")
>>> 1
>>> fruits.index("citron")
>> ValueError
```

# count()

Pour compter le nombre d'occurrences d'un élément

```python
>>> fruits = ["pomme", "banane", "pomme", "poire"]
>>> fruits.count("pomme")
2
>>> fruits.count("poire")
1
>>> fruits.count("citron")
0
```


# sort()

Pour trier une liste.

\vfill

* Par ordre naturel

```python
>>> nombres = [2, 3, 1, 5]
>>> nombres.sort()
>>> nombres
[1, 2, 3, 5]
```

\vfill

* Par ordre alphabétique

```python
>>> mots = ["abeille", "faucon", "chat"]
>>> mots.sort()
['abeille', 'chat', 'faucon']
```

# Ordre lexicographique

Pour chaque "liste-élément" on compare le premier élément.
S'il y a égalité, on regarde le deuxième élément, etc:

```python
>>> composite = [["chat", 1], ["abeille", 2], ["chat", 3]]
>>> composite.sort()
[['abeille', 2], ['chat', 1], ['chat', 3]]
```

\vfill

L'ordre alphabétique est l'ordre lexicographique pour les chaînes de caractères :)

# Attention!

```python
>>> mauvaise_liste = ["un", 2]
>>> mauvaise_liste.sort()
TypeError
```


# Comparer autrement

Trier les mots par leur taille

* Avec l'argument `key`

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

# Indexer des listes

Rappel:

```python
>>> lettres = ["a", "b", "c", "d", "e"]
>>> lettres[0]  # ça commence à zéro
"a"
>>> lettres[4]
"e"
```

Mais on peut aussi compter à l'envers:

```python
>>> lettres[-1]
"e"
>>> lettres[-2]
"d"
```

# Trancher des listes

Ou "faire des slices", ou "slicer".

```python
>>> lettres = ["a", "b", "c", "d", "e"]
>>> lettres[1:3]  # début (inclus), fin (non-inclus)
['b', 'c']
>>> lettres[:3] # début implicite
['a', 'b', 'c']
>>> lettres[3:] # fin implicite
['d', 'e']
>>> lettres[1:-2]  # fin négative
['b', 'c']
>>> lettres[:]  # une copie
['a', 'b', 'c', 'd', 'e']
```

#

\centering
Retour sur les strings

# index() et count() marchent aussi

```python
>>> message = "Bonjour, monde !"
>>> message.index("B")
0
>>> message.count("o")
3
```

# Trancher des chaînes de caractères

Ou slicer des strings:

\vfill

```python
>>> message = "Bonjour, monde !"
>>> message[1:4]
'onj'
>>> message[:7]
'Bonjour'
>>> message[9:-2]
'monde'
```


# Formater des chaînes de caractères

Problème:

\vfill

```python
>>> nom = "Ford"
>>> résultat = 42
>>> message = "Bonjour, " + nom + ". "
>>> message += "La réponse est: " + str(résultat) + "."
>>> message
'Bonjour, Ford. La réponse est: 42.'
```

\vfill

Ce n'est pas très lisible!

# format()

Solution: utiliser un "template" et la méthode `format()`

\vfill

```python
>>> nom = "Ford"
>>> résultat = 42
>>> template = "Bonjour, {}. La réponse est: {}"
>>> message = template.format(nom, résultat)
>>> message
'Bonjour, Ford. La réponse est: 42.'
```

# format() avancé

On peut aussi nommer les remplacements:

```python
template = "Bonjour, {nom}. La réponse est: {résultat}"
template.format(nom="Ford", résultat=42)
```

# format() avancé

On peut aussi faire des alignements et du "padding":

\vfill

```python
template = "{name:>10}: {score:03}"
print(template.format(name="Alice", score=42))
print(template.format(name="Bob", score=5))
```

```
     Alice: 042
       Bob: 005
```

# Explications

Le texte dans les accolades après le `:` est un mini-langage de spécification de format:

* `>10` signifie: "aligner a droite, taille maximale 10"
* `03` signifie: "rajouter des zéros en début de nombre jusquà atteindre 3 chiffres".

Plus de précisions dans la documentation:


\url{https://docs.python.org/fr/3/library/string.html#format-specification-mini-language}.
