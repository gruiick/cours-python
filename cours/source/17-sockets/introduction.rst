Introduction
=============

Clients et serveurs
-------------------

Dans le chapitre 15, nous avons parlé des données binaires et évoqué le
fait que cela permettait à nos programmes Python d'intéragir avec
l'extérieur, notamment via le système de fichiers.

Il existe dans la librairie standard une autre façon pour Python de
communiquer via *le réseau* : il s'agit du module ``socket``.

Une communication sur le réseau Internet implique:

* Un *client* qui va faire des *requêtes*
* Un *serveur* qui va renvoyer des *réponses* au client
* Une *adresse* du serveur utilisée par le client

Dans notre cas, cette adresse est un *tuple*, composé de deux éléments:
une *adresse IP* et un *port*.

.. image:: /img/client-serveur.png

En général:

* Le *client* et le *serveur* sont sur des machines différentes
* Il n'y a qu'un seul processus qui est capable d'écouter sur un port donné
