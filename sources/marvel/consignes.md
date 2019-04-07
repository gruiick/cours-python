# Implémentation du jeu Marvel

## Introduction

De nombreux personnages sur developper.marvel.com n'ont pas de description. En revanche, ils ont tous une petite image (ou `thumbnail` en Anglais).

Le jeu consistera donc à:

* choisir  un personnage au hasard
* montrer l'URL de l'image
* demander au joueur le nom du personnage correspondant
* le joueur aura droit à 3 essais maximum

## Étape 1: préparation

* Créez un compte sur `developper.marvel.com` et une clé d'API
* Créez le fichier api-keys.txt avec le bon format
* Récupérez le fichier `marvel.py` sur [git.e2li.org]( https://git.e2li.org/index.cgi?p=dmerejkowsky/cours-python.git;a=blob_plain;f=sources/marvel/marvel.py;hb=HEAD)
* Vérfiez que le code fonctionne: `python3 marvel.py character-description Hulk`

## Étape 2: Rajouter une nouvelle requête

* Rajoutez une nouvelle classe `CharacterThumbnail`, dérivée de `Query`
* Vérifiez que l'url de l'image fonctionne, en l'ouvrant dans un navigateur

## Étape 3: Le deux clients

* Renommez la classe `Client` en `MarvelClient`.
* Rajoutez une clase abstraite `BaseClient`. Elle devra contenir les méthodes `get_all_characters()` et `get_character_thumbnail()`
* Créez une classe `FakeClient` qui dérive de `BaseClient`. Astuce:

```python
class FakeClient(BaseClient):
    characters = {
        "Hulk": "http://marvel/hulk.jpg",
        "Captain America": "https://marvel.com/captain.jpg",
    }

    def get_all_characters():
    	...
```

* Rajoutez la méthode `get_all_characters()` dans `BaseClient` et implémentez-là dans `FakeClient` et `MarvelClient`.
* Note:  Pour des raisons pratiques, on va limiter le nombre de personnages possibles (sinon le jeu serait bien trop difficile!). Utilisez le fichier `famous.txt` dans `MarvelClient.get_all_characters()`.


# Étape 4: Le jeu

Vous êtes maintenant prêts à implémenter le jeu lui-même.

Astuces:

* La classe `Game` prendra un `client` en paramètre de `__init__()`.
* Dans la fonction `main()`, utilisez la présence ou nom de la chaîne de
  charactères "--test" dans `sys.argv` pour choisir le client à utiliser
  (FakeClient ou MarvelClient)
