% Programmation avec Python (chapitre 3)
% Dimitri Merejkowsky


\center \huge None

# Jouons avec les dictionnaires

```python
>>> scores = { "Anne": 42, "Bernard": 5 }
>>> scores["Anne"]
42
>>> scores.get("Anne")
42

>>> scores["Sophie"]
KeyError
>>> scores.get("Sophie")
<rien>
```

Que se passe-t-il?

# Exprimer l'absence

En réalité, `get()` retourne None quand la clé n'est pas présente

\vfill

```python
>>> a = 42
>>> a
42
>>> b = None
>>> b
<rien>
```


# None est ambigu

None est `falsy`, tout comme 0, False et les listes vides:

```python
element = dictionnaire.get(clé)
if not element:
    ...
```

Mais ici, comment faire la différence entre:

* la clé existe et vaut None
* la clé existe et est falsy
* la clé n'existe pas ?

# Solution 1: tester l'appartenance

Avec `in`:

```python
if clé in dictionnaire:
    # La clé existe, pas d'erreur
    valeur = dictionnaire[clé]
```

# Solution 2: tester None

Avec `is`:

```python
>>> scores = { "Anne": 42, "Bernard": 5 }
>>> score1 = scores.get("Anne")
>>> score1 is None
False
>>> score2 = scores.get("Sophie")
>>> score2 is None
True
```


# Retourner None

`None` est aussi la valeur par défaut lorsqu'il n'y a pas de `return`
dans le corps de la fonction:

```python
>>> def ne_retourne_rien(a, b):
>>>     c = a + b

>>> résultat = ne_retourne_rien(3, 2)
>>> résultat is None
True
```

# Retourner None (2)

On dit aussi que la fonction est une *procédure*.

On a déjà écrit des procédures: dans `pendu.py`, `display_hint()` et `main()`
ne retournaient rien.

# Retourner None au autre chose

```python
def trouve_dans_liste1(liste, element):
    if element in list:
        return liste.index(element)


def trouve_dans_liste2(liste, element):
    if element in list:
        return liste.index(element)
    else:
        return None
```

\vfill

Les deux fonctions font la même chose : `trouve_dans_liste2` est simplement plus *explicite.*

# Types optionnels

```python
def trouve_dans_liste(liste, element):
    if element in list:
        return liste.index(element)
    else:
        return None
```
On dit aussi que le type de retour de  `trouve_dans_liste` est *optionnel*.

#

\centering \huge Retour sur les listes

# Méthodes

```python
fruits = ["pomme", "banane"]
fruits.append("orange")
```

Quand on écrit `fruits.append("orange")`, on peut voir `append()`
comme une "fonction" qui prendrait `fruits` en argument implicite
(avant le `.`), et `orange` en argument explicite.

On appelle ce genre de fonction une **méthode**.

# clear()

Pour vider une liste:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.clear()
>>> fruits
[]
```

Notez que la méthode `clear()` ne renvoie rien!
La liste est modifiée *sur place*.


# extend()

Pour concaténer des listes:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.extend(["orange", "abricot"])
>>> fruits
['pomme', 'banane', 'orange', 'abricot']
```
\vfill

Peut aussi s'écrire `+=`

```python
>>> nombres = [1, 2]
>>> nombres += [3, 4]
>>> nombres
[1, 2, 3, 4]
```


# pop()

On a vu la méthode `pop()` pour les dictionnaires, mais elle existe
aussi pour les listes:

