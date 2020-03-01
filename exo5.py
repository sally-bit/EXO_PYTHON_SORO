from math import*
#coding:uft-8

"""
Une compagnie d'assurance automobile propose à ses clients quatre familles de tarifs identifiables par une couleur, du moins au plus onéreux :
 tarifs bleu, vert, orange et rouge. Le tarif dépend de la situation du conducteur :

un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux ans, se voit attribuer le tarif rouge, si toutefois il n'a jamais été responsable d'accident. Sinon, 
la compagnie refuse de l'assurer.

un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit 
au tarif orange s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident, sinon il est refusé.

un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un accident,
du tarif rouge pour deux accidents, et refusé au-delà

De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la maison depuis plus de cinq ans.
Ainsi, s'il satisfait à cette exigence, un client normalement "vert" devient "bleu", un client normalement "orange" devient "vert", et le "rouge" devient orange.

Ecrire l'algorithme permettant de saisir les données nécessaires (sans contrôle de saisie) et de traiter ce problème.


"""


def demande_client(nom_complet):
    print("BIENVENUE Mr/Mn {} AUX DEMANDES CIENTS DE NOTRE AGENCE \n VEUILLEZ REPONDRE A QUELQUE QUESTION POUR POUVOIR INTEGRER NOTRE AGENCE".format(nom_complet))
    age_conducteur=int(input("Quel age avez-vous ? : "))
    anne_premis=int(input("Depuis combien d'annee vous avez votre permis ? : "))
    accident=int(input("Combien d'accident vous avez eu ? : "))
    
    if age_conducteur < 25 and anne_premis < 2 :
        if accident == 0:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Et vous etez dans la famille de tarif  ROUGE")
        else:
            print("DESOLE Mr/Mm {} vous ne pouvez pas devenir clients de notre agence d'assurances \n parce que vous est responsable {} accident ".format(nom_complet,accident))
    elif (age_conducteur < 25 and anne_premis > 2) or (age_conducteur > 25 and anne_premis < 2):
        if accident == 0:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Et vous etez dans la famille de tarif  ORGANGE")
        elif accident == 1:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Mais ayant provoqué {} accident , vous etez dans la famille de tarif  ROUGE".format(accident))
            
        else:
            print("DESOLE Mr/Mm {} vous ne pouvez pas devenir clients de notre agence d'assurances \n parce que vous est responsable {} accident ".format(nom_complet,accident))
            
    elif age_conducteur > 25 and anne_premis > 2 :
        if accident==0:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Et vous etez dans la famille de tarif  VERT")
        elif accident == 1:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Mais ayant provoqué {} accident , vous etez dans la famille de tarif  ORANGE".format(accident))
        elif accident == 2:
            print("FELICITATION Mr/Mm {} vous etez desormais clients de notre agence d'assurances".format(nom_complet))
            print("Mais ayant provoqué {} accident , vous etez dans la famille de tarif  ROUGE".format(accident))
            
        else:
            print("DESOLE Mr/Mm {} vous ne pouvez pas devenir clients de notre agence d'assurances \n parce que vous est responsable {} accident ".format(nom_complet,accident))       
        
           
            
def client(nom_complet):
    print("BIENVENUE Mr/Mn {} AUX SERVICES FIDELITE , POUR POUVOIR BENEFICIER DES AVANGATAGES  DE  NOTRE AGENCE,\n VEUILLEZ REPONDRE A QUELQUE QUESTION".format(nom_complet))
    anne_client=int(input("Depuis combien d'annee vous etez dans notre agence ? :  "))
    tarif=str(input("Et quel etait tarif (vert, orange et rouge) ? : "))
    if anne_client >= 5:
        print("AVEZ PLUS 5 ANS DE FIDELITE A LA MAISON VOTRE TARIF CHANGER :")
        if tarif in "rouge":
            print("De tarif {}  =====>  tarif orange".format(tarif))
        elif tarif in "orange":
            print("De tarif {}  =====>  tarif vert".format(tarif))
        elif tarif in "vert":
            print("De tarif {}  =====>  tarif bleu".format(tarif))
        else:
            print("veuillez entrer tarif (vert, orange et rouge)")
    else:
        print("DESOLE VOUS NE POUVEZ PAS BENIFICIEZ DES AVANTAGES ,CES AVANTAGES SONT POUR DES CLIENTS QUE ONT 5 ANS DE FIDELITE A L'AGENCE")
        

        
print("BIENVENUE A L'AGENCE D'ASSURANCES,FAITES UN CHOIX")
nom_comp=str(input("Entez vous nom complet : "))
choix=bool(input("etez-vous clients de l'agence? (True ou False):"))
if choix == True:
    client(nom_comp)
else:
    demande_client(nom_comp)         