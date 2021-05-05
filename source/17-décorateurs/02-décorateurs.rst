Décorateurs
============

Définition
------------

Un décorateur est une fonction qui *enveloppe* une autre fonction.

On place le nom du décorateur avec une arobase (``@``) au-dessus
de la fonction décorée::

    def mon_décorateur(fonction):
        def fonction_retournée():
            # fait quelque chose avec l'argument `fonction`, par exemple
            # l'appeler avec un argument:
            fonction(42)
        return fonction_retournée

    @mon_décorateur
    def ma_fonction_décorée(un_argument):
        fais_un_truc_avec(un_argument)

Les deux dernières lignes sont équivalentes à::

    def ma_fonction_décorée(un_argument):
        fais_un_truc_avec(un_argument)

    ma_fonction_décorée = mon_décorateur(ma_fonction_décorée)


Exemples de décorateurs
-----------------------

On peut faire un décorateur qui nous empêche
d'appeler une fonction sous certaines conditions::

    def pas_pendant_la_nuit(fonction):
        def résultat():
            if il_fait_nuit:
                print("chut")
            else:
                fonction()
        return résultat

    @pas_pendant_la_nuit
    def dire_bonjour():
        print("bonjour")

    il_fait_nuit = True
    dire_bonjour()
    # afiche: "chut"

Décorateur prenant des arguments
--------------------------------

On peut aussi avoir des arguments passés aux décorateurs. Dans ce cas, on a besoin de
*trois* fonctions imbriquées. En effet, il nous faut une fonction pour traiter l'argument
``message`` et une autre pour traiter l`argument ``fonction``::

    def affiche_message_avant_appel(message):
        def décorateur(fonction):
            def résultat():
                print(message)
                fonction()
            return résultat
        return décorateur

    @affiche_message_avant_appel("dire_bonjour est appelée")
    def dire_bonjour():
        print("bonjour")

    dire_bonjour()
    # affiche:
    # dire_bonjour est appelée
    # bonjour
