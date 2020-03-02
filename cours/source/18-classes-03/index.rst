Chapitre 18 - Classes (3ème partie)
====================================

Rappel - composition
---------------------

Dans le chapitre 13 on a parlé de *composition* qui décrit une relation entre deux classes.

Pour rappel::


    class Chat:
        def __init__(self, nom):
            self.nom = nom

        def ronronne(self):
            print(self.nom, 'fait: "prrrrr"')

        def caresse(self):
            self.ronronne()


    class Enfant:
        def __init__(self, prénom, chat):
            self.chat = chat

        def console(self):
            self.chat.caresse()



Héritage
--------

L'héritage décrit une autre relation entre classes, appelée parfois un peu abusivement "partage de code".

Petit détour
++++++++++++

Commencons par une question - qu'est-ce qui ne va pas dans ce code ?::

    def faire_le_café():
        mettre_café_dans_tasse()
        allumer_bouilloire()
        attendre_que_ça_bouille()
        verser_dans_tasse()
        melanger()

    def faire_le_thé():
        mettre_thé_dans_tasse()
        allumer_bouilloire()
        attendre_que_ça_bouille()
        verser_dans_tasse()
        laisser_infuser()


Le proble est la *duplication* du code. Les lignes de ``allumer_bouilloire()`` à ``verser_dans_tasse()`` sont
identiques.

Du coup:

* Le code est plus long
* Si jamais la procédure pour faire chauffer l'eau change, il faudra changer
  le code a deux endroits différents

Une solution est possible est *d'extraire une fonction*::


    def faire_chauffer_l_eau():
        allumer_bouilloire()
        attendre_que_ça_bouille()


    def faire_le_café():
        mettre_café_dans_tasse()
        faire_chauffer_l_eau()
        verser_dans_tasse()
        melanger()

    def faire_le_thé():
        mettre_thé_dans_tasse()
        faire_chauffer_l_eau()
        verser_dans_tasse()
        laisser_infuser()
