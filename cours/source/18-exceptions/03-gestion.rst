Gestion des exceptions
======================

Bloc try/except
---------------

On peut *gérer* (ou *attraper*) une exception en utilisant un bloc
``try/except`` et le nom d'une classe d'exception::


    try:
        a = 1 / 0
    except ZeroDivisionError:
        print("Quelqu'un a essayé de diviser par zéro!")

   # Affiche: Quelqu'un a essayé de diviser par zéro!

À noter : le bloc dans ``try`` s'interrompt dès que l'exception est levée,
et on ne passe dans le bloc ``except`` que si une exception a effectivement
été levée.

.. code-block:: python

    x = 14
    y = 0
    try:
        z = x / y
        print("z vaut", z)
    except ZeroDivisionError:
        print("Ouelqu'un a essayé de diviser par zéro!")

   # Affiche: Ouelqu'un a essayé de diviser par zéro!


Notez que la ligne ``print("z vaut", z)`` n'as pas été exécutée.

Autr exemple:


.. code-block:: python

    x = 14
    y = 2
    try:
        z = x / y
        print("z vaut", z)
    except ZeroDivisionError:
        print("Ouelqu'un a essayé de diviser par zéro!")

   # Affiche: 'z vaut 7.0'

Notez que la ligne ``print("Ouelqu'un a essayé de diviser par zéro!")`` n'as pas été exécutée.

Gestion de plusieurs exceptions
--------------------------------

Le mot après ``except`` doit être celui d'une classe, et l'exception n'est gérée
que si sa classe est **égale ou une fille** de celle ci.

Par exemple, ceci fonctionne car ``ZeroDivisionError`` est bien une fille
de la classe ``ArithmeticError``::

    x = 14
    y = 0
    try:
        z = x / y
        print("z vaut", z)
    except ArithmeticError:
        print("Ouelqu'un a essayé une opération impossible")


On peut aussi mettre plusieurs blocs de ``except``::


  try:
      tente_un_truc_risqué()
  except ZeroDivisionError:
      print("raté : division par zéro!")
  except FileNotFoundError:
      print("raté : fichier non trouvé")

Ou gérer des exception de classes différentes avec le même bloc::

  try:
      tente_un_truc_risqué()
  except (ZeroDivisionError, FileNotFoundError)
      print("raté!")

Accéder à la valeur de l'exception
-----------------------------------

On peut récupérer l'instance de l'exception levée avec le mot-clé ``as``::

  try:
      ouvrir_fichier()
  except FileNotFoundError as e:
      print("le fichier: ", e.filename, "n'existe pa")


Ici on utilise l'attribut ``filename`` de la classe ``FileNotFoundError``
pour afficher un message d'erreur
