Chaînes de caractères
======================

Les chaînes de caractères, aussi appelées "strings", permettent
de représenter du texte. On a utilisé une string pour afficher
"bonjour monde" dans le chapitre précédent.

On écrit toujours les strings entre guillemets (ou quotes).

soit avec des doubles guillemets : ::

    print("Bonjour monde!")
    # affiche: Bonjour monde!

soit avec des guillemets simples : ::

    print('Bonjour monde!')
    # affiche:  Bonjour monde!

Double et simple quotes
-----------------------

On peut mettre des simples quotes dans des double quotes et vice-versa : ::


   print("Il a dit: 'bonjour' ce matin.")
   # affiche: Il a dit: 'bonjour' ce matin.

   print('Il a dit: "bonjour" ce matin')
   # affiche: Il a dit: "bonjour" ce matin


Échappement
-----------

On peut aussi *échapper* des caractères avec la
barre oblique inversée ``\\`` - backslash.


.. code-block:: python

   print('Il a dit: "bonjour". C\'est sympa!')
   # affiche: Il a dit: "bonjour". C'est sympa!


Concaténation
-------------

On peut construire de longues chaînes de caractères en
en concaténatant de plus petites, avec l'opérateur ``+`` : ::

   name = "John"
   message = "Bonjour " + name + " !"
   print(message)
   # affiche: Bonjour John !


Répétition
-----------

On peut construire une longue string en répétant
la même petite string plusieurs fois avec l'opérateur
`*` : ::

    message = "Na" * 3
    print(message)
    # affiche: NaNaNa
