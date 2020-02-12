Types
=====

.. code-block:: python

   >>> a = 42
   >>> message = "La réponse est: " + a
   TypeError: can only concatenate str (not "int") to str

*Notre premier message d'erreur !*

On ne mélange pas les torchons et les serviettes!

Conversions
-----------

Entier vers string
++++++++++++++++++

.. code-block:: python

    >>> a = 42
    >>> message = "La réponse est: " + str(a)
    >>> message
    'La réponse est 42'

String vers entier
++++++++++++++++++

.. code-block:: python

   >>> answer = int("42")
   >>> answer
   42

Notez les parenthèses autour des valeurs.
