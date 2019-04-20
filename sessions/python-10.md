% Programmation avec Python (chapitre 10)
% Dimitri Merejkowsky

#

\center \huge Exceptions

# Examples d'erreurs

  * division par zéro
  * dépassement d'un tableau
  * clé non trouvée dans un dico
  * opération entre types incompatibles
  * le fichier n'existe pas
  * la variable n'existe pas

# Les backtraces

```python
def une_fonction():
	return 1 / 0

def une_autre_fonction():
    une_fonction()

une_autre_fonction()
```

# Les backtraces

```
Traceback (most recent call last):
  File "foo.py", line 7, in <module>
    une_autre_fonction()
  File "foo.py", line 5, in une_autre_fonction
    une_fonction()
  File "foo.py", line 2, in une_fonction
    return 1 / 0
ZeroDivisionError: division by zero
```


# Les backtraces

```python
def une_fonction(diviseur):
	return 1 / diviseur

def une_autre_fonction():
    une_fonction(diviseur=0)

une_autre_fonction()
```

# Les backtraces

```
Traceback (most recent call last):
  File "foo.py", line 7, in <module>
    une_autre_fonction()
  File "foo.py", line 5, in une_autre_fonction
    une_fonction(diviseur=0)
  File "foo.py", line 2, in une_fonction
    return 1 / diviseur
ZeroDivisionError: division by zero
```

# Lever une exception


```python
def retirer_somme(compte, montant):
   solde = ...
   if montant >= solde:
           raise ValueError("montant supérieur au solde!")
```

# Attraper une exception

```python
try:
    a = 1 / 0
    this_will_never_happen()
except ZeroDivisionError:
    print("someone tried to divide by zero!")
```

* Note: si l'exception n'est pas une fille de la classe attrapee, c'est rate.

# Attraper une exception

* On peut mettre plusieurs blocs de `except`
* On peut attraper plusieurs exceptions d'un coup


# Attraper une exception


```python
try:
    something_dangerous()
except ZeroDivisionError:
    print("tried to devide by zero")
except FileNotFoundError:
    print("file not found")
```



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
