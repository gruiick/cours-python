% notions: tuples, immuables & mutables, passage par référence,
% copie, retour multiples

#

\center Les tuples


# Création de tuples


```python
mon_tuple = tuple()  # un tuple vide
mon_tuple = ()  # aussi un tuple vide
mon_tuple = (1, 2)  # un tuple à deux éléments
```

# Note

C'est la virgule qui fait le tuple, pas les parenthèses
(on n'utilise les parenthèse que pour l'esthétique)

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
print("{} de {}", v, c)
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

# Conclusion

Une fonction ne peut modifier la valeur de ses arguments qui s'ils sont
mutables.

Toutes les copies doivent être explicites
