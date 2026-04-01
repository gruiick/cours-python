Fichiers
========

Ouvrir un fichier en lecture
----------------------------

Fichiers "textes" et fichiers "binaires"
++++++++++++++++++++++++++++++++++++++++

Cela vous est peut-être déjà arrivé : Imaginons que vous ayez dans
votre répertoire courant un code source python dans ``mon_script.py``
et un pdf dans ``cours.pdf``.

Vous pourrez ouvrir ``mon_script.py`` dans un éditeur de texte,
mais pas ``cours.pdf``, ou alors ça affichera n'importe
quoi.

En Python, on utilise la fonction native ``open()``, en passant en argument
le chemin du fichier.

Selon que l'on veuille accéder au *texte* dans le fichier ou aux données
binaires qui sont à l'intérieur, on utilisera l'argument ``"r"`` ou ``"rb"``
('r' comme 'read', et 'b' comme 'binary')

Enfin, ``open()`` renvoie un "file-objet", qu'on note souvent
'f', qui contient une méthode ``read()`` pour lire le contenu
du fichier.

En pratique, voici ce que cela donne : ::

    f = open("mon_script.py", "r")
    code = f.read()
    print(code)
    # affiche le code présent dans le fichier mon_script.py

    f = open("cours.pdf", "rb")
    données = f.read()
    # données est maintenant une grosse suite
    # d'octets

    f = open("cours.pdf", "r")
    f.read()
    # Erreur: UnicodeDecodeError: 'utf-8' codec can't
    # decode byte 0xd0 in position 10


Comme on doit utilisé l'option ``rb`` pour lire le pdf, on dit parfois
que le fichier ``pdf`` est un fichier "binaire", par opposition avec
``mon_script.py`` qui est un fichier "texte".

Ça n'a pas vraiment de sens : les deux fichiers sont stockés sur votre
ordinateur comme des suites d'octets, indépendamment de leur contenu.

Il se trouve que l'un des deux contient une suite d'octets qui est
décodable en tant que string. En fait, sous le capot, la suite d'octets
renvoyée dans le premier example a été décodée avec l'encodage par défaut
de votre système. On peut d'ailleurs passer l'encodage en argument à
``open()`` : ::

    f = open("vieux_texte_en_latin_1.txt", "r", encoding="latin-1")
    texte = f.read()

Ouvrir un fichier en écriture
-----------------------------

On peut aussi *écrire* dans un fichier, toujours avec ``open()``,
mais cette fois-ci avec la méthode ``write()`` du file-objet.

On peut écrire du texte avec l'option ``"w"`` et une chaîne de
caractères : ::

    f = open("mon_script.py", "w")
    f.write("Nouveau contenu!")

Et écrire directement des données binaires avec ``"wb"`` et
une suite d'octets ::

    f = open("cours.pdf", "wb")
    f.write(b"\x0c\x1f...")

Encore une fois, sous le capot, la chaîne de caractères sera encodée par
Python avant d'être écrite dans le fichier texte.


Fermeture des file-objets
-------------------------

Notez qu'il est impératif de fermer les fichiers que vous ouvrez, que ce soit
en lecture ou en écriture, en appelant la méthode ``close()`` : ::

    f = open("mon_poéme.py", "w")
    f.write(premier_vers)
    f.write(deuxième_vers)
    f.close()

Conseils
--------

* On utilise souvent le binaire pour échanger entre Python et le monde extérieur.
* Tout texte a un *encodage*, et il vous faut connaître cet encodage pour travailler avec.
* Si vous avez le choix, utilisez UTF-8.
