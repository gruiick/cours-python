% Programmation avec Python (Épisode 6)
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


# Le module sys

Le module `sys` est disponible par défaut, et contient plusieurs variables
utiles.

On va parler ici de l'une d'entre elles: `argv`.

# sys.argv avec un fichier

`sys.argv` est une liste de chaînes de caractères, qui
n'est *jamais vide*, et est utile quand on lance python
avec un fichier source:

```python
# Dans lancez_moi.py
import sys

def main():
   print(sys.argv)

main()
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

main()
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
3. Affiche "Bonjour" puis "None"

\pause

Réponse: 3 - le premier print vient de l'appel de la fonction,
comme la fonction ne renvoie rien (pas de `return`), x vaut
None

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

Réponse 1: `ma_variable` est un *attribut* de `mon_module`, elle n'est
pas disponible en dehors.

#

```python
# Dans mon_module.py
ma_variable = 42
```

```python
import mon_module
mon_module.ma_variable = 43
print(mon_module.ma_variable)
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

# Introduction

Vous allez jouer le rôle successivement d'un espion Bordure, puis d'un
espion Syldave (les noms viennent de l'univers de Tintin), et l'atelier
comporte trois parties.

# Chiffrement v1

Vous devez implémenter le script suivant, nommé `chiffrer.py`.

Il se lance ainsi:

```bash
$ python chiffrer.py n MESSAGE
```

où `n` est en entier entre 0 et 25, et `MESSAGE` une chaîne de caractères
non accentués.

L'algorithme est le suivant:

* Supprimer les espaces et les signes de ponctuation du message
* Remplacer chaque lettre par une majuscule
* Décaler chaque lettre du message en utilisant le pas `n`.

Par exemple, si le message est `BONJOUR` et le pas 2, le message
chiffré devient `DQPLQWT`.

Notez que si on décale la lettre `Y` avec un pas de 3, on doit obtenir
`B` (il faut effectuer une rotation)


# Chiffrement v2

Pour le chiffrement version 2, il faut maintenant utiliser une *clé* `k`
à la place de l'entier `n`.

Le script devient:

```bash
$ python chiffrer2.py k MESSAGE
```

Pour chiffrer le message, on continue à décaler chaque lettre d'un pas,
mais la valeur du pas n'est plus constante. À la place, elle est
donnée par les lettres de la clé.

Par exemple, avec la clé 'ACB', le pas prend les valeurs `0, 2, 1, 0, 2, 1` etc.

En chiffrant `tintin` avec la clé `ACB`, on doit obtenir `TKOTKO`.

# Casser le chiffrement

Maintenant vous jouez le rôle d'un espion Syldave. Voici ce que vous avez
à votre disposition:

* Le script `chiffrer2.py`
* Le message secret suivant: `IHDXUVZKRISCBNJWBXIDUWVVODUBPRFQRIRGBUR`

Vous savez également que:

* La clé utilisée contient 3 lettres
* Le message parle du maréchal Plekszy-Gladz

Vous devez déchiffrer le message, et obtenir la valeur de la clé.

# Indications - 1

Quelques indices:

* La fonction `ord` permet de convertir une lettre en son code ASCII:

  `ord('A') = 65, ord('B') = 66, ... ,ord('Z') = 90`

* La fonction `chr` permet de convertir un entier en lettre:

  `chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'`

# Indications - 2

* L'opérateur `%` permet de s'assurer qu'une valeur est comprise dans un intervalle donné.

`0 % 26 = 0, 1 % 26 = 1, ..., 26 % 26 = 0`

`27 % 26 = 1, 28 % 26 = 2, ...`

* Toutes les chaînes de caractères en Python contiennent les méthodes `is_alpha()` et `upper()`:

`"a".is_alpha() = True, "!".is_alpha() = False`

`"Message Important".upper() = "MESSAGE IMPORTANT"`

# Conseils pour l'implémentation

* Dans `chiffrer.py`, assurez-vous d'avoir une fonction `décale_lettre` prenant une lettre et un pas. Cela facilitera l'implémentation de `chiffrer2.py`.

* Pour la dernière partie:
   * Pour casser le message, vous pouvez partir de `chiffrer2.py`. Il y a très peu de code à changer ...
   * Il y a $26^3$ clés possibles. Un ordinateur n'aura aucun mal à les essayer toutes une par une (ça ne fait "que" 17 000 possibilités environ)
    * Quand vous aurez déchiffré le message, vérifiez que votre clé est correcte, en essayant de le re-chiffrer avec l'algorithme v2 - vous devez retomber sur le message chiffré initial.

