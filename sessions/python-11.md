% Programmation avec Python (chapitre 11)
% Dimitri Merejkowsky

\center \huge Retour sur les exceptions

# A quoi sert finally

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

Que se passe-t-il si on remplace `1/0` par
`my_list[42]` ?

\center \huge Libraries tierces

# Introduction: pip

* python3 -m pip
* `--user`

But: what about several projects?

# Virtualenvs

# pip + virtualenv = <3

# Tuto

* Let's install requests!

```
# avant

# après
```

