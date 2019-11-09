% Les modules en Python - Partie 1
% Dimitri Merejkowsky

# Un fichier = un module

Et oui, vous faites des modules sans le savoir depuis le début :)

Un fichier `foo.py` correspond *toujours* module `foo`

**Attention: Ce n'est pas tout à fait réciproque. Le module `foo` peut venir d'autre chose
qu'un fichier foo.py.**

# Importer un module

Ou: accéder à du code provenant d'un *autre* fichier source.

Imaginons un fichier `bonjour.py` contenant seulement une assignation
d'une variable `a` à l'entier 42 :

```python
# Dans bonjour.py
a = 42
```

On peut accéder à cette variable en important le module, par
exemple depuis l'interpréteur, en utilisant le mot-clé `import`
suivi du nom du module:

```python
$ python
>>> import bonjour
>>> bonjour.a
42
```

Notez que pour que cela fonctionne:

* Le nom du module est écrit directement, ce n'est *pas* une
  chaîne de caractères.
* Il faut lancer la commande `python` sans argument
* Il faut la lancer depuis le répertoire qui contient `bonjour.py`.

On voit que l'assignation de la variable `a` dans `bonjour.py` est devenue
un *attribut* du module `bonjour` lorsque `bonjour` a été importé

\newpage

Si maintenant on rajoute une fonction `dire_bonjour` dans `bonjour.py`:

```python
# toujours dans bonjour.py
a = 42
def dire_bonjour():
    print("Bonjour!")
```

On peut appeler la fonction `dire_bonjour` depuis l'interpréteur en accédant
à l'attribut `dire_bonjour` du module `bonjour`:

```python
>>> import bonjour
>>> bonjour.dire_bonjour()
Bonjour!
```

# Différence avec la commande python

Notez bien que lancer l'interpréteur et taper `import bonjour` dedans n'est pas
la même chose que lancer `python bonjour.py`.

Dans le deuxième cas, tout le code dans `bonjour.py` est exécuté, puis la commande python
se termine.

Dans le cas de l'interpréteur, on peut utiliser tous les attributs du module et appeler
les fonctions autant de fois qu'on veut:

```python
>>> import bonjour
>>> bonjour.dire_bonjour()
Bonjour!
>>> bonjour.dire_bonjour()
Bonjour!
```

On peut aussi modifier les valeurs des attributs:

```python
>>> import bonjour
>>> bonjour.a
42
>>> bonjour.a = 36
>>> bonjour.a
36
```



# Les imports ne sont faits qu'une seule fois

Il est important de noter que le code à l'intérieur d'un
module n'est *pas* ré-éxécuté si le module a déjà été
importé auparavant.

On peut le voir en mettant du code dans `bonjour.py`,
en plus des simples définitions de fonctions et assignations
de variables
```python
# Dans bonjour.py
print("Je suis le module bonjour et tu viens de m’importer")
```

```python
>>> import bonjour
Je suis le module foo et tu viens de m’importer
>>> import bonjour
<rien>
```

Il faudra donc redémarrer l'interpréteur à chaque fois que le code dans `bonjour.py` change.

# La bibliothèque standard

La bibliothèque standard est une collection de modules directement utilisables fournis à l'installation de Python.

Exemple: `sys`, `random`, ...

Toute la bibliothèque standard est documentée - et la traduction en Français est en cours:

https://docs.python.org/fr/3/library/index.html

Mettez ce lien dans vos favoris - il vous sera très utile.

# Quelques exemples de modules de la bibliothèque standard

## Easter eggs

(Ou fonctionnalités cachées)

* `import antigravity`
* `import this`

Je vous laisse découvrir ce que fait le premier. Quant au deuxième, il contient
une liste de préceptes que la plupart des développeurs Python s'efforcent de
respecter. On en reparlera ...
