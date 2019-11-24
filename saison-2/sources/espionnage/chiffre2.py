import string
import sys


def enlever_les_espaces(msg):
    msg_compact = ""
    for lettre in msg:
        if lettre.isalpha():
            msg_compact += lettre
    return msg_compact


def mettre_en_maj(msg):
    msg_maj = msg.upper()
    return msg_maj


def chiffre(chaine, msg):

    mesg_chiffre = ""
    i = 0

    for lettre in msg:
        pas = ord(chaine[i % len(chaine)]) - 65

        mesg_chiffre += decale_lettre(pas, lettre)
        i += 1
    return mesg_chiffre


def decale_lettre(pas, lettre):
    let = ((ord(lettre) - 65) + pas) % 26
    return chr(let + 65)


def main():
    message_compact = enlever_les_espaces(sys.argv[2])
    message_maj = mettre_en_maj(message_compact)
    # argv1 contient une chaine
    message_chiffre = chiffre(sys.argv[1], message_maj)
    print(message_chiffre)


main()
