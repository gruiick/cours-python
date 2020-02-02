+++
title = "Flôt de contrôle"
weight = 11
+++

# Flot de contrôle

L'essence de la programmation!


## if

```python
a = 3
b = 4
if a == b:
    print("a et b sont égaux")
print("on continue")
```


Notes:

* deux points à la fin de la ligne
* indentation après les deux points
* si la condition n'est pas vraie, rien ne se passe

Notez qu'on peut mettre uniquement une variable ou une valeur
après le if. Ceci ne fonctionne pas:

```python
if a = 3:
	print("a égale 3")
```

et fait une erreur de syntaxe


## if / else

```python
a = 3
b = 4
if a == b:
    print("a et b sont égaux")
else:
    print("a et b sont différent")
```


## if / elif

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

On peut mettre autont de `elif` qu'on veut!
Le derier `else` s'éxécute en dernier


## while

Répéter tant qu'une condition est vraie

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


## Notre première boucle infinie

```python
while True:
	print("spam!")
```

CTRL-C pour interrompre


## Combiner while et if

On peut "sortir" de la boucle `while` avec `break`


```python
i = 0
while True:
    i = i + 1
    print(i)
    if i > 3:
        break
```

```
1
2
3
4
```
