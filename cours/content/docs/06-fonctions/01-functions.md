+++
title = "Fonctions"
weight = 1
+++

# Fonctions

## Fonction sans argument

Définition:
```python
def dire_bonjour():
    print("Bonjour")
```

* avec `def`
* avec un `:` à la fin et un _bloc indenté_ (appelé le "corps")

Appel:
```
>>> dire_bonjour()
Bonjour
```

* avec le nom de la fonction et des parenthèses

## Le pouvoir des fonctions

Ici on vient de créer une nouvelle fonctionnalité
à Python. Avant qu'on définisse la fonction
`dire_bonjour()`, il ne savait pas dire bonjour,
il savait uniquement afficher des messages à
l'écran.

On dit qu'on a _créé une abstraction_. Et
c'est une technique extrêmement utile en
programmation.


## Fonction avec un argument

Définition: avec l'argument à l'intérieur des parenthèses

```python
def dire_bonjour(prénom):
	print("Bonjour " + prénom)
```

Appel: en passant une variable ou une valeur dans les parenthèses

```python
>>> dire_bonjour("Germaine")
Bonjour Germaine

>>> prénom_de_charlotte = "Charlotte"
>>> dire_bonjour(prénom_de_charlotte)
Bonjour Charlotte
```

## Exécution d'une fonction

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
