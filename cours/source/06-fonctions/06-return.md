+++
title = "return"
weight = 6
+++

# Valeur de retour d'une fonction

Définition avec le mot `return`

```python
def additionner(x, y):
	return x + y
```

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

```python
>>> dire_bonjour("Dimitri", première_fois=True)
Bonjour Dimitri
Heureux de faire votre connaissance
>>> dire_bonjour("Dimitri", première_fois=False)
Bonjour Dimitri
```
