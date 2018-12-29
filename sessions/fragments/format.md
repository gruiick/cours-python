% notions: string.format(), mini-language de specification de format

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

Ce n'est pas très lisible ...

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
