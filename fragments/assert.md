\center \huge Un nouveau mot-clé

# Les mots-clés

Des mots qui ne peut être utilisé pour des noms de variales.

On a déjà vu: `def`, `class`, `import`, etc ...

Aujourd'hui on va parler de `assert`

# Assertions

* Arrêter immédiatement le programme avec un message
* Ressemble à `sys.exit()`
* Mais usage un peu différent

# Les assertions sont là pour les dévelopeurs

* Le message n'aura en général *aucun* sens si c'est un simple utilisateur
  qui le lit.
* Il indique en général un problème *interne*, dans le code lui-même,
  par opposition aux erreurs *externes*
  
 
Mais on en reparlera :)

# Example

```python

def move_space_ship()
    assert speed < light_speed, "the laws of the universe are broken"

```

