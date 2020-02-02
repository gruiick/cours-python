+++
title = "Rappels"
weight = 1
+++

# Rappels

_Note: ceci est surtout un rappel du chapitre 11. N'hésitez pas à vous y
reporter si les exemples de code ne vous paraissent pas clairs._


## Classes vides

Définition:
```python
class MaClasse:
    pass
```

Instanciation:
```python
>>> instance_1 = MaClasse()
```

## Attributs

Un attribut est une variable _à l'intérieur_ d'autre chose (par exemple une instance de classe).

La syntaxe consiste en l'instance à gauche et l'attribut à droite après un point:

```python
>>> mon_instance = MaClasse()
# création de l'attribut `x` dans mon_instance:
>>> mon_instance.x = 42
# accès à l'attribut `x` dans mon_instance:
>>> mon_instance.x
42
```

## Méthodes

Une méthode est une fonction définie à l'intérieur d'une classe:

Définition:
```python
class MaClasse:
    def ma_méthode(self):
        return 42
```

Les méthodes sont des attributs des instances de classes:

```python
class MaClasse:
    def ma_méthode(self):
            return 42
>>> ma_méthode()
Erreur
>>> mon_instance = MaClasse()
>>> mon_instance.ma_méthode()
42
```


## self

`self` *prend la valeur de l'instance courante* quand la méthode est appelée.

```python
class MaClasse:
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.x = 42
>>> mon_instance.affiche_attribut_x()
42
```

On peut aussi *créer* des attributs dans une méthode:

```python
class MaClasse:
    def crée_attribut_x(self):
        self.x = 42
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.affiche_attribut_x()
# Erreur: `mon_instance` n'a pas d'attribut `x`

>>> mon_instance.crée_attribut_x()
>>> mon_instance.affiche_attribut_x()
42
```

## Méthodes avec arguments

```python
class MaClasse
    def crée_attribut_x(self, valeur_de_x):
        self.x = valeur_de_x

    def affiche_attribut_x(self);
        print(self.x)

>>> mon_instance = MaClasse()
>>> mon_instance.crée_attribut_x(42)
>>> mon_instance.affiche_attribut_x()
42
```

## Méthodes appelant d'autres méthodes

```python
class MaClasse:
    def méthode_1(self):
        print("démarrage de la méthode 1")
        print("la méthode 1 affiche bonjour")
        print("bonjour")
        print("fin de la méthode 1")


    def méthode_2(self):
        print("la méthode 2 appelle la méthode 1")
        self.méthode_1()
        print("fin de la méthode 2")
```


```python
>>> mon_instance = MaClasse()
>>> mon_instance.méthode_2()
```

```text
la méthode 2 appelle la méthode 1
démarrage de la méthode 1
la méthode 1 affiche bonjour
bonjour
fin de la méthode 1
fin de la méthode 2
```

## Constructeur sans arguments

Un constructeur en Python désigne la méthode nomée `__init__`,
quand celle-ci existe.

La méthode `__init__` est appelée automatiquement quand la
classe est instanciée:

```python
class MaClasse:
    def __init__(self):
        self.x = 1
        self.y = 2

>>> mon_instance = MaClasse()
>>> mon_instance.x
1
>>> mon_instance.y
2
```

## Constructeur avec arguments

La méthode `__init__` peut avoir des arguments,
dans ce cas, ceux ci doivent être fournis
lors de l'instanciation:

```python
class MaClasse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```python
>>> mon_instance = MaClasse(3, 4)
>>> mon_instance.x
3
>>> mon_instance.y
4
```
