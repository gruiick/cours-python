Exemple
=======

Pour ce premier exemple, le client et le serveur vont tourner sur la même machine: la vôtre!

Le processus du serveur tournera dans un premier terminal, et le processus du client dans un autre.

Pour les différencier, on peut utiliser la variable `sys.ps1`.

Étape 1
-------

Ouvrez deux terminaux, lancez dans chacun d'eux la commande `python3` sans arguments, puis tapez::

  >>> import sys
  >>> sys.ps1 = "(serveur) >>> "

dans le premier, et::

  >>> import sys
  >>> sys.ps1 = "(client) >>> "

dans le second.

Vous devriez obtenir le résultat suivant::

    (serveur) >>>

::

    (client) >>>

Dans chacun d'eux, définissez les variables ``IP`` et ``PORT``::

    (serveur) >>> IP = "127.0.0.1"
    (serveur) >>> PORT = 3000

::

    (client) >>> IP = "127.0.0.1"
    (client) >>> PORT = 3000


L'adresse IP ``127.0.0.1`` est spéciale et désigne votre propre machine.
Le PORT 3000 est un port arbitraire


Étape 2
-------

Dans le REPL du serveur, créez une socket du type 'AF_INET' et 'SOCK_STREAM', puis appelez
``bind()`` avec le tuple (IP, PORT) [#f1]_ ::


    (serveur) >>> IP = "127.0.0.1"
    (serveur) >>> PORT = 3000
    (serveur) >>> import socket
    (serveur) >>> s_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    (serveur) >>> s_serveur.bind((IP, PORT))

Ensuite, appelez ``s_serveur.listen(0)``: cela permet à votre serveur d'accepter des connections::

    (serveur) >>> s_serveur.listen(0)

Enfin, appelez ``s_serveur.accept`: cette méthode retourne un tuple qu'on note souvent ``con, addr``::

    (serveur) >>> con, addr = s_serveur.accept()

Cette fois ci, vous devriez constater que le processus du serveur est *bloqué*: l'invite de commande ne s'affiche
pas - en effet, le serveur est en attente d'une connexion par le client


Étape 3
-------

De la même façon que pour le serveur, créez une socket du même type côté
client::

    (client) >>> IP = "127.0.0.1"
    (client) >>> PORT = 3000
    (client) >>> import socket
    (client) >>> s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Ensuite, *connectez* la socket client à la socket serveur::

    (client) >>> s_client.connect((IP, PORT))

Comme par magie, vous devriez voir le processus **dans l'autre terminal** reprendre son exécution:
les deux processus Python sont donc bien en train de *communiquer*


Étape 4
-------

Vous pouvez maintenant utiliser les méthodes ``send()`` et ``recv``, respectivement avec l'objet
``con`` côté serveur, et ``s_client`` côté client pour envoyer et recevoir des messages entre
les deux processus.

Notez que ``send`` prend des ``bytes`` en arguments et renvoie le nombre d'octets envoyés,
et que ``recv()`` prend un nombre d'octets à lire.

On peut envoyer des message du client vers le serveur::


    (client) >>> s_client.send(b"Bonjour")
    7

::

    (serveur) >>> con.recv(7)
    b'Bonjour'


Et du serveur vers le client::

    (serveur) >>> con.send(b"Comment va ?")
    12

::

    (client) >>> s_client.recv(12)
    b'Comment va ?'


.. rubric:: notes

.. [#f1] Il existe des sockets de plusieurs type et avec des comportements différents. AF_INET et SOCK_STREAM sont
         les plus courants.
