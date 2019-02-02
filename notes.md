Ce fichier contient diverses notes utiles à la préparation des futurs cours.

# Sujets à évoquer

* short circuit in if: `if a is not None and a.b == 42`
* files: "wa", accès séquentiel (chunk = file.read(chunk_size))
* style: trailing white space, editor configuration,
* [formatage de strings](fragments/format.md)
* liste par compréhension et filtres
* `help()`, doc en ligne (également en français)

* modules et packages:
  * scripts vs modules
  * débugger avec l'interpréteur avec `import/relod()`.
  * `if __name__ == "__main__"`

* décorateurs
* classes
    * héritage
    * super()
* Données binaires, encodage (binaire, ASCII, hexadécimal, unicode ...)

* virtualenv, pip, et bibliothèques tierces

* IDEs: don't use them ... yet (or ever)
    * linters,
    * déboguage
    * demo: pyflakes - black

* tests: pytest, TDD


# Idées d'ateliers

* Persistence de données (écriture/lecture de fichiers). Stocker les scores du pendu?

Parser du RSS et télécharger les émissions:

  * Source: https://github.com/dmerejkowsky/pypodget/
  * Concepts:
     * `setup.py`
     * scripts, entry points

* Remplacer Matlab par Python + numpy + matplotlib
* Effets audio
* Jeux vidéos (pygame)
* IOT : micro-controller, Rasberry Pi
* Blender/GIMP
* Stéganographie: cacher un texte dans une image

* Patcher des binaires Windows pour le fun?
