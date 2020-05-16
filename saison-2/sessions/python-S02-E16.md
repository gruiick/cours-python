# Cours Python E2L - 16 mai 2020 - par internet

# Git - 2ème partie

## Notes

Ces notes accompagnent la vidéo disponible sur le site de l'E2L.

* 13:56

Dit autrement, si `foo.py` et `bar.py` ont le même contenu, il n'y aura
qu'un seul "blob" pour ce contenu. (et un tree à deux éléments) -
On appelle ce phénomène une *déduplication*.

Une autre optimisation consiste à stocker des *différences*. Par exemple, si le mardi foo.py contient 3 lignes, et le mercredi seule la 2ème ligne
a changé, git ne stockera qu'une ligne au lieu de 3)

Git combine tout cela pour faire des *packs*, mais c'est un poil complexe donc
je vais pas rentrer trop dans les détails.

* 17:11

`git log` peut s'utiliser avec plein d'options. On peut aussi utiliser
`got log -p` pour voir les modifications apportées par chaque commit,
avec en rouge ce qui a été supprimé, et en vert ce qui a été
rajouté.

* 18:36

Certains forges autorisent même d'avoir des permissions spécifiques à certaines branches.

* 28:52

Ma langue a fourché:

* les changements dans "Staged Changes" en bas feront partie du prochain commit
* les changements dans "Unstaged Changes" en haut ne feront pas partie du prochain commit.

* 29:56

Précision: `git branch` sans arguments liste toutes les branches locales. La branche courante
est représentée par une étoile en début de ligne et une couleur différente.

* 30:10

Nommer des choses en informatique c'est toujours compliqué - que ce soit les noms
de variables, de fonctions de classes ou de branches :P

* 41:07

Un point important que j'ai oublié de mentionner : la commande `pull` qu'on a utilisé
est simplement une combinaison de `fetch` puis `merge`, en tout cas dans les cas simples.

* 41:51

J'ai pas été très clair ici : certaines des fonctionnalités de `git gui`
que je vous ai montrées sont aussi faisables directement avec la commande
`git add -p`.

* 51:59

D'ailleurs si vous avez un git assez récent, vous verrez que
les fonctionnalités de `checkout` on été découpées en deux
avec d'un côté `git switch` et de l'autre `git restore`.

Je vous recommande d'utilisez celles-là si vous pouvez.
(moi j'utilise tout le temps `checkout` par habitude)

* 52:38

Le livre officiel sur Git, en Français, très complet : https://git-scm.com/book/fr/v2
