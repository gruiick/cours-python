% Programmation avec Python (chapitre 7)
% Dimitri Merejkowsky


#

\center \huge Rappels sur les classes


# Définition d'une classe

Construire la classe`Counter` avec un attribut `count`:

```python
class Counter:
    def __init__(self):
        self.count = 0
```



# Instantiation

Construire une nouvelle *instance* de `Counter`

```python
>>> counter = Counter()
>>> counter.count
0
```

# Méthode

Ajouter une méthode pour incrémenter le compteur:

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
    	self.count += 1

```

# Apeller une méthode

```python
>>> counter = Counter()
>>> counter.count
0
>>> counter.increment()
>>> counter.count
1
```
