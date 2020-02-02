+++
title = "Arguments par défaut"
weight = 4
+++

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

Appel:
```python
>>> dire_bonjour("Thomas", enthousiaste=True)
Bonjour Thomas!
>>> dire_bonjour("Thomas", enthousiaste=False)
Bonjour Thomas
>>> dire_bonjour("Thomas")
Bonjour Thomas
```

