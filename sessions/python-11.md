% Programmation avec Python (chapitre 11)
% Dimitri Merejkowsky

\center \huge Retour sur les exceptions

# A quoi sert finally?

```python
try:
    file = open("file.txt")
    1 / 0
except ZeroDivisionError:
    print("got you")
finally:
    print("closing")
    file.close()
```

# versus

```python
try:
    file = open("file.txt")
    1 / 0
except ZeroDivisionError:
    print("got you")

file.close()
```

# Réponse:

Que se passe-t-il si l'exception *n'est pas* ZeroDivisionError?

#

\center \huge Utiliser des bibliothèques tierces

# Rappel

```python
import foo

foo.bar()
```

Fonctionne si:

* Il y a un `foo.py` quelque part qui contient une fonction `bar`
* Dans le dossier courant
* Ou dans la bibliothèque standard Python

# Parlons de PATH

* Vous connaissez peut-être la variable d'environement PATH, qui dit
  où sont les exécutables.

```bash
PATH="/bin:/usr/bin:/usr/sbin"
$ ifconfig
# résout sur /usr/sbin/ifconfig
$ ls
# résout sur /bin/ls
```

Résoudre: trouver le premier élément dans la liste.

# sys.path

En Python c'est pareil.

```python
import sys
print(sys.path)
```

# Sur mon Arch

```
* ''   # vide = chemin courant
* /usr/lib/python3.7
* /usr/lib/python3.7/lib-dynload
* /home/dmerej/.local/lib/python3.7/site-packages
* /usr/lib/python3.7/site-packages
```

* Le chemin courant a la priorité sur la bibliothèque standard!

# À noter

Seul deux des composants sont accessibles en *écriture* par
mon utilisateur courant:

* Le chemin courant
* Un chemin dans mon $HOME (`~/.local/lib/python3.7/site-packages/`)

Même principe sur macOS et Windows (presque)

# Bibliothèques tierces

Par example, pour faire des jolis tableaux:

```python
import tabulate

scores = [
  ["John", 345],
  ["Mary-Jane", 2],
  ["Bob", 543],
]
table = tabulate.tabulate(scores)
print(table)
```

```
---------  ---
John       345
Mary-Jane    2
Bob        543
---------  ---
```

# Le problème

On peut trouver le code source de `tabulate` facilement.

Mais comment faire pour le mettre dans `sys.path`?

# Dans la distribution

Si vous êtes sous Linux, peut-être que vous pouvez utiliser votre
gestionnaire de paquets.

Du genre: `sudo apt install python3-tabulate`.

# À la main

On peut récupérer les sources et les installer avec `python3 setup.py install --user`

* Quasiment *tous* les projets python ont un `setup.py` utilisable de cette façon.
* On utilise `--user` pour éviter des problèmes de permissions

* Démo!

# Anatomie du setup.py

Un appel à `setuptools.setup()`. C'est tout

```python
from setuptools import setup

setup(
  name='tabulate',
  version='0.8.1',
  description='Pretty-print tabular data',
  py_modules=["tabulate"],
  scripts=["bin/tabulate"],
  ...
)
```

# À noter

Sur linux, si le paquet contient des *scripts*, ils arriveront dans `~/.local/bin`.

Sous macOS et Windows, ce sera un autre emplacement, mais qui *dépendra de la version de Python*.

