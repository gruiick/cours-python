+++
title = "None"
weight = 1
+++

# None

## Définition

`None` est une "valeur magique" natif en Python. Il est toujours présent, et il est unique.

Un peu comme `True` et `False` qui sont deux valeurs qui servent à représenter tous les booléens.

## Représenter l'absence

L'interpréteur intéractif n'affiche rien quand la valeur est None

```python
>>> a = 42
>>> a
42
>>> b = None
>>> b
```

## Retourner None

En réalité, *toutes* les fonctions pythons retournent *quelque chose*, même quand
elle ne contiennent pas le mot-clé `return`.

```python
def ne_renvoie_rien():
    print("je ne fais qu'afficher quelque chose")
```

```python
>>> resultat = ne_renvoie_rien()
"je ne fais qu'afficher quelque chose"
>>> resultat
```

## Opérations avec None

La plupart des fonctions que nous avons vues échouent si on leur passe None
en argument:

```python
>>> len(None)
TypeError: object of type 'NoneType' has no len()
>>> None < 3
TypeError: '<' not supported between instances of
  'NoneType' and 'int'
>>> int(None)
TypeError: int() argument must be a string,
  a bytes-like object or a number,
  not 'NoneType'
>>> str(None)
'None'
```

## Example d'utilisation:

```python
def trouve_dans_liste(valeur, liste):
    for element in liste:
        if element == valeur:
            return element
    return None
```

```python
>>> trouve_dans_liste(2, [1, 2, 3])
2
>>> trouve_dans_liste(False, [True, False])
False
>>> trouve_dans_liste(1, [3, 4])
```


```python
def trouve_dans_liste(liste, valeur):
    for element in liste:
        if element == valeur:
            return element
```

None est Falsy, et on peut vérifier si une variable vaut None avec `is None`

```python
# hypothèse: `ma_valeur` n'est pas None
mon_element = trouve_dans_liste(ma_valeur, ma_liste)
if mon_element is None:
    print("élément absent de la liste")
if not mon_element:
    # Peut-être que l'élément n'était pas dans la liste,
    # ou peut-être y était-il, mais avec une valeur falsy
    ...
```
