Exercice
========

Le but de l'exercice est d'implémenter le jeu du pendu.

Voila à quoi une session de jeu doit ressembler:



.. code-block:: text

  ______
  entrer une lettre
  e
  _____e
  entrer une lettre
  a
  _a___e
  entrer une lettre
  u
  _au__e
  entrer une lettre
  q
  _au__e
  entrer une lettre
  c
  _auc_e
  entrer une lettre
  h
  _auche
  entrer une lettre
  g
  gauche
  Gagné

Consignes
---------

* Télécharger les fichiers :download:`pendu.py </extraits/pendu.py>` et :download:`mots.txt </extraits/mots.txt>`.

* S'assurer que le code fonctionne en lançant ``python3 pendu.py``

* À ce stade, vous devriez constater plusieurs problèmes:

  * Au lieu d'avoir un mot au hasard, le mot à deviner est toujours ``accord``
  * Au lieu d'afficher un indice, le code affiche une liste de tentatives
  * Le jeu est impossible à gagner parce que la fonction ``a_gagné`` renvoie toujours ``False``

Le but de l'exercice est de corriger ces 3 problèmes.

