% Programmation avec Python (Épisode 8)
% Dimitri Merejkowsky
% 18 janvier 2020


# Quiz

Les transparents qui suivent contiennent tous du code, suivi d'une liste
numérotée de 1 à 2.

Seule l'une des deux réponse est correcte - à vous de la trouver.

Si vous n'êtes pas sûr, vous pouvez recopier le code dans un fichier
`exemple.py` et lancer `python3 exemple.py` pour faire tourner
le code :)

Vous pouvez aussi lire les chapitres 1 à 13 sur
https://dmerej.info/books/python/

À vous de jouer!

#

```python
print("Bonjour")
```

\vfill

1. Bonjour
2. Au revoir

#


```python
print(1 + 2)
```

\vfill

1. 2
2. 3

#

```python
print(11  / 2)
```

\vfill

1. 5
2. 5.5

#

```python
print(11  // 2)
```

\vfill

1. 5
2. 5.5

#


```python
print(11  % 2)
```

\vfill

1. 0
2. 1


#

```python
print(1 + 2 * 3)
```

\vfill

1. 9
2. 7

#

```python
print((1 + 2) * 3)
```

\vfill

1. 9
2. 7

#

```python
a = 2
print(a)
```

\vfill

1. 2
2. 3

#

```python
a = 2
b = 3
print(a + b)
```

\vfill

1. 5
2. 4

#

```python
message = "Bonjour"
print(message)
```

\vfill

1. Bonjour
2. Au revoir

#

```python
message = "Bonjour"
message = message + " monde"
print(message)
```

\vfill

1. Bonjour
2. Bonjour monde


#

```python
message = "Bonjour"
message += " monde"
print(message)
```

\vfill

1. Bonjour
2. Bonjour monde

#

```python
message = "Bonjour en Anglais se dit 'hello'"
print(message)
```

\vfill

1. Bonjour en Anglais se dit hello
2. Bonjour en Anglais se dit 'hello'

#

```python
message = 'Bonjour en Anglais se dit "hello"'
print(message)
```

\vfill

1. Bonjour en Anglais se dit 'hello'
2. Bonjour en Anglais se dit "hello"

#

```python
réponse = 42
message = "La réponse est: " + str(réponse)
print(message)
```

\vfill

1. La réponse est: 'réponse'
2. La réponse est: 42

#

```python
entrée_utilisateur = "40"
age = int(entrée_utilisateur)
année_de_naissance = 2020 - age
print(année_de_naissance)
```

\vfill

1. 1980
2.   40

#

```python
la_terre_est_plate = False
print(la_terre_est_plate)
```

\vfill

1. True
2. False

#


```python
il_pleut = True
j_ai_mon_parapluie = False
print(il_pleut and j_ai_mon_parapluie)
```

\vfill

1. True
2. False

#

```python
il_pleut = True
j_ai_mon_parapluie = False
je_suis_mouillé = il_pleut and (not j_ai_mon_parapluie)
print(je_suis_mouillé)
```

\vfill

1. True
2. False

#

```python
a = 2
b = 3
print(a == b)
```

\vfill

1. True
2. False


#

```python
a = 2
b = 3
print(a != b)
```

\vfill

1. True
2. False

#

```python
a = 2
b = 3
print(a < b)
```

\vfill

1. True
2. False

#

```python
a = 2
b = 2
print(a <= b)
```

\vfill

1. True
2. False

#

```python
min = 2
x  = 3
max = 5
print(min < x < max)
```

\vfill

1. True
2. False

#

```python
a = 3
b = 4
if a == b:
    print("a et b sont égaux")
else:
    print("a et b sont différents")
```

\vfill

1. a et b sont égaux
2. a et b sont différents

#

```python
age = 18
if age < 10:
	print("inférieur à dix")
elif 10 <= age < 20:
	print("âge entre 10 et 20")
elif 20 <= age < 40:
	print("âge entre 20 et 40")
else:
	print("âge supérieur à 40")
```

\vfill

1. âge entre 10 et 20
2. âge supérieur à 40

#

```python
i = 0
while i < 3:
    i = i + 1
print(i)
```

\vfill

1. 2
2. 3

#

```python
i = 0
while True:
    i = i + 1
    if i >= 3:
        break
print(i)
```

\vfill

1. 1
2. 3

#

```python
def dire_bonjour():
    print("Bonjour")

def dire_au_revoir():
    print("Au revoir")

dire_bonjour()
```

\vfill

1. Bonjour
2. Au revoir

#

```python
def dire_bonjour(prénom):
    print("Bonjour " + prénom )

dire_bonjour("Alice")
```

