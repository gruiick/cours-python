% Programmation avec Python (chapitre 11)
% Dimitri Merejkowsky


\center \huge L'E2L est présente sur le fediverse

# Le fediverse

Note: seulement si j'ai le temps

\center \huge Retour sur les virtualenvs

python3 -m venv chemin
source chemin/bin/activate
out
chemin/bin/activate/binaire

en particulier:
toujours lancer pip depuis un virtualenv

rajouter une dépendance:
pip install <le nom> (trouvé sur pypi)
recherche des deps

pip istall <le nom> --upgrade pour mettre à jour

\center \huge pytest et TDD

on n'a fait que du code *de production* jusque là

assert

example de test avec pytest

digression: les 2 valeurs du code

- valeur primaire: le produit! le programme, le site web, etc.
- valeur secondaire: le fait qu'on puisse *modifier* le programme
  (d'où le nom *soft* ware)

les tests n'aident pas la valeur primaire, mais ils sont indispensables
pour la valeur secondaire

changement: tout change tout le temps!
necessité des refactorings -> vus tout du long, a chaque atelier
comment ne rien casser?
-> les tests


tdd: une *discipline* pour faire evoluer le code de production et le
code de prod *en même temps*

3 règles
un cycle


\center \huge Atelier

Le jeu de bowling