\vfill

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.pop()  # Retourne l'élément
'pomme'
>>> fruits  # Et modifie la liste
["banane"]
```

# pop() sur liste vide

```python
>>> liste_vide = list()
>>> liste_vide.pop()
IndexError
```


# index()

Pour récupérer la position d'un élément:

```python
>>> fruits = ["pomme", "banane"]
>>> fruits.index("banane")
>>> 1
>>> fruits.index("citron")
>> ValueError
```

# count()

Pour compter le nombre d'occurrences d'un élément

```python
>>> fruits = ["pomme", "banane", "pomme", "poire"]
>>> fruits.count("pomme")
2
>>> fruits.count("poire")
1
>>> fruits.count("citron")
0
```


# Indexer des listes

Rappel:

```python
>>> lettres = ["a", "b", "c", "d", "e"]
>>> lettres[0]  # ça commence à zéro
"a"
>>> lettres[4]
"e"
```

Mais on peut aussi compter à l'envers:

```python
>>> lettres[-1]
"e"
>>> lettres[-2]
"d"
```

# Trancher des listes

Ou "faire des slices", ou "slicer".

```python
>>> lettres = ["a", "b", "c", "d", "e"]
>>> lettres[1:3]  # début (inclus), fin (non-inclus)
['b', 'c']
>>> lettres[:3] # début implicite
['a', 'b', 'c']
>>> lettres[3:] # fin implicite
['d', 'e']
>>> lettres[1:-2]  # fin négative
['b', 'c']
```


#

\centering \huge Retour sur les strings

# Rappel

On a vu que les strings étaient "presque" des liste de caractères.

Par exemple, on peut itérer sur les lettres d'un mot avec: `for lettre
in mot`.

# index() et count() marchent aussi

```python
>>> message = "Bonjour, monde !"
>>> message.index("B")
0
>>> message.count("o")
3
```

# Trancher des chaînes de caractères

On peu aussi slicer des strings:

\vfill

```python
>>> message = "Bonjour, monde !"
>>> message[1:4]
'onj'
>>> message[:7]
'Bonjour'
>>> message[9:-2]
'monde'
```

# Les strings sont immuables

Mais on ne **peut pas** modifier une string "sur place".

```python
>>> message = "Bonjour, monde !"
>>> message[-1] = "?"
TypeError
```

```python
>>> message = "Bonjour, monde !"
>>> message.clear()
AttributeError
```

#

\centering \huge La ligne de commande

# Schéma

![programme](img/programme.png)

# Entrée / sortie

3 canaux:

* Une entrée qu'on peut lire (`stdin`)
* Deux sorties:
    * Sortie normale (ou standard) (`stdout`)
    * Sortie d'erreur (`stdout`)


# Accès en Python

* Pour lire stdin: `input()`
* Pour écrire dans stdout: `print()`
* Pour écrire dans stderr: pas de fonction native

# Accès en Python (2)

Rajouter `import sys` en haut du fichier, puis:

* `sys.stdin.read()`
* `sys.stout.write()`
* `sys.stderr.write()`

On peut aussi utiliser:

`print("erreur", file=sys.stderr)`


# Accès depuis l'invite de commande

On dit aussi *shell*, ou *CLI* (pour *command line interface*).

* stdin: Taper quand le shell vous laisse la main, finir par 'entrée'
* stdout et stderr sont affichés en même temps pas défaut

# Rediriger stdout

Linux , macOS, Windows:

```
python3 fichier.py > output.txt
```

stdout sera écrit dans `output.txt`, et seul `stderr` sera visible.


# Code de retour


* 0 quand tout va bien
* un autre entier quand quelque chose va mal

\vfill

> Toutes les familles heureuses se ressemblent, mais chaque famille
> malheureuse l'est à sa façon.
>
>    Tolstoï

# Code de retour

Les valeurs d'erreur possibles sont en général présentes
dans la documentation.

Note: **ne pas retourner 0** en cas d'erreur, même minime, et même si
un message a été affiché.

C'est important pour pourvoir composer plusieurs programmes (on y
reviendra).


# Afficher le code retour depuis le shell

```bash
# Linux, macOS
$ python3 code.py
$ echo $?
0
```

```bash
# Windows
> python3 code.py
> echo %ERRORLEVEL%
0
```

# Gestion du code de retour en Python

Par défaut, le code de retour est 0.

On peut terminer le programme avec `sys.exit()` et un numéro:

```python
import sys

def fait_quelque_chose():
     if erreur:
         sys.exit(1)
```

Note: dans un vrai programme, veillez à construire et afficher un
message utile!

# Gestion du code de retour en Python (2)

`sys.exit(0)` pour terminer immédiatement et sans erreur.

```python
import sys

