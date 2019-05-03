% Programmation avec Python (chapitre 11)
% Dimitri Merejkowsky

\center \huge Retour sur les exceptions

# A quoi sert finally?

```python
try:
    fp = open("file.txt")
    1 / 0
except ZeroDivisionError:
    print("got you")
finally:
    print("closing")
    fp.close()
```

versus:

```python
try:
    fp = open("file.txt")
    1 / 0
except ZeroDivisionError:
    print("got you")

fp.close()
```

# Réponse:

Que se passe-t-il si l'exception *n'est pas* ZeroDivisionError?


\center \huge Utiliser des bibliothèques tierces

Plan:

- sys.path
- difference debian/arch
- in $HOME
- PYTHONPATH

- so how do we put the code from pypi.org inside sys.path?
- setup.py

- pip

- example with tabulate
- TODO: example with more deps

- problemes:

- un seul .local/bin sur linux :/
- 2 projets avec des versions de deps differentes

# The rules

* One virtualenv per project
* One virtualenv per Python version
* Only use pip from *inside* a virtualenv

Tuto:

* let's install tabulate and requests
