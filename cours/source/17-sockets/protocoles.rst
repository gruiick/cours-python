Protocoles
==========

Le problème
------------

Notez que ``send()`` et ``recv()`` sont très basiques:

* On peut appeler ``send()`` plusieurs fois d'affilée
* On peut aussi appeler ``recv()`` alors que le client n'a encore rien envoyé,
  le serveur va juste bloquer en attendant le prochain message du client.
* Si le client envoie 3 octets et que le serveur utilise ``recv(10)``, il n'y
  a pas d'erreur
* Si le client envoie 10 octets et que le serveur utilise ``recv(3)``, il n'y
  a pas non plus d'erreur, et il faut appeler ``recv()`` une deuxième fois
  (avec 7 par exemple) pour récupérer le message en entier


Protocoles
-----------

Ainsi, si on veut que deux machines s'échangent des messages via Internet, il faut
convenir d'un **protocole** - qui parle en premier, quel genre de message peut-il
envoyer? Il faut aussi convenir d'une façon de communiquer la *taille* des réponses.



Le protocole HTTP
-----------------

Le protocole HTTP est relativement simple. On peut le vérifier en essayant
de se connecter à l'adresse ``(93.184.216.34, 80)``, et envoyant les messages
suivants - à l'heure où j'écris ces lignes, l'IP ci-dessus correspond au site
``http://example.com`` ::

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("93.184.216.34", 80))
    s.send(b"GET / HTTP/1.1\r\n")
    s.send(b"Host: example.com\r\n")
    s.send(b"\r\n")

    message = s.recv(351).decode()
    print(message)


Résultat:

.. code-block:: text

   HTTP/1.1 200 OK
   Age: 514391
   Cache-Control: max-age=604800
   Content-Type: text/html; charset=UTF-8
   Date: Sun, 01 Mar 2020 15:57:23 GMT
   Etag: "3147526947+ident"
   Expires: Sun, 08 Mar 2020 15:57:23 GMT
   Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
   Server: ECS (bsa/EB18)
   Vary: Accept-Encoding
   X-Cache: HIT
   Content-Length: 1256

   <!doctype html>


Notez qu'on a appelé `.decode()` sur le message reçu du serveur - on dit que HTTP
est un protocole de *texte*.

Notez que la réponse du serveur rappelle le nom du protocole ``HTTP/1.1`` et répond avec
de nombreuses lignes contenant une *clé* et une *valeur* séparé par des deux-points

On appelle cela des *en-têtes* (ou *headers*). L'un d'eux contient la taille totale du
message: ``Content-Length: 1256``.

Après le bloc de headers, on voit le *corps* de la réponse: quelque chose qui commence
par ``<!doctype html>``.

On peut lire la suite du message::


    suite = s.recv(1000).decode()
    print(suite)

.. code-block:: text

  <html>
  <head>
      <title>Example Domain</title>

      <meta charset="utf-8" />
      <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style type="text/css">
      body {
          background-color: #f0f0f2;
          margin: 0;
          padding: 0;
          font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

      }
      div {
          width: 600px;
          margin: 5em auto;
          padding: 2em;
          background-color: #fdfdff;
          border-radius: 0.5em;
          box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
      }
      a:link, a:visited {
          color: #38488f;
          text-decoration: none;
      }
      @media (max-width: 700px) {
          div {
              margin: 0 auto;
              width: auto;
          }
      }
      </style>
  </head>

  <body>
  <div>
      <h1>Example Domain</h1>
      <p>This domain is for use in illustrative examples in documents. You may use this
      domain in literature without prior coordination or asking for permission.</p>
      <p><a href="https://www.iana.org/domains/example">More information...</a></p>
  </div>
  </body>
  </html>


Si maintenant vous allez sur ``https://example.com`` avec un navigateur Web, et cliquez sur
"Afficher le code source de la page", vous devriez voir exactement le contenu ci-dessus.

Cela prouve que:

* Il y a un serveur qui écoute sur l'adresse IP de example.com, sur le port 80
* Ce serveur comprend le protocole HTTP
* Un navigateur ne fait rien d'autre que:
   * envoyer des requêtes HTTP vers un serveur
   * interpréter le texte retourné et l'afficher
* On peut facilement coder à la fois des *clients* et des *serveur* HTTP en Python, juste avec le module socket.

