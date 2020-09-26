% Python Épisode 4
% Dimitri Merejkowsky
% E2L

\huge \center Rappels

# print

Afficher quelque chose dans la console:

\vfill

```python
print("Bonjour, monde")
```

\vfill

*Affiche: Bonjour, monde*

# Commentaires

Les lignes qui commencent par un `#` sont ignorées:

\vfill

```python
# Ceci est un commentaire
print("Bonjour, monde")
```

\vfill

*Affiche: Bonjour, monde*

# Maths (1)

* `+`, `*`, `-`, `/`

\vfill

```python
print(1 + 2)
```

\vfill

*Affiche: 3*

# Maths (2)

Opérations: `//`, `%`


```python
print(14 // 3)
print(14 % 3)
```

\vfill

*Affiche 4, puis 2*


# Instructions et expressions

* Les instructions sont *exécutées*
* Les expressions sont *évaluées*


# Exemple

```python
print(1+2)
```

\vfill

* Évaluation de l'expression `1+2` (ça fait `3`)
* Exécution de l'instruction `print`
* Affiche `3`

# Variables


```python
a = 2
b = 3
c = a + b
print(c)
```

\vfill

* Assigne 2 à la variable `a`
* Assigne 3 à la variable `b`
* Assigne le résultat de l'évaluation de `a+b` à c (5)
* Affiche 5

# Chaînes de caractères (strings)

Avec des `"` ou des `'`

\vfill

```python
print("Il a dit: 'bonjour' ce matin.")
```
*Affiche: Il a dit: 'bonjour' ce matin*

\vfill

```python
print('Il a dit: "bonjour" ce matin')
```
*Affiche: Il a dit: "bonjour" ce matin*

# Concaténation

Avec `+`

\vfill

```python
prénom = "Marie"
message = "Bonjour " + prénom
print(message)
```

\vfill

*Affiche: Bonjour Marie*

# Conversions (1)

Entier vers string avec `str()`:

\vfill

```python
x = 40
y = 2
message = "La réponse est: " + str(x + y)
print(message)
```

\vfill

*Affiche: La réponse est 42*

# Conversions (2)


String vers entier avec `int()`:

\vfill

```python
quarante_en_chiffres = "40"
réponse = int(quarante_en_chiffres) + 2
```

\vfill

*Assigne 42 à la variable `réponse`*.


# Opérations booléennes (1)

Renvoient `True` ou `False` après évaluation:

\vfill

+-------+-----------------------------+
|``==`` | égal                        |
+-------+-----------------------------+
|``!=`` | différent                   |
+-------+-----------------------------+
|``>``  | strictement supérieur       |
+-------+-----------------------------+
|``>=`` | supérieur ou égal           |
+-------+-----------------------------+
|``<``  | strictement inférieur       |
+-------+-----------------------------+
|``<=`` | inférieur ou égal           |
+-------+-----------------------------+

# Exemples


```python
âge = 14
peut_conduire = (âge >= 18)
```

\vfill

*Assigne* la valeur `False` *à la variable* `peut_conduire`.


# Opérations (2)


+-------+-----------+
|``not``| négation  |
+-------+-----------+
|``and``| et        |
+-------+-----------+
|``or`` | ou        |
+-------+-----------+

```python
il_pleut = True
j_ai_un_parapluie = False
je_suis_mouillé = il_pleut and not j_ai_un_parapluie
```

\vfill

*Assigne la valeur* `True` *à la variable* `je_suis_mouillé`.

#

\center \huge Contrôle de flux

# Contrôle de flux

* Modifier l'ordre d'exécution des instructions.
* Utiliser des blocs:
    * `:`, retour à la ligne, indentation


# if / else


```python
a = 3
b = 4
if a == b:
   print("a et b sont égaux")
else:
   print("a et b sont différents")
```

\vfill

* Assigne `3` à la variable `a`
* Assigne `4` à la variable `b`
* Évalue l'expression `a == b`. (`False`)
* Saute l'exécution du bloc après le `if`
* Exécute le bloc après le `else`
* Affiche *a et b sont différents*


# while

Évalue le bloc tant que l'expression après le `while` renvoie
`True`:

```python
i = 0
while i < 3:
    print(i)
    i = i + 1
```

\vfill

*Affiche 0, puis 1, puis 2*

# while, if, et break

Interrompre une boucle avec `break`:

```python
i = 0
while True:
    i = i + 1
    print(i)
    if i > 3:
        break
```

\vfill

*Affiche 1, puis 2, puis 3, puis 4*
