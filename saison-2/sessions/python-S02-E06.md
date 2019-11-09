% Programmation avec Python (chapitre 6)
% Dimitri Merejkowsky


#

\center \huge Rappels sur les classes

# Classes vides

Définition:
```python
class MonObjet:
    pass
```

Instanciation:
```python
>>> objet_1 = MonObjet()
```

# Attributs

```python
>>> mon_instance = MonObjet()
>>> mon_instance.x = 42
>>> mon_instance.mon_attribut
42
```

# Méthodes

Définition:
```python
class MonObjet:
    def ma_méthode(self):
        return 42
```

Appel:
```python
class MonObjet:
    def ma_méthode(self):
            return 42
>>> ma_méthode()
Erreur
>>> mon_instance = MonObjet()
>>> mon_instance.ma_méthode()
42
```


# self - 1

`self` *prend la valeur de l'instance courante* quand la méthode est appelée.

```python
class MonObjet:
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MonObjet()
>>> mon_instance.x = 42
>>> mon_instance.affiche_attribut_x()
42
```

# self - 2

On peut aussi *créer* des attributs dans une méthode:

```python
class MonObjet:
    def crée_attribut_x(self):
        self.x = 42
    def affiche_attribut_x(self):
        print(self.x)

>>> mon_instance = MonObjet()
>>> mon_instance.affiche_attribut_x()
# Erreur: `mon_instance` n'a pas d'attribut `x`

>>> mon_instance.crée_attribut_x()
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes avec arguments

```python
class MonObjet
    def crée_attribut_x(self, valeur_de_x):
        self.x = valeur_de_x

    def affiche_attribut_x(self);
        print(self.x)

>>> mon_instance = MonObjet()
>>> mon_instance.crée_attribut_x(42)
>>> mon_instance.affiche_attribut_x()
42
```

# Méthodes appelant d'autres méthodes - 1

```python
class MonObjet:
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

# Méthodes appelant d'autres méthodes - 2

```python
>>> mon_instance = MonObjet()
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

# Constructeur sans arguments

```python
class MonObjet:
    def __init__(self):
        self.x = 1
        self.y = 2

>>> mon_instance = MonObjet()
>>> mon_instance.x
1
>>> mon_instance.y
2
```

# Constructeur avec arguments

```python
class MonObjet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```
>>> mon_instance = MonObjet(3, 4)
>>> mon_instance.x
3
>>> mon_instance.y
4
```
