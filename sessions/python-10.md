% Programmation avec Python (chapitre 10)
% Dimitri Merejkowsky

#

\center \huge Exceptions

# Exemple

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

ZeroDivisionError est une *classe*.

# Exemple modifié

```python
def une_fonction(diviseur):
	return 1 / diviseur

def une_autre_fonction():
    une_fonction(diviseur=0)

une_autre_fonction()
```

# Exemple modifié


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

**Prenez le temps de lire les backtraces soigneusement!**


# Exemples d'erreurs

  * `b += 2` - **NameError**
  * `a / 0` - **ZeroDivisionError**
  * `my_list[42]` -  **IndexError**
  * ``my_dict["bad-key"]`` - **KeyError**
  * `1 + "two"` - **TypeError**
  * `open("badpath")` - **FileNotFoundError**

# Hiérarchie d'exceptions (simplifiée)

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- OSError
      |    +-- FileNotFoundError
      +-- TypeError
      +-- ValueError

```

Liste complète dans la documentation:
https://docs.python.org/fr/3/library/exceptions.html#exception-hierarchy

# KeyboardInterrupt et SystemExit

* `KeyboardInterrupt` est levée quand on fait `ctrl-c`.

* `SystemExit` est levé quand on utilise `sys.exit()`
  * Python cache la backtrace dans ce cas-là
  * Pas utile de l'attrapper en général


# Attraper une exception

```python
try:
    a = 1 / 0
    this_will_never_happen()
except ZeroDivisionError:
    print("someone tried to divide by zero!")
```

* Note: si l'exception n'est pas une fille de la classe attrapée, c'est raté.

# Attraper une exception

On peut mettre plusieurs blocs de `except`

```python
try:
    something_dangerous()
except ZeroDivisionError:
    print("tried to devide by zero")
except FileNotFoundError:
    print("file not found")
```

# Attraper une exception

On peut attraper plusieurs exceptions d'un coup

```python
try:
    something_dangerous()
except (ZeroDivisionError, FileNotFoundError):
   print("something bad happened")
```

# finally, else


```python
try:
	something_dangerous()
except SomeError:
    print("something bad happened")
else:
    print("everything went well")
finally:
    clean_up()
```

# WBYL

* Watch Before You Leap

```python
if exists():
    if pas_un_dossier():
        if j_ai_les_droits_en_lecture():
            open(filename):
```

# EAFP

* Easier to Ask for Forgiveness than Permission

```python
try:
    file = open(filename)
except IOError:
    ...
finally:
   file.close()
```

# Avec with

Pas besoin de `finally` :)

```python
try:
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Fichier non trouvé")
```

L'exception est capturée, le fichier est fermé, puis  l'exception est
levée à nouveau.

# Attention à la position du except

```python
if truc:
    if machin:
        for bidule in chose:
            raise MyError("kaboom!")
````

# Attention à la position du except

```python
if truc:
    if machin:
        try:
            for bidule in chose:
                raise MyError("kaboom!")
        except:
        	...

```

# Attention à la position du except

```python
if truc:
    try:
        if machin:
            for bidule in chose:
                raise MyError("kaboom!")
    except:
	...

````

# Accédér aux détails de l'exception

* Avec `as`:

```python

try:
    something_dangerous()
except FileNotFoundError as error:
    print("file not found:", error.filename)
```

\vfill

Voir la documentation pour les attributs disponibles.


# Lever une exception

* Avec raise

```python
def retirer_somme(compte, montant):
   solde = ...
   if montant >= solde:
           raise ValueError("montant supérieur au solde!")
```

# Créer vos propres exceptions

Toujours hériter de `Exception`.

```python
class BankError(Exception):
    ....

class NotEnoughMoney(BankError):
    def __init__(self, amount, withdrawal):
         self.amount = amount
         self.withdrawal = withdrawal
```

#

\center \huge Atelier

# Convertisseur d'unités

Miles en kilomètres, gallons en litres, etc.

#

\center \huge Pour la prochain fois

* Rajouter le support d'autres unités (comme les volumes, ...)
* Gérer toutes les erreurs possibles (unité non trouvée, ...)

Plus dur:
* Gérer les vitesses (mètres par secone vers miles par heure)
* Gérer les températures (dégres Celsius vers Farenheit)
* Gérer les monnaies
