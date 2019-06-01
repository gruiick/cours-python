% Programmation avec Python (chapitre 13)
% Dimitri Merejkowsky

#

\center \huge Rappels

# Virtualenvs

* Création:

```
$ python3 -m venv /path/to/foo
```

* Utilisation:

```
$ /path/to/foo/bin/pip install requests
# ou
$ source /path/to/foo/bin/activate
(foo) $ pip install requests
```


# Tests

```python
# foo.py
def add_3(x):
	return x + 3

# test_foo.py
import foo

def test_add_3():
	result = foo.add_3(2)
	assert result == 5
```

# pytest

```
$ pytest test_foo.py
============== test session starts =================
test_foo.py .                                 [100%]
=========== 1 passed in 0.01 seconds ===============
```

# TDD

* Une discipline
* 4 règles
* Un cycle


# Règles


* Règle 1 : Il est interdit d'écrire du code de production, *sauf* si c'est pour faire passer un test qui
  a échoué.
* Règle 2 : Il est interdit d'écrire plus de code que celui qui est nécessaire pour provoquer une erreur
  dans les tests (n'importe quelle erreur)
* Règle 3 : Il est interdit d'écrire plus de code que celui qui est nécessaire pour faire passer
  un test qui a échoué
* Règle 4 : Une fois que tous les tests passent, il est interdit de modifier le code sans s'arrêter
  pour considérer la possibilité d'un refactoring.

# Cycle


* RED: on écrit un test qui échoue
* GREEN: on fait passer le test
* REFACTOR: on refactor le code de production et le code de test

#

\center \huge Générateurs

\vfill

\normalsize Ces objects qui sont "presque" des listes ...

# Retour sur les boucles

Itération sur une liste
```python
for i in [1, 2, 3]:
    print(i)
```

Clés d'un dictionnaire
```python
for key in {"a": 1, "b": 2, "c": 3}.keys():
	print(key)
```

Valeurs d'un dictionnaire
```python
for value in {"a": 1, "b": 2, "c": 3}.values():
	print(key)
```

# Pas des listes

```python
>>> my_dict = {"a": 1, "b": 2, "c": 3}
>>> my_dict.keys()
dict_keys(['a', 'b', 'c'])
>>> my_dict.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
```

# Vues

En fait, `.keys()`, `.values()`, `.items()` renvoient des *vues*.

Elles changent quand le dictionnaire changent, mais on ne peut pas
s'en servir pour changer la taille du dictionnaire.

```python
>>> my_dict = {"a": 1, "b": 2, "c": 3}
>>> for k in my_dict.keys():
>>> 	if k == "a":
>>> 		del my_dict[k]
RuntimeError: dictionary changed size during iteration
```

# Vues (2)

Si vraiment vous en avez besoin, vous pouver les convertir en liste
avec `list()`.

```python
>>> my_dict = {"a": 1, "b": 2, "c": 3}
>>> for k in list(my_dict.keys()):
>>> 	if k == "a":
>>> 		del my_dict[k]
>>> my_dict
{"b": 2, "c": 3}
```

# Listes par compréhension

```python
# 1
sequence = ["a", "b", "c"]
new_sequence = []
for element in sequence:
	  new_sequence.append(element.upper())


# 2
sequence = ["a", "b", "c"]
new_sequence = [element.upper() for element in sequence]
```

# Listes par compréhension (2)

On peut transformer la séquence originale:

```python
>>> sequence = [element.upper() for element in sequence]
>>> sequence
["A", "B", "C"]
```

\vfill

On peut changer le type:

```python
>>> as_strings = ["1", "2", "3"]
>>> numbers = [int(x) for x in as_strings]
>>> numbers
[1, 2, 3]
```

# Filtrer une liste

```python
>>> numbers = [1, 2, 3, 4]
>>> odds = [x for x in numbers if x % 2 == 1]
>>> odds
[1, 3]
```

\vfill

```python
>>> numbers = [1, 2, 3, 4]
>>> odds_squared = [x*x for x in numbers if x % 2 == 1]
>>> odds_squared
[1, 9]
```

# Dictionnaires et ensembles par compréhension

Même principe:

```python
>>> scores = [("bob", 2), ("alice", 3)]
>>> my_dict = {t[0]:t[1] for t in scores}
>>> my_dict
{"bob": 2, "alice": 3}
```

\vfill

```python
>>> numbers = [-1, 2, -3, 3]
>>> numbers = {abs(x) for x in numbers}
>>> numbers
{1, 2, 3}
```

# Avantage des compréhensions

* Code plus succint
* Code plus rapide :)
* Code "idiomatique"

