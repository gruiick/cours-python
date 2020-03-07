% Programmation avec Python (Épisode 11)
% Dimitri Merejkowsky


# Quiz

#

```python
class A:
   def méthode_dans_a(self):
       print("dans A")

class B(A):
   def méthode_dans_b(self):
       print("dans B")


b = B()
print(b.méthode_dans_a())
```

\vfill

1. Erreur
2. Affiche 'dans A'

#



```python
class A:
    def méthode_dans_a(self):
         print("dans A")

class B(A):
    def méthode_dans_b(self):
         print("dans B")

class C(B):
    def méthode_dans_c(self):
         print("dans C")

c = C()
c.méthode_dans_a()
```

\vfill

1. dans A
2. dans B
3. dans C

#


```python
class A:
    def __init__(self):
        self.attribut_de_a = 42

class B(A):
    def affiche_a(self):
        print(self.attribut_de_a)

```

\vfill

1. Affiche '42'
2. Erreur

#

```python
class A:
   def une_méthode(self):
       print("je viens de la classe A")

class B(A):
    def une_méthode(self):
        print("je viens de la classe B")



b = B()
b.une_méthode()
```

\vfill

1. je viens de la classe A
2. je viens de la classe B

#

```python
class A:
   def une_méthode(self):
       print("je viens de la classe A")

class B(A):
    def une_méthode(self):
        super().une_méthode()
        print("je viens de la classe B")
```

\vfill

1. Affiche 'je viens de classe A' puis 'je viens de la classe B'
1. Affiche 'je viens de classe B' puis 'je viens de la classe A'

#

```python
class A:
   def __init__(self):
       self.attribut_de_a = "Bonjour"

class B(A):
    def __init__(self):
       self.attribut_de_b = "monde"
       super().__init__()


b = B()
print(b.attribut_de_a + " " + b.attribut_de_b)
```

\vfill

1. Erreur
2. Affiche: "bonjour monde"
