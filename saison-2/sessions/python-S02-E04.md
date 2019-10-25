% Programmation avec Python (chapitre 3)
% Dimitri Merejkowsky


#

\center \huge Tout depuis le début

# Variables

```python
>>> a = 3
>>> b = 4
>>> a + b
7
```

# Maths

```python
>>> 10 / 3
3.3333333333333335  # flottant!
>>> 10 // 3
3  # division entière - quotient
>>> 10 % 3
1  # division entière - reste
```

# Comparaisons

```python
>>> a = 3
>>> b = 3
>>> a == b
True
>>> a < 3
False
```

# Blocs - if

```python
if a == 3:
    print("a égale 3")
else:
    print("a est différent de 3"
```

# Blocs - while

```python
i = 0
while i < 3:
    print(i)
    i =  i +1
```


# Blocs - break

```python
i = 0
while True:
    print(i)
    i = i + 1
    if i > 3:
        break
```

# Fonctions

```python
def additionne(x, y):
    return x + y

>>> additionne(3, 5)
8
```


# Portée des variables

```python
def additionne(x, y):
    return x + y

>>> x = 3
>>> additionne(x, 5)
8
```

# print

```python
a = 3
print("la valeur de a est", a, "!")
```

```text
la valeur de a est 3 !
```

```python
print("un message " , end="")
print("sur une seule ligne ", end="")
print("mais en plusieurs bouts")
```

```text
un message sur une seule ligne mais en plusieurs bouts
```

# input()

Lire une entrée utilisateur

```python
prénom = input("Entrez votre prénom: ")
```


# Listes

```python
une_liste_vide = []
deux_éléments = [1, 2]
```

# Itérer sur une liste

```python
for nom in ["Alice", "Bob", "Charlie"]:
    print(nom)
```

# Indexer une liste

```python
>>> joueurs = ["Alice", "Bob", "Charlie"]
>>> joueurs[0]
"Alice"
>>> joueurs[1]
"Bob"
>>> joueurs[2]
"Charlie"
```

# Modifier une liste

```python
>>> joueurs = ["Alice", "Bob", "Charlie"]
>>> joueurs[1] = "John"
>>> joueurs
["Alice", "John", "Charlie"]
```

# Test d'appartenance

```python
>>> joueurs = ["Alice", "Bob", "Charlie"]
>>> "Alice" in joueurs
True
>>> "Eve" in joueurs
False
```

# Dictionnaires

```python
un_dictionnaire_vide = {}
une_clé_une_valeur = { la_terre_est_plate: False }
scores = { "Alice": 20, "Bob": 14 }
```

# Indéxer un dictionnaire

```python
>>> scores = { "Alice": 20, "Bob": 14 }
>>> scores["Alice"]
20
>>> scores["Bob"]
14
```


# Modifier un dictionnaire

```python
>>> scores = { "Alice": 20, "Bob": 14 }

# mise à jour
>>> scores["Alice"] = 30
>>> scores
{ "Alice": 30, "Bob": 14 }

# insertion
>>> scores["Charlie"] = 23
>>> scores
{ "Alice": 30, "Bob": 14, "Charlie": 23 }
```

# Test d'appartenance

```python
>>> scores = { "Alice": 20, "Bob": 14 }
>>> "Alice" in scores
True
>>> "Eve" in scores
False
```

# Itérer sur les clés d'un dictionnaire

```python
scores = { "Alice": 20, "Bob": 14 }
for nom in scores:
    score = scores[nome]
    print(nom, "a un score de", score)
```

#

\center \huge Atelier

# Consignes

* Demander une longueur à l'utilisateur
* Afficher un sapin avec la bonne taille (ici, 7):

\vfill

```
   #
  ###
 #####
#######
   #
   #
```
