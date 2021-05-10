Objets
======

En fait, *tout ce qu'on manipule en Python* est un objet. Et tous les objets sont
toujours des instances d'une classe. On peut accéder à la classe qui a servi
à instancier un objet avec la fonction ``type``, par exemple::

    class MaClasse:
        pass

    mon_instance = MaClasse()
    print(type(mon_instance))
    # affiche:
    # <class '__main__.MaClasse'>


Mais aussi : ::

    print(type(2))
    # affiche: int

    print(type("bonjour"))
    # affiche: str

Donc en Python, les entiers sont des instances de la classe ``int``, et les 
strings des instances de la classe ``str``.

Ainsi, vous pouvez voir l'expression ``x = str(y)`` de deux façons :

* Soit on appelle la fonction native ``str`` pour convertir ``y`` en string.

* Soit on crée une nouvelle instance de la classe ``str`` en appelant le constructeur
  de la classe ``str`` avec ``y`` en argument.

Notez que ça ne s'arrète pas là : ::

    def ma_fonction():
        pass

    print(type(ma_fonction))
    # affiche: function

    class MaClasse:
        def ma_méthode(self):
            pass

    mon_instance = MaClasse()
    print(type(mon_instance.ma_méthode))
    # affiche: method

    import sys
    print(type(sys))
    # affiche: module


Et même : ::

    print(type(MaClasse))
    # affiche: type

    print(type(type))
    # affiche: type

Et oui, les classes elles-mêmes sont des instances de classe ! (de la classe ``type``)

Du coup en Python, le terme 'objet' désigne *toujours* une instance de classe, même
``None`` est une instance d'une classe (elle s'appelle ``NoneType``).

Ordre de résolution
-------------------

Il est temps de revenir sur l'évaluation des expressions impliquant des
attributs.

On a vu trois systèmes différents :

Appeler une fonction définie dans un module : ::

    import mon_module
    mon_module.ma_fonction()

Appeler une méthode d'instance définie dans une classe : ::

    mon_instance = MaClasse()
    mon_instance.ma_méthode()

Appeler une méthode de classe définie dans une classe : ::

    MaClasse.ma_méthod_de_classe()

D'après ce qu'on a vu dans la section précédente, on sait maintenant que
dans tous les cas, à gauche du point se situe un objet, et que tous
les objets sont des instances d'une classe (appelé le "type" de l'objet).

Pour évaluer l'expression ``mon_objet.mon_attribut``, où ``mon_objet`` est une
instance de ``mon_type``, Python cherche toujours l'attribut dans deux endroits :

* d'abord en tant qu'attribut de l'instance ``mon_objet`` ;
* ensuite, en tant qu'attribut de la classe ``mon_type``.

La recherche se poursuit ainsi en suivant toutes les classe parentes de
``mon_type``.


On peut voir ce mécanisme en action dans le code suivant : ::

    class A:
        def f1(self):
            print("f1 dans A")

        def f2(self):
            print("f2")


    class B(A):
        @classmethod
        def f3(cls):
            print("f3")

        def f1(self):
            print("f1 dans B")


    b = B()
    b.f1()
    b.f3()
    b.f2()
    # affiche:
    # f1 dans B
    # f3
    # f2


Conclusion
----------

Maintenant, vous devriez comprendre pourquoi on dit parfois qu'en
Python, **tout est objet**.

Dans un prochain chapitre, on expliquera pourquoi, en plus de cela,
on peut dire qu'en Python, **tout est dictionnaire**.
