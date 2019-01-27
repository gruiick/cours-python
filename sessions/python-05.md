% Programmation avec Python (chapitre 5)
% Dimitri Merejkowsky


#

\center \huge Suite de l'atelier précédent

# Rappel

Travail de la dernière fois.

Les problèmes que j'ai vu:

* noms
* méthodologie

#

\center \huge naming

# Quelques principes

* L'un des problèmes les plus compliqué de l'informatique

* Tout en Anglais
* Pas d'abbréviation
* Pas de redondance

# Exemples

* `get_freq` -> `get_frequencies`
* `nom_fich` -> `filename`
* `list_frag` -> `fragments`  # le pluriel nous dit que c'est une liste
* `liste_mot` -> `words`

Essayez de rester cohérents!

# Exemples (2)

```python
# Avant
for fragment in list_frag:
   fragment_min = fragment.lower()
   frag_clean = clean(fragment_min)
   liste_mot.append(frag_clean)
```

```python
# Après
for fragment in fragments:
   fragment = fragment.lower()
   fragment = clean(fragment)
   liste_mot.append(fragment)
```

On peut ré-utiliser le même nom plusieurs fois!

#

\center \huge Style

# Espaces

* Deux lignes entre chaque fonction
* Des espaces autour des `=` pour les affectations
* Pas d'espace quand c'est un argument nommé

#

\center \huge Repartons du début

# Découper les mots

Dans la liste se trouvent des mots mal découpés:

* `peutétre`
* `lhumanité`

Reprenons depuis le début

# Tester chaque fonction une par une

* Spécification
* Test
* Implémentation

# Découpage en fragments - spécification

On a:

> L'univers est, peut-être, « infini! »

On veut:

```python
["l", "univers", "est", "peut-être", '«',  "infini", '»']
```

On s'occupera d'enlever la ponctuation plus tard.

# Découpage en fragments - test

```python
contents = "L'unives est, peut-être, infini!"
fragments = split_fragments(contents)
print(fragments)
```

# Découpage en fragments - implémentation

```python
def split_fragments(contents):
    res = list()
    for fragment in contents.split():
        if "’" in fragment:
            (before, after) = fragment.split("’")
            res.append(before)
            res.append(after)
         else:
            res.append(fragment)
    return res
```

# Découpage en mots - spécification

On a:

```
L'unives est, peut-être, « infini! »
```

On veut:

```
['l', 'unives', 'est', 'peut-être', 'infini']
```

# Découpage en mots - test

```python
contents = "L'univers est, peut-être, « infini! »"
words = split_words(contents)
print(words)
```

# Découpage en mots - implémentation

On peut reprendre le code vu ensemble,
avec quelques modifications:

```python
def split_words(text):
   fragments = split_fragments(text)
   res = list()
   for fragment in fragments:
      fragment = fragment.lower()
      fragment = clean_fragment(fragment)
      if fragment:   # le fragment peut-être vide ici
         res.append(fragment)
   return res
```

# clean_fragment()

Juste une petite modification:

```python
def clean_fragment(fragment):
    result = ""
    for c in fragment:
        # autorise les tirets et apostrophes à l'intérieur
        # des mots
        if c.isalpha() or c in ["-", "'"]:
            result += c
    return result
```

# Calcul des fréquences - spécification

On a:

```python
["pomme", "poire", "banane", "poire", "banane", "banane"]`
```

On veut:

```python
{"pomme": 1, "poire": 2, "banane": 3}
```

\vfill

Note: par encore d'ordre ici!

# Calcul des fréquences - test


```python
words = [
   "pomme", "poire", "banane",
   "poire", "banane", "banane"
]
frequencies = get_frequencies(words)
print(frequencies)
```

# Calcul des fréquences - implémentation


```python
def get_frequencies(words):
   res = dict()
   for word in words:
      # Si le mot est déjà là, on incrémente
      # son compteur:
      if word in res:
         res[word] += 1
      else:
         # Sinon on crée une nouvelle clé
         # avec la valeur 1
         res[word] = 1
   return res
```


# Tri - spécification

On a:

```python
{'pomme': 1, 'poire': 2, 'banane': 3}
```

On veut:

```python
[
   (3, 'banane'),
   (2, 'poire'),
   (1 'pomme'),
]
```

# Tri - test

```python
frequencies = {'pomme': 1, 'poire': 2, 'banane': 3}
scores = get_scores(frequencies)
print(scores)
```


# Tri - implémentation

```python
def get_scores(frequencies):
   res = list()
   for word, count in frequencies.items():
      res.append((count, word))
   res.sort(reverse=True)
   return res
```

# Affichage des résultats

On a :

```python
scores = [
   (20, "banane"),
   (19, "poire"),
   ...
]
```

On veut:

```
20 banane
19 poire
```

# Affichage des résultats - test

```python
scores = [
   (20, "banane"),
   (19, "poire"),
   ...
]
print_scores(scores)
```

# Affichage des résultats - implémentation


```python
def print_scores(scores):
   for count, word in scores:
      print(count, word)
```

# Assemblons les morceaux

```python
def main():
   filename = "ruffin.txt"
   file = open(filename)
   contents = file.read()
   words = split_words(contents)
   frequencies = get_frequencies(words)
   scores = get_scores(frequencies)
   top_words = scores[:20]  # le top 20
   print_scores(top_words)

main()
```

# Touches finales

C'est bien si le nom du fichier est lu depuis la ligne de commande:

```python
import sys

def main():
   if len(sys.argv) < 2:
      sys.exit("not enough arguments")
   filename = sys.argv[1]
   ...
```

#

\center \huge Compléments
