\center \huge Lire et écrire des fichiers

# Rappel: lire

```python
file = open("toto.txt", "r")   # 'r' comme 'read'
contenu = file.read()
file.close()
```

Note: le fichier `toto.txt` doit exister!

# Écrire

On peut écrire tout le contenu d'un coup:

```python
contenu = "du texte à sauvegarder"
file = open("article.txt", "w") # 'w' comme 'write'
file.write(contenu)
file.close()
```


* Le fichier `article.txt` sera écrasé s'il existe déjà.
* N'oubliez surtout pas d'appeler `close()`

# Que faire en cas d'erreur ?

```python
file = open("article.txt", "w") # 'w' comme 'write'
# ... beacoup de code ici
# ... < une erreur
file.close()
```

S'il y a une erreur entre `open()` et `close()`, le fichier ne sera pas fermé!


# Le mot-clé with

```python
with open("toto.txt", "w") as file:
    file.write("du texte")
```

Quand on sort du bloc `with` on a la garantie que `file.close()` sera appelé,
*même* si on sort du bloc à cause d'une erreur.

# Convention

Il n'y a maintenant plus aucune raison d'appeler `.close()` "à la main",
donc ne le faites pas ...

# Lire et écrire des lignes

Très courant:

```python
with open("toto.txt", "r") as file:
    lignes = file.readlines()

# faire quelque chose avec la liste de lignes

with open("toto.txt", "w") as file:
    file.writelines(lignes)
```

Pensez à fermer le premier fichier avant d'ouvrir le second.
(ça marche même s'ils ont le même nom)
