from math import*
#coding:uft-8

"""
Écrire, avec des comparaisons, un algorithme qui affiche l’état de l’eau (glace, liquide, vapeur) en fonction de sa température.

"""

def etat_eau(Tre):
    if Tre >48:
        print("l'eau est a l'etat vapeur")
    elif Tre<0:
        print("l'eau est a l'etat glace")
    else:
        print("l'eau est a l'etat liquide")
    



while cont:
    temperature=int(input("Entrez la temperature de l'eau pour voir son etat : "))   
    etat_eau(temperature)     
    choix=input("voulez-vous continuez ? oui ou non : ")
    if choix in "non":
        break
    else:
        continue