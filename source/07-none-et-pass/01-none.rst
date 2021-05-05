None
====

Définition
-----------

``None`` est un mot-clé qui sert à représenter l'absence.

Un peu comme ``True`` et ``False`` qui sonts des mot-clés qui réprésentent des booléens.

Retourner None
----------------

En réalité, *toutes* les fonctions pythons retournent *quelque chose*, même quand
elle ne contiennent pas le mot-clé ``return``.::

   def ne_renvoie_rien():
       x = 2

   resultat = ne_renvoie_rien()

   print(resultat)
   # affiche: None

Opérations avec None
---------------------

La plupart des fonctions que nous avons vues échouent si on leur passe ``None``
en argument::

    x = len(None)
    # erreur: TypeError

    x = None < 3
    # erreur: TypeError

    x = int(None)
    # erreur: TypeError

Mais ``str`` fonctionne::

    x = str(None)
    print(x)
    # affiche: 'None'

On peut vérifier si une variable vaut ``None`` avec ``is None``::

    x = ne_renvoie_rien()
    print(x is None)
    # affiche: True

Example d'utilisation
----------------------

.. code-block:: python

    def trouve_dans_liste(valeur, liste):
        for element in liste:
            if element == valeur:
                return element
        return None

    x = trouve_dans_liste(2, [1, 2, 3])
    print(x)
    # affiche: 2

    x = trouve_dans_liste(1, [3, 4])
    print(x)
    # affiche: None
