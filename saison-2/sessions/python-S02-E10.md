% Programmation avec Python (Épisode 10)
% Dimitri Merejkowsky


# Quiz

#

```python
print(0b110)
```

\vfill

1. 3
2. 6


#

```python
print(0x1F)
```

\vfill

1. 31
2. 12

#

```python
x = ord('c') - ord('a')
print(x)
```

\vfill

1. 2
2. 'b'

#

```python
n = ord('a')
y = chr(n + 4)
print(y)
```

\vfill

1. 3
2. 'e'

#

```python
data = bytearray(b"bonjour")
data[0] = 18
print(data)
```

\vfill

1. `bytearray(b'\x12onjour')`
2. `bytearray(b'18onjour')`


#

```python
message = "J'aime le café"
print(message.encode())
```

\vfill

1. b"J'aime le cafe"
2. b"J'aime le caf\\xc3\\xa9"

#

```python
message = "J'aime le caf\xc3\xa9"
print(message.decode())
```

\vfill

1. "J'aime le caf?"
2. "J'aime le café"

#

```python
# le fichier message.txt contient la ligne:
"Salut ça va ?"
f = open("message.txt", "r")
contenu = f.read()
print(contenu)
f.close()
```

\vfill

1. Salut ça va ?
2. *rien*

\vfill

#

```python
# le fichier réponse.txt est vide
f = open("réponse.txt", "w")
f.write("Ça roule")
f.close()
```

\vfill

Que contient le fichier `réponse.txt` ?

1. il est vide
2. "Ça roule"

#

```python
# le fichier poème.txt est vide
f = open("poème.txt", "w")
f.write("Un viel étang\n")
f.write("Une grenouille qui plonge\n")
f.write("Le bruit de l'eau")
f.close()
```

\vfill

Que contient le fichier `poème.txt` ?

1. Un joli haïku
2. Une recette de cuisine
