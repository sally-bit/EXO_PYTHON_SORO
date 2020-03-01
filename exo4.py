from math import*
#coding:uft-8

"""



"""


def maximal(r):
    list_max=list()
    R=r+1
    p=0.9
    for elt in range(1,R):
        res=(p**elt)-(1/elt)
        res=round(res,2)
        list_max.append(res)
    print("l'ensembre des valeurs  du nombre p**r - 1/r  dans l'intervalle [1,{}] est la liste => {}".format(r,list_max))
    M=max(list_max)
    M_index=list_max.index(M)+1
    print(" Et le maximun de cet nombre est => {} pour r => {}".format(M,M_index))
    

        
            


cont=True
while cont:
    n=int(input("Entrez le nombre r : "))    
    maximal(n)
   
    choix=input("voulez-vous continuez ? oui ou non : ")
    if choix in "non":
        break
    else:
        continue