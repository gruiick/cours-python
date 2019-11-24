import string
import sys
import random





def chiffre(chaine, msg):

    mesg_chiffre=""
    i=0

    for lettre in msg:
        pas=ord(chaine[i%len(chaine)])-65

        mesg_chiffre += decale_lettre(pas,lettre)
        i+=1
    return mesg_chiffre


def decale_lettre(pas, lettre):
    let=((ord(lettre)-65) + pas ) % 26
    return chr(let+65)


def main():
    for i in string.ascii_uppercase:
        for j in string.ascii_uppercase:
            for k in string.ascii_uppercase:
              cle=i+j+k
              msg_dechiffre = chiffre(cle, "IHDXUVZKRISCBNJWBXIDUWVVODUBPRFQRIRGBUR")
              if "PLEKSZYGLADZ" in msg_dechiffre:
                  print (cle,msg_dechiffre)
                  #return te sort du main
                  return

main()

#IHDXUVZKRISCBNJWBXIDUWVVODUBPRFQRIRGBUR