Il faudra peut-être changer le PATH sur votre machine si vous voulez lancer les scripts
directement. Ou alors, utilisez `python3 -m` (quand c'est possible).

Example:

```
python3 -m tabulate
```

# Dépendances

Prenons une autre bibliothèque: `cli-ui`.

Elle sert à faire des jolis programmes en couleur:

```python
import cli_ui

cli_ui.info_1("Ceci est une info importante")
cli_ui.info("Ceci est en", cli_ui.bold, "gras")
```

# Dépendances de cli-ui

En fait, `cli-ui` utilise *d'autres* bibliothèques.

Par exemple:

```python
headers=["name", "score"]
data = [
  [(bold, "John"), (green, 10.0)],
  [(bold, "Jane"), (green, 5.0)],
]
cli_ui.info_table(data, headers=headers)
```

Devinez qui s'occupe d'afficher le tableau!

# Déclaration des dépendances

Aussi dans setup.py:

```python
setup(
  name="cli-ui",
  version="0.9.1",
  install_requires=[
     "tabulate",
     ...
  ],
  ...
)
```

# pypi

pypi.org: un site que recense plein de bibliothèques python.

Vive l'open source!

cli-ui et tabulate y sont présents.

# pip

* `pip` vient par défaut avec Python3
* Vous pouvez aussi l'installer avec `get-pip.py` (python3 get-pip.py --user)
* Toujours le lancer avec `python3 -m pip`.

# Intérêt de pip

* Va chercher tout seul sur `pypi`
* Lance `setup.py` tout seul (pour trouver les dépendances, et les installer)

* S'utilise avec `python3 -m pip install --user ...`



# Fonctionnalités en plus

* Peut supprimer quelque chose installé - `python3 -m pip uninstall <>`
* Peut chercher sur `pypi` directement - `python3 -m pip search <>`
* Peut lister ce qui est installé - `python3 -m pip freeze`

# Limitations de pip seul

* Il faut penser à utiliser `--user`
* Si le paquet est déjà installé dans le système (genre `/usr/lib/` sous Linux),
  pip ne saura pas le mettre à jour - il faudra passer par le gestionnaire de paquet de
  la distribution
  


# Versions de dépendances

Parfois, les versions sont incompatibles entre elles!

https://tankerhq.github.io/python-cli-ui/changelog.html#v0-8-0

# Solution

On peut donner des versions dans `setup.py`:

```python
install_requires=[
   "cli-ui < 0.8",
   ...
]
```


# Apparté - pourquoi sudo pip c'est pas une bonne idée

Les fichiers dans `/usr/lib` sont contrôllés par votre gestionnaire de paquet.

Les mainteneurs de votre distribution font en sorte qu'ils marchent bien les uns
avec les autres.

Si vous lancer `sudo pip` vous risquez de casser votre système.

# Plusieurs projets

* Projet A utilise `cli-ui` 0.7
* Projet B utilise `cli-ui` 0.9

Comment faire pour travailler sur les deux projets?

# Environements virtuels

* Un répertoire *isolé* du reste du système.
* Contient un binaire python légèrement différent du binaire ordinaire.
* Se crée avec `python3 -m venv <le chemin>` - sauf sous Debian ;-(

# Avec virtualenv

* Vous pouvez aussi installer `virtualenv` avec pip puis utiliser `virtualenv`

```bash
$ python3 -m pip install virtualenv --user
$ python3 -m virtualenv <le chemin>
```

# L'isolation en pratique

* Plus de chemin dans `~/.local/lib`
* Moins de chemins dans le système
* Les scripts restent dans le virtualenv

# Pip + Virtualenv = <3

Et vous avez aussi un `pip` spécial dans `/le chemin/bin/pip`

* Plus besoin de `--user`
* On peut créér deux virtualenvs différent pour les projets A et B


# Activer un virtualenv

Si taper le chemin du virtualenv vous embête, vous pouves
*l'activer* avec `source <chemin>/bin/activate`

Pour sortir: `deactivate`.

# Les règles

* Un virtualenv par projet et par version de Python
* Toujours utiliser pip depuis un virtualenv

C'est plus long, mais ça vous évitera un tas de problèmes ...

# Pour aller plus loin

* PYTHONPATH
* `requirements.txt`
* `pipenv`
* `poetry`

On y reviendra

#

\center \huge À vous de jouer!

#

Pas d'atelier collectif cette fois. Objectif:

* Créer un virtualenv et installer pygame dedans
* Suivre le tutoriel par vous-même :)

https://nerdparadise.com/programming/pygame

Je suis là si vous avez des questions!
