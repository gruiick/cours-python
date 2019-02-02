% Programmation avec Python (chapitre 5)
% Dimitri Merejkowsky


#

\center \huge Suite de l'atelier précédent

# Rappel

Travail de la dernière fois.

Les problèmes que j'ai vus:

* noms
* méthodologie

#

\center \huge naming

# Quelques principes

L'un des problèmes les plus compliqué de l'informatique

* Tout en anglais (sorry)
* Pas d'abréviation
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
   words.append(fragment)
```

On peut ré-utiliser le même nom plusieurs fois!

#

\center \huge Style

# Espaces - exemple

\vfill


```python
def foo(a, b):
    a = 42
    bar(a, spam=False)


def bar(a, spam=True):
    ...

```

# Espaces - règles


* Deux lignes entre chaque fonction
* Des espaces autour des `=` pour les affectations
* Pas d'espace quand c'est un argument nommé
* Exactement un espace après chaque virgule

Question de convention. Voir PEP8.

#

\center \huge Repartons du début

\normalsize (un genre de corrigé)

# Revoir les changements chez vous

Vous pourrez voir la suite des changements sur github:

https://github.com/E2L/cours-python/tree/master/sources/topwords/


# Note importante

En programmation, il y a très rarement une seule
bonne réponse !

Ceci n'est qu'une solution possible, et une *technique possible*
pour arriver à cette solution ...


# Découper les mots

Dans la liste se trouvent des mots mal découpés:

* `peutétre`
* `lhumanité`

Il faut revoir pas mal de code! (comme souvent après la découverte
d'un bug).

On va essayer d'être plus méthodique.

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

\center \huge Compléments - tris


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


# sorted()

Si on a besoin de l'ordre initial après coup:

```python
b = a.copy()
b.sort()

# ou:
b = sorted(a)
```

#


\center \huge Compléments - fichiers


# Rappel: lire

```python
file = open("toto.txt", "r")   # 'r' comme 'read'
contenu = file.read()
file.close()
```

Note: le fichier `toto.txt` doit exister!

# Écrire

On peut écrire tout le contenu d'un coup:

```python
contenu = "du texte à sauvegarder"
file = open("article.txt", "w") # 'w' comme 'write'
file.write(contenu)
file.close()
```


* Le fichier `article.txt` sera écrasé s'il existe déjà.
* N'oubliez surtout pas d'appeler `close()`

# Que faire en cas d'erreur ?

```python
file = open("article.txt", "w") # 'w' comme 'write'
# ... beacoup de code ici
# ... < une erreur
file.close()
```

S'il y a une erreur entre `open()` et `close()`, le fichier ne sera pas fermé!


# Le mot-clé with

```python
with open("toto.txt", "w") as file:
    file.write("du texte")
```

Quand on sort du bloc `with` on a la garantie que `file.close()` sera appelé,
*même* si on sort du bloc à cause d'une erreur.

# Convention

Il n'y a maintenant plus aucune raison d'appeler `.close()` "à la main",
donc ne le faites pas et utilisez `with`.

# Lire et écrire des lignes

Très courant:

```python
with open("toto.txt", "r") as file:
    lignes = file.readlines()

# faire quelque chose avec la liste de lignes

with open("toto.txt", "w") as file:
    file.writelines(lignes)
```

Pensez à fermer le premier fichier avant d'ouvrir le second.
(ça marche même s'ils ont le même nom)

#

\center \huge Atelier 2

# Problème à résoudre

Garder une liste de scores persistent dans
le jeu du pendu

# Point de départ

https://github.com/E2L/cours-python/tree/master/sources/hangman

* Version modifiée du pendu (grâce aux suggestions de certains
  d'entre vous)
* Préparation d'un squelette isolé
