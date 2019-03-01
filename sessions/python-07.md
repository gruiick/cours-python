% Programmation avec Python (chapitre 7)
% Dimitri Merejkowsky

#

\center \huge Un nouveau mot-clé

# Les mots-clés

Des mots qui ne peut être utilisé pour des noms de variales.

On a déjà vu: `def`, `class`, `import`, etc ...

# Assertions

* Arrêter immédiatement le programme avec un message
* Ressemble à `sys.exit()`
* Mais usage un peu différent

# Les assertions sont là pour les dévelopeurs

* Le message n'aura en général *aucun* sens si c'est un simple utilisateur
  qui le lit.
* Il indique en général un problème *interne*, dans le code lui-même,
  par opposition aux erreurs *externes*
Mais on en reparlera :)

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

#

\center \huge Compléments sur les classes

# Attributs d'instances

En vrai les attributs qu'on a vu maintenant sont des
attributs d'instance. Ils sont liés à l'instance courante.

Mais on dit souvent "attribut" tout court.

Il existe un autre type d'attribut.

# Attributs de classe

Dans le bloc de la classe, mais à l'extérieur des
blocs de méthodes:

```python
class Car:
    total_number_of_cars = 0

    def __init__(self, color="black"):
    	# attribut d'instance: avec self
    	self.color = color
    	# attribut de classe: avec le nom de la classe
    	Car.total_number_of_cars += 1
```

# Attributs de classe - 2

Les attributs de classe sont partagés entre toutes
les instances:

```python
>>> ford = Car()
>>> ferrari = Car(color="red")
>>> Car.total_number_of_cars
2
```

# Méthodes de classes

De même, techniquement les méthodes qu'on a vu sont des méthodes
d'instance, et il existe des méthodes de classe


# Méthodes de classes


Avec un joli `@classmethod` au-dessus

```python
class Car:
    total_number_of_cars = 0


    @classmethod
    def print_number_of_cars(cls):
    	print(cls.total_number_of_cars, "have been made")


   def print_color(self):
       print("This car is", self.color)
```

Notez le `cls`

# Méthodes de classes

Pour appeler:

```python
>>> ferrari = Car(color="red")
>>> ford = Car()
>>> Car.print_number_of_cars()
2 cars have been made
```

# On retrouve le même mécanisme

* ce qu'on écrit

```
car.print_color()
```

\vfill

* ce qui est appelé:

```
# self = car
def print_color(self):
      print(self.color)

```

# On retrouve le même mécanisme


* ce qu'on écrit

```
Car.print_number_of_cars()
```

\vfill

* ce qui est appelé:

```
# cls = Car
@classmethod
def print_number_of_cars(cls):
     print(cls.total_number_of_cars)
```

#

\center \huge Les API Web


# Concepts

# HTTP

Une façon pour des machines différentes de parler entre elles.

On fait toujours un aller-retour du *client* vers le *serveur*.

![](img/client-serveur.png)

# Requêtes

Une requête part du client vers le serveur et consite en:

* Une URL
* Un verbe (souvent GET)
* Des paramètres
* Et d'autres trucs

# Réponses

Une réponse revient du serveur vers le client et contient

* Un code de retour
* Du contenu (très souvent, du texte)
* Et d'autres trucs

# API Web et navigateurs

Quand vous tapez une url dans votre navigateur ou que vous suivez
un lien, c'est votre navigateur qui fait la requête.

Le serveur lui renvoie un contenu particulier (du HTML)
C'est ce que vous voyez quand vous faites "show source"

Vous voyez parfois le code de retour (le plus connu étant 404)

# API Web et navigateurs

Grosso modo, quand vous visitez une page, vous faites un GET,
et quand vous remplissez un formulaire, vous faites un POST

*C'est très simplifié*

# Utiliser une API Web

Grosso modo:

* Lire les conditions d'utilisation (important!)
* Regarder les URLs possibles et les paramètres attendus
* Faire quelque chose avec la réponse

Notez qu'on a *absolument* aucune connaissance du code qui tourne sur le serveur!


# JSON

* Un format *texte*.
*  *Très* utilisé justement pour échanger des données entre des machines différentes.
* Implémenté dans plein de langages.



# JSON

Examples:

* Une liste:

```json
["one", "two"]
```

* Un "objet":
```json
{
   "color": "blue",
   "size": 3
}
```

# JSON

On peut imbriquer les objets les uns dans les autres:

```json
{
   "a": 42,
   "b": true,
   "c": ["one", "two"],
}
```

On dit que JSON est un format *texte* par ce qu'on peut le mettre dans une string.


# JSON / Python

Python | JSON
-------|-----
dictionnary | object
True        | true
False       | false
None        | null


# Parser du JSON en Python


```python
>>> import json
>>> data = json.loads("...")
>>> data["a"]
42
```

# Émettre du JSON à partir d'un objet Python

```python
>>> import json
>>> my_object = { "key1" : ["one", "two"] }
>>> json.dumps(my_object, indent=2)
"""
{
  "key1": ["one", "two"]
}
"""
```


#

\center \huge Atelier


# Objectif

* Partir d'un bout de code (moche) qui utilise l'API marvel
* Le nettoyer en introduisant des classes
* Le rendre plus flexible
* Etc ...