\vfill

1. Bonjour Alice
2. Au revoir Alice

#

```python
def ma_fonction(x, y):
    return x -y

résultat = ma_fonction(2, 5)
print(résultat)
```

\vfill

1. 3
2. -3

#

```python
def ma_fonction(x, y):
    return x -y

résultat = ma_fonction(y=2, x=5)
print(résultat)
```

\vfill

1. 3
2. -3

#


```python
def dire_bonjour(prénom, enthousiaste=False):
	message = "Bonjour " + prénom
	if enthousiaste:
		message += "!"
	print(message)

dire_bonjour("Thomas", enthousiaste=True)
```

\vfill

1. Bonjour Thomas
2. Bonjour Thomas!

#


```python
def dire_bonjour(prénom, enthousiaste=False):
	message = "Bonjour " + prénom
	if enthousiaste:
		message += "!"
	print(message)

dire_bonjour("Thomas")
```

\vfill

1. Bonjour Thomas
2. Bonjour Thomas!

#

```python
a = "un"
b = "deux"
c = "trois"
print(a, b, c)
```

\vfill

1. undeuxtrois
2. un deux trois

#

```python
a = "chauve"
b = "souris"
print(a, b, sep="-")
```

\vfill

1. chauve-souris
2. chauve souris

#

```python
def ne_fait_rien():
    pass

ne_fait_rien()
```

\vfill

1. <rien>
2. ne_fait_rien

#

```python
def ne_renvoie_rien():
    a = 2
    b = 3
    c = a + b

résultat = ne_renvoie_rien()
print(résultat)
```

\vfill

1. <rien>
2. None

#

```python
fruits = ["pomme", "poire"]
print(len(fruits))
```

\vfill

1. 1
2. 2

#

```python
fruits = ["pomme", "poire"]
premier_fruit = fruits[0]
print(premier_fruit)
```

\vfill

1. pomme
2. poire


#

```python
prénoms = ["Alice", "Bob"]
print("Alice" in prénoms)
```

\vfill

1. True
2. False

#

```python
prénoms = ["Alice", "Bob"]
print("Ève" not in prénoms)
```

\vfill

1. True
2. False

#

```python
total = 0
liste_de_nombres = [1, 2, 3]
for élement in liste_de_nombres:
    total += élement
print(total)
```

\vfill

1. 0
2. 6

#

```python
prénoms = ["Alice", "Bob"]
prénoms[1] = "Charlie"
print(prénoms)
```

\vfill

1. ['Alice', 'Bob', 'Charlie']
2. ['Alice', 'Charlie']

#

```python
scores = {"Alice": 5, "Bob": 4}
score_d_alice = scores["Alice"]
print(score_d_alice)
```


\vfill

1. 5
2. 4

#

```python
scores = {"Alice": 5, "Bob": 4}
scores["Alice"] = 6
print(scores)
```

1. {'Alice': 6, 'Bob': 4}
2. {'Alice': 5, 'Bob': 4}

\vfill

#

```python
scores = {"Alice": 5, "Bob": 4}
scores["Charlie"] = 3
print(scores)
```

\vfill

1. {'Alice': 5, 'Bob': 4, 'Charlie': 3}
1. {'Alice': 5, 'Bob': 4}

#

```python
scores = {"Alice": 5, "Bob": 4}
del scores["Alice"]
print(scores)
```

\vfill

1. {'Alice': 5, 'Bob': 4}
1. {'Bob': 4}

#

```python
score_max = 0
scores = {"Alice": 5, "Bob": 6, "Charlie": 4}
gagnant = None
for prénom_du_joueur in scores:
    score_du_joueur = scores[prénom_du_joueur]
    if score_du_joueur >= score_max:
        score_max = score_du_joueur
        gagnant = prénom_du_joueur
print("gagnant:", gagnant, "score:", score_max)
```

\vfill

1. gagnant: Bob, score: 6
2. gagnant: Alice, score: 5

#

```python
mon_tuple = (42, 14)
print(42 in mon_tuple)
```

\vfill

1. True
2. False

#

```python
mon_tuple = (42, 14)
print(len(mon_tuple))
```

\vfill

1. 1
2. 2

#

```python
mon_tuple = (42,)
print(len(mon_tuple))
```

\vfill

1. 1
2. 2

#


```python
couple = ("Batman", "Robin")
héros, side_kick = couple
print(side_kick)
```

\vfill

1. Batman
2. Robin

#

