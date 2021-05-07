Pile d'appels
=============

Reprenons un exemple de code qui provoque une erreur, par exemple en essayant
de diviser par zéro::

  def mauvaise_fonction():
      return 1 / 0

  def fonction_intermédiaire():
      mauvaise_fonction()

  def fonction_principale():
      fonction_intermédiaire()

  fonction_principale()


Si on lance ce code, voilà ce qu'on obtient::


  Traceback (most recent call last):
    File "mauvaises_maths.py", line 13, in <module>
      fonction_principale()
    File "mauvaises_maths.py", line 10, in fonction_principale
      fonction_intermédiaire()
    File "mauvaises_maths.py", line 6, in fonction_intermédiaire
      mauvaise_fonction()
    File "mauvaises_maths.py", line 2, in mauvaise_fonction
      return 1 / 0
  ZeroDivisionError: division by zero

Ceci s'appelle une *pile d'appels*. Elle permet de voir exactement par quelles fonction on est passé et
dans quel ordre. Elle se lit de haut en bas:

* On appelé `fonction_principale()`
* Cette fonction a à son tour appelé `fonction_intermédiaire()`
* `fonction_intermédiaire()` à appelé `mauvaise_fonction()`
* `mauvaise_fonction()` a levé une exception

Notez que chaque élément de la pile comprend:

* le nom de la fonction
* le chemin du module la contetant
* le numéro et la ligne précise du code qui a été appelé

Il est important de bien lire les piles d'appels quand on cherche
à comprendre d'où vient une exception.

Après la pile d'appels, on a le *nom* de l'exception et sa *description*.

