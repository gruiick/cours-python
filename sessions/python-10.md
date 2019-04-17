% Programmation avec Python (chapitre 10)
% Dimitri Merejkowsky

\center \huge Rappels

* string formatting (%, .format(), f"")
* abstract base classes


\center \huge Exceptions

* Examples:
  * division par zéro
  * dépassement d'un tableau
  * clé non trouvée dans un dico
  * opération entre types incompatibles
  * le fichier n'existe pas
  * la variable n'existe pas

* les backtraces
  * comment les lire
  * y a un sens!

```python
def une_fonction():
	return 1 / 0

def une_autre_fonction():
    une_fonction()

une_autre_fonction()
```



```python
def une_fonction(diviseur):
	return 1 / diviseur

def une_autre_fonction():
    une_fonction(diviseur=0)

une_autre_fonction()
```

# Lever une exception

```python
def retirer_somme(compte, montant):
   solde = ...
   if montant >= solde:
           raise ValueError("montant supérieur au solde!")
```

# Attraper une exception

* Quand c'est pas le bon type, ben ça throw quand même
* On peut mettre plusieurs blocs de `catch`
* On peut attraper plusieurs exceptions d'un coup

Attention aux bare except

# Hiérarchies

À connaître
À utiliser si vous faites une librairie.

# finally, else

# WBYL et EAFP

Watch Before You Leap
Easier to Ask for Forgiveness than Permission

fichiers encore:

```python
if exists():
if pas_un_dossier():
if j_ai_les_droits_en_lecture():
open(filename):
```

```python
try:
    open(filename):
catch IOError:
    ...
```


# avec with


# attention a ou vous mettez except

```python
if truc:
    if machin:
        for bidule in chose:
            raise MyError("kaboom!")
````

```python
if truc:
    if machin:
        try:
            for bidule in chose:
                raise MyError("kaboom!")
        except:
        	...

```


```python
if truc:
    try:
        if machin:
            for bidule in chose:
                raise MyError("kaboom!")
    except:
	...

````


# Accédér aux détails de l'exceptions

* Avec `as`
* Attrribut `args`
* Parfois d'autres atttributs (voir la doc)
