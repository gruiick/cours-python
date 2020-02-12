+++
title = "pass"
weight = 2
+++

# pass

En Python, à cause de l'organisation en blocs indentés, on ne
peut pas vraiment avoir de blocs vides. Mais parfois, on
a besoin d'un bloc qui ne fasse rien.

Dans ce cas, on peut utiliser le mot-clé `pass`, par exemple
après un if:

```python
une_condition = False
if une_condition:
    pass
else:
    print("une_condition n'est pas vraie")
```

On peut aussi - et c'est l'usage le plus courant - utiliser `pass` pour
définir une fonction qui ne fait rien:

```python
def ne_fait_rien():
    pass
```

```python
>>> ne_fait_rien()
<rien>
```