```python
def tire_carte():
    valeur = "10"
    couleur = "trèfle"
    return (valeur, couleur)

v, c = tire_carte()
print(v, "de", c)
```

\vfill

1. 10 de trèfle
2. 5 de carreau


#

```python
class MaClasse:
    pass

mon_instance = MaClasse()
mon_instance.mon_attribut = 42
print(mon_instance.mon_attribut)
```

\vfill

1. 42
2. None

#

```python
class MaClasse:
    def ma_méthode(self):
        return 42

mon_instance = MaClasse()
print(mon_instance.ma_méthode())
```

\vfill

1. 42
2. None


#

```python
class MaClasse:
    def __init__(self):
        self.mon_attribut = 42

    def affiche_mon_attribut(self):
        print(self.mon_attribut)

mon_instance = MaClasse()
mon_instance.affiche_mon_attribut()
```

\vfill

1. 42
2. None

#

```python
class MaClasse:
    def méthode1(self):
        return 2

    def méthode2(self):
        return 3

    def grosse_méthode(self):
        résultat = self.méthode1() + self.méthode2()
        return résultat

mon_instance = MaClasse()
résultat = mon_instance.grosse_méthode()
print(résultat)
```

\vfill

1. 5
2. None

#

```python
class Chat:
    def __init__(self, nom):
        self.nom = nom
chat = Chat("Monsieur Moustaches")
print(chat.nom)
```

\vfill

1. None
2. Monsieur Moustaches

#

```python
class Chat:
    def __init__(self, nom):
        self.nom = nom

class Humain:
    def __init__(self,  prénom):
        self.prénom = prénom

    def adopte(self, chat):
        print(self.prénom, "adopte", chat.nom)

boule_de_poils = Chat("Boule de Poils")
bernard = Humain("Bernard")
bernard.adopte(boule_de_poils)
```

\vfill

1. Bernard adopte Boule de Poils
2. Boule de Poils adopte Bernard

#

```python
class Chat:
    def __init__(self, nom):
        self.nom = nom

    def ronronne(self):
        print(self.nom, 'fait: "prrrrr"')

    def caresse(self):
        self.ronronne()

boule_de_poils = Chat("Boule de poils")
boule_de_poils.caresse()
```
\vfill

1. rien
2. Boule de poils fait: "prrrrr"

#


```python
# Tous les enfants ont un chat!
class Enfant:
    def __init__(self, prénom, chat):
        self.prénom = prénom
        self.chat = chat

    def console(self):
        self.chat.caresse()

boule_de_poils = Chat("Boule de poils")
alice = Enfant("Alice", boule_de_poils)
alice.console()
```

1. rien
2. Boule de poils fait: "prrrrr"


#

\huge Atelier

On va implémenter un pense bête en ligne de commande.

# Consignes - 1

* Le programme doit lancer une boucle interactive.
* À chaque étape de la boucle, il faut afficher
  les choses à faire, par exemple:

```
[ ] faire ceci
[x] faire cela
```

\vfill

Ici, `faire ceci` est à faire, mais `faire cela` est fait.

# Consignes - 2

Ensuite, l'utilisateur peut enter des actions, déterminé
par le premier caractère:

```
> + faire un truc
# ajoute un élément "faire un truc" à la liste
> - 2
# supprime le deuxième élement de la liste
> x 1
# marque le premier élément comme fait
> o 3
# marque le troisième élément comme non fait
```

# Consignes - 3

Exemple d'interaction:

```
rien à faire pour le moment
> + faire un premier truc
1 [ ] faire un premier truc
> + faire autre chose
1 [ ] faire un premier truc
2 [ ] faire autre chose
> x 1
1 [x] faire un premier truc
2 [ ] faire autre chose
> x 2
1 [x] faire un premier truc
2 [x] faire autre chose
```

# Squelette - 1

Deux classes:

```python
class ChoseÀFaire:
    def __init__(self, contenu, fait): ...

class PenseBête:
    """ Contient une liste de choses à faire """
    def __init__(self):
        self.liste = []
    def ajouter(self, chose_à_faire): ...
    # Attention! les index commencent à 1
    def supprimer(self, index): ...
    def marquer_comme_fait(self, index): ...
    def marquer_comme_non_fait(self, index): ...
```

# Squelette - 2

Deux fonctions:

```python
def parse(entrée_utilisateur):
    """" Retourne un tuple (action, argument)
    Par exemple:
    >>> parse("+ quelque chose")
    ("ajouter", "quelque chose")
    >>> parse("- 2")
    ("supprimer", 2)
    """

def main():
    """" Boucle principale """
    ....
```
