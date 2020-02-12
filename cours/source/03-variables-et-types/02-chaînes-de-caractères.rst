Chaînes de caractères
======================

Aussi appelées "string".


Avec des simple quotes (``'``)

.. code-block:: python

    >>> 'Bonjour monde!'
    'Bonjour monde!'

Marche aussi avec des double quotes (`"`)

.. code-block:: python

    >>> "Bonjour, monde!"
    'Bonjour monde'

Double et simple quotes
-----------------------

On peut mettre des simples quotes dans des double quotes et vice-versa.

.. code-block:: python

   >>> "Il a dit: 'bonjour' ce matin."
   "Il a dit: 'bonjour' ce matin."

   >>> 'Il a dit: "bonjour" ce matin'
   'Il a dit: "bonjour" ce matin!'


Échappement
-----------


Avec la barre oblique inversée "backslash"


.. code-block:: python

   >>> 'Il a dit: "bonjour". C\'est sympa!'
   'Il a dit: "bonjour". C\'est sympa!'


Concaténation
-------------


.. code-block:: python

   >>> name = "John"
   >>> message = "Bonjour " + name + " !"
   >>> message
   "Bonjour John !"