# Apparté: Python est gourmand

Python évalue d'habitude de manière "gourmande":

```python
def foo():
	..


def bar():
	...


x = foo(bar(y))
```

On calcule d'abord `y`, puis `bar(y)` puis `foo(bar(y))`


# Générateurs

Concept: fournir les valeurs une par une, à la demande.

Le code *à l'intérieur* des compréhensions est un générateur.

On peut le voir si on utilise des parenthèses:

```python
>>> generator =  (x for x in range(0, 3))
>>> generator
<generator object <genexpr> at 0x7f654c272138>
>>> list(generator)
[1, 2, 3]
```

Les générateurs sont "feignants": ils ne calculent leur valeurs que quand
c'est demandé

# Les générateurs s'épuisent

```python
>>> generator =  (x for x in range(0, 3))
>>> list(generator)
[1, 2, 3]
>>> list(generator)
[]
```

# next()

On peut aussi appeler `next()` sur un générateur, au lieu de `for ... in`

```python
>>> generator =  (x for x in range(0, 2))
>>> next(generator)
0
>>> next(generator)
1
>>> next(generator)
StopIteration
```




# Fabriquer un générateur à l'aide d'une classe

Avec une méthode `__next__()`

```python
class Squares:
	def __init__(self):
		self.value = 0

	def __next__(self):
		self.value += 1
		return self.value ** 2
```

```python
>>> squares = Squares()
>>> next(squares)
1
>>> next(squares)
4
>>> next(squares)
9
```


# Les générateurs ne sont pas des itérateurs

```python
>>> [x for x in s if x < 10]
TypeError: 'Squares' object is not iterable
```

Pour faire `for in`, il faut un itérateur, en plus d'un générateur


# Fabriquer un itérateur à l'aide d'une classe

Avec `__iter__` *et* `__next__`:

```python
class SquaresLessThan:
	def __init__(self, stop_value):
		self.value = 0
		self.stop_value = stop_value

	def __iter__(self):
		return self

	def __next__(self):
		self.value += 1
		res = self.value ** 2
		if res > self.stop_value:
			raise StopIteration()
		return res
```



# Fabriquer un itérateur à l'aide d'une classe

```python
>>> squares = SquaresLessThan(100)
>>> [x for x in squares]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

On retrouve les propriétés des expressions génératrices:
```python
>>> squares = SquaresLessThan(100)
>>> squares[2]
TypeError: 'SquaresLessThan' object is not subscriptable
>>> squares = SquaresLessThan(100)
>>> list(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> list(squares)
[]
```

# yield

On peut aussi faire des générateurs avec `yield`
pour mettre le générateur "en pause", et `return` pour
terminer:


```python
def squares(max_value):
    x = 1
    res = 1
    while res <= max_value:
        yield res
        x += 1
        res = x * x
    return

>>> s = squares(100)
>>> [x for x in s]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

# Combiner avec une classe génératrices

```python
class Squares:
    def __init__(self):
        self.value = 0

    def __next__(self):
        self.value += 1
        return self.value ** 2

def squares_less_than(max_value):
    squares = Squares()
    while True:
        x = next(squares)
        if x > max_value:
                return
        yield x
```

# yield from

On peut aussi chaîner les fonctions génératrices

```python
def integers(max_value):
	x = 0
	while x < max_value:
		yield x
		x += 1
	return


def zero_to_five():
	yield from integers(5)


>>> s = zero_to_five()
>>> [x for x in s]
[0, 1, 2, 3, 4]
```

#

\center \huge Atelier

# Listons des fichiers
