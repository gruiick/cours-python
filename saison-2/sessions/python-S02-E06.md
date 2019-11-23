% Programmation avec Python (chapitre 6)
% Dimitri Merejkowsky


#

\center \huge Modules

# Un fichier = un module

À un fichier `mon_module.py` correspond _toujours_ un module `mon_module`.
(La réciproque n'est pas vraie)

# Code dans un module

```python
# Dans bonjour.py
a = 42
```

Le module `bonjour` contient contient un *attribut* `a`
dont la valeur est 42.

# Importer un module

Avec le mot-clé `import`, suivi du nom du module,
_sans guillemets_.

```python
$ python
>>> import bonjour
>>> bonjour.a
42
```

# Une fonction dans un module

```python
# toujours dans bonjour.py
a = 42
def dire_bonjour():
    print("Bonjour!")
```

# Appeler une fonction depuis un module

```python
>>> import bonjour
>>> bonjour.dire_bonjour()
Bonjour!
```

**note**: différent de `python3 bonjour.py`.

# Interaction - 1


```python
>>> import bonjour
>>> bonjour.dire_bonjour()
Bonjour!
>>> bonjour.dire_bonjour()
Bonjour!
```

# Interaction - 2

```python
>>> import bonjour
>>> bonjour.a
42
>>> bonjour.a = 36
>>> bonjour.a
36
```

# Les imports ne sont faits qu'une seule fois


```python
# Dans bonjour.py
print("Je suis le module bonjour!")
```

```python
>>> import bonjour
Je suis le module bonjour!
>>> import bonjour
<rien>
```

# La bibliothèque standard

La bibliothèque standard est une collection de modules directement utilisables fournis à l'installation de Python.

Exemple: `sys`, `random`, ...

Toute la bibliothèque standard est documentée - et la traduction en Français est en cours:

https://docs.python.org/fr/3/library/index.html

Mettez ce lien dans vos favoris - il vous sera très utile.


# sys

Contient notamment `sys.argv`, une liste de chaînes de caractères, qui
n'est *jamais vide*.

Dans l'interpréteur intéractif, le premier élément est le
chemin du binaire python:

```bash
$ python3
>>> import sys
>>> sys.argv
["/usr/bin/python3"]
```

# sys.argv avec un fichier

```python
# Dans lancez_moi.py
import sys

def main():
   print(sys.argv)
```

\vfill

Le premier élément est alors le nom du fichier:

```bash
$ python3 lancez_moi.py
["lancez_moi.py"]
```

# sys.argv avec un fichier - 2

Si on rajoute des mots après le nom du fichier, ils apparaissent dans `sys.argv`:

```python
# dans lancez_moi.py
import sys

def main():
   print(sys.argv)
```

\vfill

```bash
$ python3 lancez_moi.py un deux trois
["lancez_moi.py", "un", "deux", "trois"]
```

# Les scripts Python

Pour interagir avec l'utilisateur, on a souvent utilisé `input()`, passer par
`sys.argv` est plus commun.

Exemple:

```bash
$ python3 faire_le_café
$ python3 faire_le_café --sans-sucre
```

#

\center \huge QCM


#

```python
def dire_bonjour():
    return "Bonjour"

x = dire_bonjour()
print(x)
```

1. Erreur
2. Affiche "Bonjour"

\pause

Réponse: 2


#

```python
def dire_bonjour():
    print("Bonjour")

x = dire_bonjour()
print(x)
```

1. Erreur
2. Affiche "Bonjour"
3. Affiche 'None"

\pause

Réponse: 3 - pas de return, la fonction
renvoie None

#

```python
def dire_bonjour():
    return "Bonjour"

dire_bonjour()
```

1. N'affiche rien
2. Affiche "Bonjour"
3. Affiche 'None"


\pause

Réponse 1 - la fonction renvoie une valeur, mais
on n'en fait rien.


#

```python
# Dans mon_module.py
ma_variable = 42
```

```python
>>> import "mon_module"
>>> print(ma_variable)
```

1. Erreur
2. Affiche '42'

\pause

Réponse 1: les noms de modules ne sont pas des strings!

#

```python
# Dans mon_module.py
ma_variable = 42
```

```python
>>> import mon_module
>>> print(ma_variable)
```

1. Erreur
2. Affiche '42'

\pause

Réponse 1: `ma_variable` est un *attribut* de `mon_module`.

#

```python
# Dans mon_module.py
ma_variable = 42
```

```python
>>> import mon_module
>>> mon_module.ma_variable = 43
>>> mon_module.ma_variable
```

1. Erreur
2. Affiche '43'

\pause

Réponse 2: on peut lire et écrire les attributs des modules
importés!

#

```python
# Dans mon_script.py
print(sys.argv[0])
```

```bash
$ python mon_script mon_argument
```

1. Erreur
2. Affiche 'mon_script'

\pause

Réponse 1: il faut donner le vrai nom du fichier!

#

```python
# Dans mon_script.py
print(sys.argv[0])
```

```bash
$ python mon_script.py mon_argument
```

1. Erreur
2. Affiche 'mon_script'

\pause

Réponse 1: il faut importer `sys` avant de pouvoir l'utiliser

#

```python
# Dans mon_script.py
import sys
print(sys.argv[0])
```

```bash
$ python mon_script.py mon_argument
```

1. Erreur
2. Affiche 'mon_argument'

\pause

C'est un piège! `argv[0]` est le chemin du script!

#

```python
# Dans mon_script.py
import sys
print(sys.argv[1])
```

```bash
$ python mon_script.py mon_argument
```

1. Erreur
2. Affiche 'mon_argument'

\pause

Réponse 2 :)

#

```python
# Dans mon_script.py
import sys
print(sys.argv[1])
```

```bash
$ python mon_script.py
```

1. Erreur
2. Affiche 'mon_script.py'

\pause

Réponse 1. `argv` a une taille 1, et on accède à l'index 1.

#

\center \huge Atelier
