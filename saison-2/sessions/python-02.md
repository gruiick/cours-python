% Programmation avec Python (chapitre 2)
% Dimitri Merejkowsky


#

\center \huge Rappels

# Variables

```python
score = 2             # un entier
taille = 1.85         # un flottant
message = "bonjour!"  # une string
```

# Opérations mathématiques

* `+`, `*`, `-`, `/`
```python
x = 3
y = 5
x + y   # 8
```

* `//` et `%`
```python
14 // 3   # 4
14 % 3    # 2
```

# Opérations avec les strings

* Concaténation:
```python
nom = "Bob"
message = "Bonjour " + nom
"Bonjour Bob"
```

* Conversions:
```python
score = 42
message = "votre score est: " + str(score)
```

```python
print("Entrez votre age")
réponse = input()
age = int(réponse)
```

# Booléens et tests

```python
a = 3
b = 4
a > b   # False

c = 3
a == b  # True
```

# Tester une condtion avec if

```python
a = 3
b = 4
if a == b:
    print("a et b sont égaux")
print("on continue")
```


# Tester une condition avec if et else

```python
a = 3
b = 4
if a == b:
    print("a et b sont égaux")
else:
    print("a et b sont différents")
print("on continue")
```

# Tester des conditions avec if, else et elif

```python
if age < 10:
	print("inférieur à dix")
elif 10 <= age < 20:
	print("âge entre 10 et 20")
elif 20 <= age < 40:
	print("âge entre 20 et 40")
else:
	print("âge supérieur à 40")
```

# Boucler sur une condition avec while

```python
i = 0
while i < 3:
    print(i)
    i = i + 1
```

```
0
1
2
```

# Sortir d'une boucle avec if et break

```python
i = 0
while True:
    i = i + 1
    print(i)
    if i > 3:
        break
```

#

\center \huge Compléments


# Combiner assignation et opérations

`a += b` est équivalent à `a = a +b`

```python
>>> a = 3
>>> a = a + 1
>>> a
4

>>> a = 3
>>> a += 1
>>> a
4
```


# Gérer les retours à la ligne

`\n` sert à échapper les retours à la ligne:

```python
>>> texte = "Je suis un message\nsur deux lignes"
>>> print(texte)
Je suis un message
sur deux lignes
>>>
```

# Concaténation de littéraux

Pas besoin de `+` pour concaténer des "littéraux".

```python
>>> text = "Je suis une " "longue" " string"
>>> text
'Je suis une longue string'
```

# Répétition

```python
>>> "argh " * 3
'argh argh argh'
```

# Une longue string sur plusieurs lignes

```python
poème = """
Ceci est un poème

Qui contient "des quotes"
Et parle d'autre choses ...
"""
```
#

\center \huge Fonctions


# Fonction sans argument

Définition:
```python
def dire_bonjour():
    print("Bonjour")
```

* avec `def`
* avec un `:` à la fin et un _bloc indenté_ (appelé le "corps")

\vfill

Appel:
```
>>> dire_bonjour()
Bonjour
```

* avec le nom de la fonction et des parenthèses

# Le pouvoir des fonctions

Ici on vient de créer une nouvelle fonctionnalité
à Python. Avant qu'on définisse la fonction
`dire_bonjour()`, il ne savait pas dire bonjour,
il savait uniquement afficher des messages à
l'écran.

On dit qu'on a _créé une abstraction_. Et
c'est une technique extrêmement utile en
programmation.


# Fonction avec un argument

Définition: avec l'argument à l'intérieur des parenthèses

```python
def dire_bonjour(prénom):
	print("Bonjour " + prénom)
```

\vfill

Appel: en passant une variable ou une valeur dans les parenthèses

```python
>>> dire_bonjour("Germaine")
Bonjour Germaine

>>> prénom_de_charlotte = "Charlotte"
>>> dire_bonjour(prénom_de_charlotte)
Bonjour Charlotte
```

# Exécution d'une fonction

C'est exatement comme si on assignait les arguments de la fonction avant d'éxécuter le code
dans le corps

```python
# Ceci:
dire_bonjour("Dimitri")

# Est équivalent à cela:
prénom_de_dimitri = "Dimitri"
print("Bonjour " + prénom_de_dimitri)

# Lui-même équivalent à:
print("Bonjour " + "Dimitri")
```

# Portée des variables - 1

Les arguments d'une fonction n'existent que dans le corps de celle-ci

```python
def dire_bonjour(prénom):
	print("Bonjour " + prénom)

dire_bonjour("Dimitri") # Ok
print(prénom)  # Erreur
```

# Portée des variables - 2

Les variables en dehors des fonctions sont disponibles partout:

```python
salutation = "Bonjour "

def dire_bonjour(prénom):
	print(salutation + prénom)

dire_bonjour("Dimitri")
```

# Portée des variables - 3

Une variable peut avoir en "cacher" une autre si elle a une portée différente

```python
def dire_bonjour(prénom):
	print("Bonjour " + prénom)   # portée: uniquement dans
								 # le corps dire_bonjour

prénom = "Dimitri"  # portée: dans tout le programme
dire_bonjour(prénom) # Ok
```

# Fonction avec plusieurs arguments

On peut mettre autant d'arguments qu'on veut, séparés
par des virgules:
```python
def afficher_addition(x, y):
	résultat = x + y
	print(résultat)
```

