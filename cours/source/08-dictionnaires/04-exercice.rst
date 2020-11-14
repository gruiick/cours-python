Exercice
========

Consignes
---------

Le but de l'exercice est d'implémenter un convertisseur d'unités de distance.

Il faut être capables de convertir des kilomètres, des miles, des yards, etc..

Le programme doit s'utiliser comme suit:

.. code-block:: console

   python convertisseur.py 1 km mi

Il y a trois "mots" après le nom du fichier, séparés par des espaces.
On appelle ces mots les "arguments" du programme.

Ici, ``1`` est la valeur de départ, ``km`` l'abbréviation de l'unité d'arrivée
et ``mi`` l'abbréviation de l'unité d'arrivée.

Voici un tableau pour vous aider:


=========   ============    ================
Nom         Abbréviation    Valeur en mẽtres
=========   ============    ================
mètre       m                1
kilomètre   km               1000
mille       mi               1609.344
yard        yd               0.9144
=========   ============    ================

Squelette
----------

Vous pouvez partir du code suivant:



.. literalinclude:: /extraits/convertisseur.py


Vous noterez que le programme est capable de récupérer la valeur,
l'unité de départ et l'unité d'arrivée correctement, mais que le
résultat est toujours égal à 1.0.

Votre objectif est de finir l'implémentation pour réaliser effectivement
la conversion.

À noter : vous n'avez pas besoin de changer l'implémentation des
fonctions ``main()`` et ``convertir()``, et ne vous inquiétez pas si
vous ne comprenez pas exactement ce que fait la fonction ``main()``, on
expliquera en détail comment elle fonctionne dans un chapitre ultérieur.
Pour terminer l'exercice, vous n'avez besoin que de modifier les
fonctions ``trouver_coefficient()``, ``conversion_en_mètres()`` et
``conversion_depuis_mètres()``.

À vous de jouer!
