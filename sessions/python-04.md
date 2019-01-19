% Programmation avec Python (chapitre 4)
% Dimitri Merejkowsky


#

\center \huge Les tuples

# Création de tuples


```python
mon_tuple = tuple()  # un tuple vide
mon_tuple = ()  # aussi un tuple vide
mon_tuple = (1, 2)  # un tuple à deux éléments
```

# Note

C'est la virgule qui fait le tuple, pas les parenthèses
(on n'utilise les parenthèses que pour l'esthétique)

\vfill

```python
(1)
# pas un tuple, juste le nombre 1 (entre parenthèses)
(1,)
# un tuple à un élément
1,
# le *même* tuple
```

# Indexation, test d'appartenance

```python
>>> couple = ('Starsky', 'Hutch')
>>> couple[0]
'Starsky'
>>> couple[1]
'Hutch'
>>> couple[3]
IndexError


>>> 'Starsky' in couple
True
>>> 'Batman' in couple
False
```

Rien de nouveau en principe :p

# Déstructuration

Créer plusieurs variables en une seule ligne

```python
>>> couple = ("Batman", "Robin")
>>> héro, side_kick = couple
>>> héro
'Batman'
>>> side_kick
'Robin'
```

On dit aussi: unpacking

# Quelques erreurs

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
```

# On peut aussi déstructurer des listes

```python
>>> fruits = ["pomme", "banane", "orange"]
>>> premier, deuxième, troisième = fruits
```

# Retour multiple

Retourner plusieurs valeurs:

```python
def tire_carte(():
    valeur = "10"
    couleur = "trèfle"
    return (valeur, couleur)

(v, c) = tire_carte()
print(v, "de", c)
# 10 de trèfle
```

\vfill

En fait c'est juste une manipulation de tuples :)

# Les tuples sont immuables

```python
>>> couple = ('Starsky', 'Hutch')
>>> couple[0] = 'Batman'
TypeError
```

Les méthodes `count()` et `index()` existent
parce qu'elles ne modifient pas le tuple.

# Les tuples sont immuables (2)

Les méthodes qui modifieraient le tuple n'existent pas:

```python
>>> couple = ('Starsky', 'Hutch')
>>> couple.clear()
AttributeError
```

#

\center Mutables, immuables, et références

# Mutables et immuables

* Mutables: listes, ensembles, dictionnaires
* Immuables: entiers, flottants, booléens, strings

# Passage par référence

En Python, on ne manipule jamais les objets directement, on
ne manipule que des *références* sur ces objets.

```python
x =  3  # x est une référence vers l'objet 'entier 3'
x = "hello" # x référence une string
```

# Exemple 1

```python
def ajoute_trois(x):
    x = x + 3   # crée une nouvelle référence

mon_entier = 42
ajoute_trois(mon_entier)
# 'mon_entier' vaut toujours 42
```

# Exemple 2

```python
def ajoute_trois(l):
    l.append(3)
    # Ne crée pas de nouvelle référence
    # Appelle une méthode qui modifie 'l' sur place

ma_liste = [1, 2]
ajoute_trois(ma_liste)
# 'ma_liste' vaut maintenant [1, 2, 3]
```

# Exemple 3

```python
def get_max(liste):
    autre_liste = liste.copy()
    autre_liste.sort()
    return autre_liste[-1]

ma_liste = [1, 3, 2]
x = get_max(ma_liste)
# x = 3
# `ma_liste` n'a pas changé
```

# Notes

* on peut aussi utiliser la fonction native "max()"
* on peut aussi utiliser une slice: `autre_liste = liste[:]`


# Valeur par défaut

```python
def exemple_bizarre(l=[1, 2, 3]):
    l.append(4)
    return l

>>> exemple_bizarre()
[1, 2, 3, 4]
>>> exemple_bizarre()
[1, 2, 3, 4, 4]
```

* Les arguments par défaut ne sont évalué qu'une seule fois

# Valeur par défaut (2)

Parfois, ce comportement *peut* être voulu

\vfill

```python
def grosse_fonction(x, cache=dict()):
    if x in cache:
        return cache[x]
    else:
        resultat = ... # plein de calculs
        cache[x] = resultat
        return resultat
```

# Valeur par défaut (3)

Sinon, remplacez l'argument mutable par un argument immutable

```python
def exemple_bizarre(l=None):
    if not l:
        l = [1, 2, 3]
    l.append(4)
    return l

>>> exemple_bizarre()
[1, 2, 3, 4]
>>> exemple_bizarre()
[1, 2, 3, 4, 4]
```

# Conclusions

* Une fonction ne peut modifier la valeur de ses arguments qui s'ils sont
mutables.

* Toutes les copies doivent être explicites

#

\center \huge Itérer sur les dictionnaires


# Itérer sur les clés

```python
scores = { "alice": 3, "bob": 4 }
for prénom in scores:
    score = scores[prénom]
    print(prénom, score)
```

\vfill
Même chose avec la méthode `.keys()`

```python
for prénom in scores.keys():
    ...

```

# Itérer sur les valeurs

```python
scores = { "alice": 3, "bob": 4 }
for score in scores.values():
    print(score)
```

# Itérer sur les clés *et* les valeurs

```python
for (prénom, score) in scores.items()
    print(prénom, score)
```

\vfill

Notes:

* on a gagné une ligne par rapport au premier exemple.
* `items()` renvoie une liste de tuples

# Presque des listes

Les méthodes `.keys()`, `.values()` et `.items()` ne retournent pas des listes,
mais des "vues".

```python
>>> prénoms = scores.keys()
>>> prénoms[1]
TypeError: 'dict_keys' object does not support indexing
```

\vfill

On détaillera cette question plus tard.

# Forcer des listes

En attendant, vous pouvez convertir les vues en listes:

```python
>>> prénoms = scores.keys()
>>> premier_prénom = list(prénoms)[0]
```

#

\center \huge La programmation n'est pas un art solitaire

# Le mythe

> Un développeur dans son garage a une idée géniale,
> l'implémente tout seul et gagne un tas de pognon.

\vfill

Ça n'existe pas (ou plus)


* Sauf dans les fictions
* Quasiment mon seul reproche à propos de la série *Silicon Valley*

# La code review

Ce qu'on a fait avec l'exercice de la dernière fois :)

# Par mail - envoi

```text
Bonjour Alice, voici une nouvelle fonction:

def ma_fonction():
    ma_liste = ...

    if len(ma_liste) == 0:
        # la liste est vide



signé: Bob
```

# Par mail - réponse

```text
Bonjour Bob, et merci pour ta contribution!

def ma_fonction():
    ma_liste = ...

    if len(ma_liste) == 0:
        # la liste est vide
        >> Ici tu pourrais mettre `if not ma_liste`


signé Alice
```

# Par mail - envoi 2

```text
Bonjour Alice, voici le code corrigé:

def ma_fonction():
    ma_liste = ...

    if not ma_liste:
        ...
```

# Code review

Croyez-le ou nom, plein de projets fonctionnent comme ça.

Pas d'outil spécifiques, on peut tout faire avec des e-mail
et du texte brut.

Et c'est souvent comme ça qu'on contribue à du code open-source.

# D'autres outils

Des outils essayent de "simplifier" le processus. En vrac: `gerrit`, `github`, `gitlab`, `bitbucket`, `phabricator` ...

\vfill

Mais dans son essence le concept n'a pas changé

#

\center \huge Un atelier

# Mob programming

Ou programmation en foule

# Les règles

* Un pilote: le seul autorisé à modifier le code
* Un copilote: indique au pilote quoi faire
* On tourne toutes les 15 minutes

# Le challenge

On va prendre deux discours politique et faire de l'analyse automatique de texte dessus.

Notamment, repérer les mots qui reviennent le plus

# Jean Véronis - aparté

Un universitaire malheureusement décédé s'en était fait une spécialité.

Vous pouvez lire *Les Mots du Président* si ça vous dit.

Il utilisait d'autres outils, bien sûr, mais ce qu'on va faire n'est pas si loin

#

\center \huge Let's go!

#

#


\center \huge Lire et écrire des fichiers

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
donc ne le faites pas ...

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