\vfill

```python
>>> a = 4
>>> b = 5
>>> afficher_addition(a, b)
9
```

# Arguments nommés

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

# Arguments par défaut

On peut aussi mettre des valeurs par défaut:

Définition:
```python
def dire_bonjour(prénom, enthousiaste=False):
	message = "Bonjour " + prénom
	if enthousiaste:
		message += "!"
	print(message)
```

\vfill

Appel:
```python
>>> dire_bonjour("Thomas", enthousiaste=True)
Bonjour Thomas!
>>> dire_bonjour("Thomas", enthousiaste=False)
Bonjour Thomas
>>> dire_bonjour("Thomas")
Bonjour Thomas
```

# Fonctions natives

Fonctions qui sont toujours présentes dans l'interpréteur. On en a déjà vu quelques unes:

* `print`, `input`: écrire et lire sur la ligne de commande
* `str`, `int`: convertir des entiers en strings et vice-versa

Il y en a tout un tas!

La liste ici:  https://docs.python.org/fr/3/library/functions.html#built-in-funcs

# Retour sur print

On peut passer autant d'arguments qu'on veut à `print` et:

* Il les sépare par des espaces
* Ajoute un retour à la ligne à la fin:

```python
>>> prénom = "Charlotte"
print("Bonjour", pŕenom)
Bonjour Charlotte
```

# Retour sur print

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

# Retourner des valeurs

Définition avec le mot `return`

```python
def additionner(x, y):
	return x + y
```

\vfill

Récupérer la valeur de retour
```python
>>> a = 3
>>> b = 4
>>> c = additionner(a, b)   # encore une assignation
>>> c
7
```

# Sortir d'une fonction avec return

`return` interrompt également l'éxécution du
corps de la fonction:

```python
def dire_bonjour(prénom, première_fois=False):
	print("Bonjour", prénom)
	if not première_fois:
		return
	print("Heureux de faire votre connaissance")
```

\vfill

```python
>>> dire_bonjour("Dimitri", première_fois=True)
Bonjour Dimitri
Heureux de faire votre connaissance
>>> dire_bonjour("Dimitri", première_fois=False)
Bonjour Dimitri
```

#

\center \huge Listes

# Définition

Une liste est une _suite ordonée_ d'éléments.

# Créer une liste

Avec `[]`, et les élements séparés par des virgules:

```python
liste_vide = []
trois_entiers = [1, 2, 3]
```


# Listes hétérogènes

On peut mettre des types différents dans la même liste

```python
ma_liste = [True, 2, "trois"]
```

\vfill

On peut aussi mettre des listes dans des listes:

```python
liste_de_listes = [[1, 2], ["Germaine", "Gertrude"]]
```

# Connaître la taille d'une liste

Avec `len()` - encore une fonction native

```python
>>> liste_vide = []
>>> len(liste_vide)
0
>>> trois_entiers = [1, 2, 3]
>>> len(trois_entiers)
3
```

# Concaténation de listes

Avec `+`

```python
>>> prénoms = ["Alice", "Bob"]
>>> prénoms += ["Charlie", "Eve"]
>>> prénoms
['Alice', 'Bob', "Charlie", 'Eve']
```

\vfill

On ne peut concaténer des listes que avec d'autres listes:

```python
>>> scores = [1, 2, 3]
>>> scores += 4  # TypeError
>>> scores += [4]  # OK
```

# Test d'appartenance

Avec `in`:

```python
>>> prénoms = ["Alice", "Bob"]
>>> "Alice" in prénoms
True
```

\vfill

```python
>>> prénoms = ["Alice", "Bob"]
>>> "Charlie" in prénoms
False
```

# Itérer sur les élements d'une liste

Avec `for ... in`

```python
prénoms = ["Alice", "Bob", "Charlie"]
for prénom in prénoms:
	# La variable 'prénom" est assignée à chaque
	# élément de la liste
    print("Bonjour", prénom)

Bonjour Alice
Bonjour Bob
Bonjour Charlie
```

# Indéxer une liste

* Avec `[]` et un entier

* Les index valides vont de 0 à `n-1` où `n` est la
taille de la liste.

```python
>>> fruits = ["pomme", "orange", "poire"]
>>> fruits[0]
"pomme"
>>> fruits[1]
"orange"
>>> list[2]
"poire"
>>> fruits[3] # IndexError
```

# Modifier une liste

Encore une assignation:

```python
>>> fruits = ["pomme", "orange", "poire"]
>>> fruits[0] = "abricot"
>>> fruits
["abricot", "orange", "poire"]
```

# Les strings sont aussi des listes (presque) - 1

On peut itérer sur les caractères d'une string:

```python
for c in "vache":
	print(c)
v
a
c
h
e
```

# Les strings sont aussi des listes (presque) - 2

On peut tester si un caractère est présent:

```python
>>> "e" in "vache"
True
>>> "x" in "vache"
False
```

# Les strings sont aussi des listes (presque) - 3

Mais on neut peut pas modifier une string

```python
>>> prénom = "Charlotte"
>>> prénom[0]
"C"
>>> prénom[3]
"r"
>>> prénom[0] = "X" # TypeError
```

#

\huge \center Atelier

# Jeu du pendu

Squellete:

```python
def choisir_mot_au_hasard():
	....


def main():
	mot = choisir_mot_au_hasard()
	...


main()
```
