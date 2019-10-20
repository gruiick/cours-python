# Ateleir du sapin

Question: pourquoi etes vous-la ?

## Deroule de la session

Introduire deux concepts:

  - range()
  - imports

Annoncer l'exo: dessiner des sapins!

_Pourquoi: pour que vous sachiez faire tous seuls_

Example:

```
   #
  ###
 #####
#######
   #
   #
```



Faire le decoupage ensemble

1/ Demander une hauteur a l'utilisateur
2/ Faire une boucle qui va de 0 a hauteur
3/ Calculer le nombre de diese et l'esapce en
   debut de ligne a chaque pas
4/ Afficher " " * n + "#" * k
5/ Calculer l'espace pour le "pied"
6/ Dessiner le pied en repetant 2 fois
  la meme operation


Go!

Si ca se passe bien:

1/ Au fait, dans shutil il y a get_terminal_size
qui renvoie un tuple (colonnes, lignes) - pouvez-vous
dessiner un sapin qui prend tout l'espace disponible

2/ On va mettre des boules dans le sapin:

Dans random il y a randint() qui prend un intervale,
pouvez-vous mettre des `O` a la place des `#`?
