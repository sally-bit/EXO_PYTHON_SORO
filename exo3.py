from math import*
#coding:uft-8

"""
Écrire le même algorithme, mais en utilisant deux variables booléennes pour vérifier l’état de l’eau, sans comparaisons dans les SI.


"""
def somme_n(n,a):
    N=n+1
    som=0
    for elt in range(1,N):
        s1=(1/elt)
        som +=s1
        if som > a:
            print("A partir n =",elt,"Hn depasse a=",a,"jusqu'a ",n)
            break
        
            


cont=True
while cont:
    n=int(input("Entrez le nombre n : "))   
    a=int(input("Entrez le nombre a : "))   
    
    somme_n(n,a)
   
    choix=input("voulez-vous continuez ? oui ou non : ")
    if choix in "non":
        break
    else:
        continue