Levée d'exceptions
==================

raise
-----

On peut lever explicitement un exception en appelant le mot-clé ``raise`` suivi
d'une **instance** d'une classe.

Par exemple en utilisant une exception native::

    def dire_bonjour(prénom):
        if not prénom:
            raise ValueError("prénom vide")

Définition d'exceptions à la carte
-----------------------------------

On peut ré-utiliser les exceptions natives, ou définir sa propre classe::

    class OpérationImpossible(Exception):
        pass


    def ma_fonction():
        if cas_impossible:
            raise OpérationImpossible()

Gérer puis re-lever l'exception géré
-------------------------------------

Parfois il est utile de re-lever l'exception qu'on vient de géner.

Dans ce cas, on utilise ``raise`` sans argument::

    try:
        tente_un_truc_risqué()
    exeept ArithmeticError:
        ...
        raise
