# Cours Python E2L - 04 avril 2020 - par internet

## Notes

Ces notes accompagnent la vidéo disponible sur le site de l'E2l.

Elles contiennent des corrections, des liens et des approfondissements
sur ce qui a été dit en direct, et peut également servir
de guide pour retrouver les sujets qui vous intéressent dans la vidéo.

## Introduction : curseur confort /contrôle

Rien de particulier à dire sur cette section

## À partir de 02m17s : Arch Linux

Site: https://archlinux.org

Un lien sur Manjaro, écrit par un mainteneur d'Arch Linux:
http://allanmcrae.com/2013/01/manjaro-linux-ignoring-security-for-stability/

## À partir de 05m31s : screenkey

Pas de lien malheureusement, le projet n'est plus maintenu :/

## À partir de 06m51s : i3

Site:  https://i3wm.org/

13:23
Je voulais faire un workspace avec `thunderbird` et un autre avec `firefox`, mais
au final j'en ai crée deux avec `firefox`, désolé.


19:13
Je dis "workspace 1 et 2" mais en réalité les workspaces `tmux` commencent
à zéro, pas à un.

## À partir de 20m04s : kitty

21:35
À ajouter : dans less, `/` permet de chercher, et `q` de quitter

21:49:
en fait, kitty ne lance pas un "équivalent" de less, il lance `less` mais avec
la sortie de toutes les commandes

24:00:
En fait, l'ouverture de liens ne marche que sur le lien est effectivement
dans ce qui est affiché par kitty *dans la fenêtre visible*, là le lien
que j'essayais d'ouvrir était caché - une bonne solution aurait été
de passer par le pager

## À partir de 26m24:  kakoune

27:23
Je veux parler de numéros de ligne bien sûr, pas de colonne!

28:33
"touches du clavier" - par opposition au pavé numérique qui contient les
flèches - toutes les touches sont sur un clavier !

29:13
"le truc avec les numéros" - autrement connu sous le nom de "pavé numérique" :)

30:26:
Je voulais dire qu'on passe souvent plus de temps à se *déplacer*
ou à *modifier* du contenu existant que simplement *insérer* du contenu tout
neuf. C'est évident pour le code je pense, mais c'est aussi souvent le cas
pour le texte aussi.

32:47:
Notez qu'on exécute une commande kakoune en tapant son nom et en finissant par `entrée`,
un peu comme les commandes du terminal

34:50:
En fait je voulais prendre des commandes similaires mais je me suis
trompé de paire:
* `gt`, et `gb` déplacent le *curseur* pour qu'il soit en haut ou en bas de la fenêtre
* `vt`, et `vb` déplacent la *fenêtre* pour que le *curseur* soit en haut ou en bas.

35:28:
'v' entre dans le mode "vue" - il n'y a de mode "visuel" dans kakoune

36:28:
Il est assez facile de trouver sur Internet des témoignages (en Anglais)
de personnes qui passent de vim à kakoune par exemple - lisez-les si vous voulez,
mais le mieux pour vous faire un avis et d'essayer par vous-même ;-)

38:15:
On utilise souvent "couper" au lieu de "détruire"

39:18:
Ma langue a fourché : pour copier ou utilise un `y` minuscule. La touche 'Y' (en majuscule)
ne fait rien de particulier dans le mode normal.

39:36:
J'ai oublié de parler de 'c' qui coupe puis rentre en mode insertion

40:55:
Pour info, le rectangle à droite contient une liste des "complétions" possibles,
sujet que je n'ai pas abordé pour des questions de temps.

43:12:
Ici si vous mettez la vidéo en pause et regardez attentivement screenkey,
vous verrez passer deux fonctionnalités dont je n'ai pas parlé:

   * utiliser '/' pour chercher
   * et le fait qu'avec kakoune, vous cherchez en fait toujours des
     *expressions* rationnelles (d'où le `\` avant l'accolade)

48:36:
Je n'ai pas été très clair ici:
`Super-h` est une commande de `i3` qui est disponible tout le temps,
et qui sélectionne la fenêtre de gauche, et `h` est une commande pour
aller à gauche dans `kakoune`.
Mais `super-h` n'est *pas* une commande kakoune - il se trouve juste que si
j'ai deux fenêtres kakoune dans i3, ce raccourci ira sur la fenêtre de gauche.

49:33:
Si vous regardez bien screenkey on ne me voit jamais taper `lire_répertoire`
en entier.
En fait, on me voit utiliser l'auto-complétion : comme le mot `lire_répertoire` existe
déjà dans le buffer, un petit menu s'affiche et juste en tapant quelques lettres
(lie) je limite la liste des complétions possible, puis enfin j'utilise
`ctrl-n` pour naviguer dans les suggestions et finalement insérer le mot
en entier. On retrouve le principe de complétion qu'on
avait vu avec dmenu

50:23:
Au passage, la communauté kakoune est encore assez petite, donc le cas de
l'édition collaborative ne se présente pas souvent !

50:50
Je parle du texte à *droite* bien sûr !

# À partir de 1h01m25s : ranger et virtualenv

Rien à signaler ici

# À partir de 1h05m39s : black et pyflakes

Rien à signaler ici non plus

