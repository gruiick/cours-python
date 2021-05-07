Contrôle de flux
================

Pour l'instant, toutes les instructions que nous avons
écrites ont été exécutée une par une et dans l'ordre
d'apparition dans le code source.

De plus, chaque ligne était constituée d'une unique expression.

Modifier l'ordre d'exécution de ces instructions s'appelle le *contrôle de
flux*, et c'est l'essence même de la programmation !


if
++

On peut utiliser le mot-clé ``if`` pour autoriser ou empêcher
l'exécution des instructions suivantes : ::

   a = 3
   b = 4
   if a == b:
       print("a et b sont égaux")
   # n'affiche rien

La 4ème ligne n'est pas exécutée parce la condition
est fausse.

Notes:

* il y a le caractère ``:`` (deux points) à la fin de la ligne ;
* le code en-dessous du ``if`` commence par 4 espaces : on appelle
  cela une *indentation*.

Notez qu'on a utilisé une **expression** après le if.
On ne peut pas utiliser d'instruction après un ``if`` en Python.

Autrement dit, ce code ne fonctionne pas : ::

    if a = 3:
        print("a égale 3")
    # affiche: SyntaxError

On parle aussi de "bloc" si plusieurs lignes sont indentées : ::

   a = 3
   b = 4
   if a == b:
       # début du bloc
       print("a et b sont égaux")
       c = 2 * a
       # fin du bloc

Notez qu'on reprend l'ordre habituel d'exécution des instructions s'il
y a un bloc indenté dans l'autre sens après le ``if`` : ::

   a = 3
   b = 4
   if a == b:
       # début du bloc
       print("a et b sont égaux")
       c = 2 * a
       # fin du bloc
   # on est après le bloc if
   print("on continue")


Ce code n'affiche pas "a et b sont égaux", mais affiche bien "on continue".


if / else
---------

On peut utiliser le mot-clé ``else`` après un condition en ``if``
pour exécuter un bloc si la condition est fausse : ::

   a = 3
   b = 4
   if a == b:
       print("a et b sont égaux")
   else:
       print("a et b sont différent")
   # affiche: a et b sont différents


if / elif
---------

On peut utiliser ``if``, ``elif`` et ``else`` pour enchaîner plusieurs
conditions : ::

    age = 23
    if age < 10:
        print("âge inférieur à dix")
    elif 10 <= age < 20:
        print("âge entre 10 et 20")
    elif 20 <= age < 40:
        print("âge entre 20 et 40")
    else:
        print("âge supérieur à 40")
    # affiche: âge entre 20 et 40


while
-----

On peut utiliser le mot-clé ``while`` pour répéter un bloc tant qu'une condition
est vraie : ::

    i = 0
    while i < 3:
        print(i)
        i = i + 1

.. code-block:: text

   0
   1
   2

Notez que la variable ``i`` passe par plusieurs valeurs différentes.

Le fait de répéter un bloc plusieurs fois est souvent appelée une
*boucle*.

Boucle infinie
--------------

On parle de *boucle infinie* si la condition ne devient jamais fausse : ::

    while True:
        print("spam!")

Dans ce cas, il faut appuyer sur ``CTRL-C`` pour interrompre
le programme.


Combiner while, if, et break
----------------------------

On peut "sortir" de la boucle ``while`` avec le mot-clé ``break`` : ::

    i = 0
    while True:
        i = i + 1
        print(i)
        if i > 3:
            break

.. code-block:: text

   1
   2
   3
   4
