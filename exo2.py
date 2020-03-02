from math import*
#coding:uft-8

"""
Écrire le même algorithme, mais en utilisant deux variables booléennes pour vérifier l’état de l’eau, sans comparaisons dans les SI.


"""


def etat_eau(Tre):
    tem_eleve=Tre>100
    tem_bas=Tre<0
    if tem_eleve:
        print("l'eau est a l'etat vapeur")
    elif tem_bas:
        print("l'eau est a l'etat glace")
       
    else:
        print("l'eau est a l'etat liquide")
        

while cont:
    temperature=float(input("Entrez la temperature de l'eau pour voir son etat : "))   
    etat_eau(temperature)     
    choix=input("voulez-vous continuez ? oui ou non : ")
    if choix in "non":
        break
    else:
        continue
