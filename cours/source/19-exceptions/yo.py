class Personnage:
    def tente_un_truc_risqué(self):
        1 / 0

    def quitte_la_scène(self):
        print("je m'en vais")


def entre_en_scène():
    return Personnage()


personnage = entre_en_scène()
try:
    personnage.tente_un_truc_risqué()
except FileNotFoundError:
    print("raté")
personnage.quitte_la_scène()
