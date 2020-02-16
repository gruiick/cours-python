Flot de contrôle
================

Pour l'instant, toutes les instructions que nous avons
écrites ont été exécutée une par une et dans l'ordre
d'apparition dans le code source.

Modifier l'ordre d'exécution de ces lignes s'appelle modifier le flot de
contrôle, et c'est  l'essence de la programmation!


if
++

On peut utiliser le mot ``if`` pour autoriser ou empécher
l'éxcution du code en-dessous::

   a = 3
   b = 4
   if a == b:
       print("a et b sont égaux")
   print("on continue")
   # affiche juste
   # on continue

La 4ème ligne n'est pas éxécutée parce la condition
est fausse.

Notes:

* il y a le caractère ``:`` (deux points) à la fin de la ligne
* le code en-dessous du ``if`` commence par 4 espaces: on appelle
  cela une *indentation*
* si la condition n'est pas vraie, rien ne se passe

Notez qu'on peut mettre uniquement une variable ou une valeur
après le if. Ceci ne fonctionne pas::

    if a = 3:
    	print("a égale 3")
    # affiche: SyntaxError

On parle aussi de "bloc" si plusieurs lignes sont identées::

   a = 3
   b = 4
   if a == b:
       # début du bloc
       print("a et b sont égaux")
       c = 2 * a
       # fin du block
   print("on continue")


if / else
---------

On peut utiliser le mot ``else`` après un condition en ``if``
pour éxécutér un bloc si la condition est fausse::

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
conditions::

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

On peut utiliser ``while`` pour répéter un bloc tant qu'une condition
est vraie::

    i = 0
    while i < 3:
        print(i)
        i = i + 1

.. code-block:: text

   0
   1
   2

Notez que la variable ``i`` passe par plusieurs valeurs différentes.

Boucle infinie
--------------

On parle de *boucle infinie* si la condition ne devient jamais fausse::

    while True:
    	print("spam!")

Dans ce cas, il faut appuyer sur ``CTRL-C`` pour interrompre
le programme.

Notez ici qu'on a mis directement la valeur ``True``, et non une comparaison.


Combiner while et if
--------------------

On peut "sortir" de la boucle ``while`` avec ``break``::

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