def antivirus():
    problèmes = cherche_problèmes()

    if not problèmes:
        print("Aucun problème trouvé")
        sys.exit(0)

    for problème in problèmes:
        # traite chaque problème un à un
        ...
````

# Gestion du code de retour en Python - un raccourci

On peut passer le message d'erreur directement à `sys.exit()` avec
une string au lieu d'un numéro:

```python
if erreur:
    sys.exit("Une erreur est survenue")

```

# Les arguments d'un programme

Pour lancer un programme, on tape son nom, suivi de mots séparés pas
des espaces.

En Python, ça donne

```
python3 fichier.py arg1 arg2
```

# Accès aux arguments en Python

* `import sys`
* `sys.argv`

`sys.argv` est une liste, et son premier argument est
*toujours* le nom du fichier exécuté.

# Exemple

```python
# Dans foo.py
import sys
print("Fichier source:", sys.argv[0])
print("Reste des arguments:", sys.argv[1:])
```

\vfill

```
$ python3 foo.py un deux
Fichier source: foo.py
Reste des arguments: ['un', 'deux']
```

#

\center \huge Cas pratique

# Squelette

Décodeur de noms d'aéroports

* Lire un fichier avec les codes et les noms associés
* En faire un dictionnaire
* Utiliser le premier argument comme nom de code
* Afficher le nom complet de l'aéeroport, ou une
  erreur s'il est inconnu.

# Différentes approches

* Bottom-up (approche *ascendante*)
* Top-Bottom (approche *descendante*)

# Approches bottom-up

Utilisé pour le pendu:

* construire des blocs élémentaires (les petites fonctions `has_won`,
  `display_hint`, etc...)
* les assembler pour faire un tout plus "haut niveau" (le corps de la
  fonction `main()`

# Approche top-down

Essayons de partir du plus "haut niveau" et de "descendre" vers les
blocs élémentaires

# Code

```python
def main():
    dico = fabrique_dico()
    code = lire_code()
    nom = trouve_code(code, dico)
    if nom:
        print(nom)
    else:
        affiche_erreur(code)

main()
```

On a fait comme si le code dont on avait besoin était déjà écrit :)

# lire_code()

```python
import sys

def lire_code():
    if len(sys.argv) < 2:
        print(
            "Pas assez d'arguments",
            file=sys.stderr
        )
        sys.exit(1)
    argument = sys.argv[1]
    # On accepte `cdg` ou `CDG`.
    code = argument.upper()
    return code
```


# fabrique_dico()

Le fichier `airports.txt` ressemble à ça:

```
CDG Paris-Charles de Gaulle
ORY Paris-Orly
NCE Nice-Côte d'Azur
...
```

Téléchargez-le ici:

\url{https://raw.githubusercontent.com/E2L/cours-python/master/sources/airports.txt}

Clique droit / Enregistrer sous / airports.txt

# fabrique_dico() - 2

```python
def fabrique_dico():
    dico = dict()
    fichier = open("airports.txt", "r")
    contenu = fichier.read()
    fichier.close()

    lignes = contenu.splitlines()
    for ligne in lignes:
        code = ligne[0:3]
        nom = ligne[4:]
        dico[code] = nom
    return dico
```

# trouve_code()

```python
def trouve_code(code, dico):
    if code in dico:
        return dico[code]
```

\vfill

Notez le `return None` implicite!


# affiche_erreur()

```python
def affiche_erreur(code):
    print(
        "Code:", code,
        "non trouvé",
        file=sys.stderr
    )
    sys.exit(2)
```

Notes:

* on affiche le code qu'on a pas trouvé (c'est utile de l'avoir dans
  le message)
* valeur d'erreur différente du cas où il n'y avait pas assez
  d'arguments

# Rappel du `main()`


```
def main():
    dico = fabrique_dico()
    code = lire_code()
    nom = trouve_code(code, dico)
    if nom:
        print(nom)
    else:
        affiche_erreur(code)

main()
```

#

\centering \huge Démo


# Place au débat

Quelle approche avez-vous préférée entre bottom-up et top-down?

Pourquoi?
