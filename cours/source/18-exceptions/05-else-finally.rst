Else et finally
===============

else
----

Si on rajoute un bloc ``else`` après le ``except``, le bloc n'est éxécuté que si
*aucune* exception n'a été levée::

    try:
    	tente_un_truc_risqué()
    except (ZeroDivisionError, FileNotFoundError):
        print("raté")
    else:
        print("ouf - ça a marché")

finally
--------

Si on rajoute un bloc ``finally`` après le ``except``, le bloc est éxécuté *dans tous les cas*,
qu'une exception ait été levée ou non. On s'en sert souvent pour "annuler" du code
qui aurait été utilisé dans le bloc ``try``::


    personnage = Personnage()
    try:
        personnage.entre_en_scène()
    	personnage.tente_un_truc_risqué()
    except ZeroDivisionError:
        print("raté")
    finally:
        personnage.quitte_la_scène()


Si dans le bloc ``try`` une exception **différente** de ``ZeroDivisionError`` est
levée, on passera *quand même* dans le bloc ``finally``, *puis* l'exception sera
levée à nouveau.
